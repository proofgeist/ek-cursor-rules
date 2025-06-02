#!/bin/bash

# Cursor Rules Import Script
# Imports cursor rules into a new project

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Script directory (where the rules are located)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RULES_SOURCE="$SCRIPT_DIR/rules"

# Default values
TARGET_DIR=""
LINK_TYPE="copy"
RULE_SETS="all"
FORCE=false

# Help function
show_help() {
    echo -e "${BLUE}Cursor Rules Import Script${NC}"
    echo ""
    echo "Usage: $0 [OPTIONS] TARGET_DIRECTORY"
    echo ""
    echo "Options:"
    echo "  -l, --link-type TYPE    How to import rules: copy, symlink, hardlink, dirsymlink (default: copy)"
    echo "  -r, --rules SETS        Which rule sets: all, general, python, git, or comma-separated (default: all)"
    echo "  -f, --force             Overwrite existing .cursor directory"
    echo "  -h, --help              Show this help message"
    echo ""
    echo "Link Types:"
    echo "  copy        Independent copies (safe for modification)"
    echo "  symlink     File-level symlinks (updates with source changes)"
    echo "  hardlink    File-level hardlinks (shared file data, updates with source)"
    echo "  dirsymlink  Directory-level symlink to entire rules folder (most efficient)"
    echo ""
    echo "Examples:"
    echo "  $0 /path/to/my-project                        # Copy all rules"
    echo "  $0 -l dirsymlink /path/to/my-project          # Symlink entire rules directory"
    echo "  $0 -l hardlink /path/to/my-project            # Hardlink all files"
    echo "  $0 -r general,git /path/to/my-project         # Only general and git rules"
    echo "  $0 -r python -f /path/to/python-project      # Python rules, force overwrite"
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -l|--link-type)
            LINK_TYPE="$2"
            shift 2
            ;;
        -r|--rules)
            RULE_SETS="$2"
            shift 2
            ;;
        -f|--force)
            FORCE=true
            shift
            ;;
        -h|--help)
            show_help
            exit 0
            ;;
        -*)
            echo -e "${RED}Error: Unknown option $1${NC}"
            show_help
            exit 1
            ;;
        *)
            if [[ -z "$TARGET_DIR" ]]; then
                TARGET_DIR="$1"
            else
                echo -e "${RED}Error: Multiple target directories specified${NC}"
                exit 1
            fi
            shift
            ;;
    esac
done

# Validate arguments
if [[ -z "$TARGET_DIR" ]]; then
    echo -e "${RED}Error: Target directory is required${NC}"
    show_help
    exit 1
fi

if [[ ! "$LINK_TYPE" =~ ^(copy|symlink|hardlink|dirsymlink)$ ]]; then
    echo -e "${RED}Error: Link type must be copy, symlink, hardlink, or dirsymlink${NC}"
    exit 1
fi

# Check if source rules exist
if [[ ! -d "$RULES_SOURCE" ]]; then
    echo -e "${RED}Error: Rules directory not found at $RULES_SOURCE${NC}"
    exit 1
fi

# Create target directory if it doesn't exist
if [[ ! -d "$TARGET_DIR" ]]; then
    echo -e "${YELLOW}Target directory doesn't exist. Creating: $TARGET_DIR${NC}"
    mkdir -p "$TARGET_DIR"
fi

# Check if .cursor already exists
CURSOR_DIR="$TARGET_DIR/.cursor"
if [[ -d "$CURSOR_DIR" ]] && [[ "$FORCE" != true ]]; then
    echo -e "${YELLOW}Warning: .cursor directory already exists in $TARGET_DIR${NC}"
    echo -e "${YELLOW}Will skip existing files. Use --force to overwrite everything.${NC}"
fi

# Remove existing .cursor if force is enabled
if [[ -d "$CURSOR_DIR" ]] && [[ "$FORCE" == true ]]; then
    echo -e "${YELLOW}Removing existing .cursor directory...${NC}"
    rm -rf "$CURSOR_DIR"
fi

# Handle directory-level symlink (special case)
if [[ "$LINK_TYPE" == "dirsymlink" ]]; then
    echo -e "${BLUE}Creating directory-level symlink to entire rules folder...${NC}"
    mkdir -p "$CURSOR_DIR"
    
    # Check if rules symlink already exists
    if [[ -L "$CURSOR_DIR/rules" ]] && [[ "$FORCE" != true ]]; then
        echo -e "${YELLOW}Rules symlink already exists, skipping...${NC}"
    elif [[ -d "$CURSOR_DIR/rules" ]] && [[ "$FORCE" != true ]]; then
        echo -e "${YELLOW}Rules directory already exists, skipping symlink creation...${NC}"
    else
        if [[ -e "$CURSOR_DIR/rules" ]] && [[ "$FORCE" == true ]]; then
            rm -rf "$CURSOR_DIR/rules"
        fi
        ln -s "$RULES_SOURCE" "$CURSOR_DIR/rules"
        echo -e "${GREEN}Directory symlink created successfully${NC}"
    fi
    
    # Create .cursorignore file
    if [[ ! -f "$TARGET_DIR/.cursorignore" ]]; then
        echo -e "${BLUE}Creating .cursorignore file...${NC}"
        cat > "$TARGET_DIR/.cursorignore" << EOF
# Cursor rules directory (symlinked to source)
.cursor/

EOF
    else
        echo -e "${YELLOW}.cursorignore already exists, skipping...${NC}"
    fi
    
    # Success message
    echo ""
    echo -e "${GREEN}✅ Cursor rules processing completed for $TARGET_DIR${NC}"
    echo -e "${BLUE}Link type: directory symlink${NC}"
    echo -e "${BLUE}All rule sets included via directory link${NC}"
    echo ""
    echo -e "${YELLOW}Next steps:${NC}"
    echo "1. Navigate to your project: cd $TARGET_DIR"
    echo "2. Open the project in Cursor"
    echo "3. The rules will be automatically applied"
    echo ""
    echo -e "${YELLOW}Note: Directory symlink means ALL changes to source rules will affect this project${NC}"
    exit 0
fi

# Create .cursor directory for file-level operations
echo -e "${BLUE}Creating .cursor directory in $TARGET_DIR${NC}"
mkdir -p "$CURSOR_DIR/rules"

# Function to import rule set
import_rule_set() {
    local rule_set="$1"
    local source_dir="$RULES_SOURCE/$rule_set"
    local target_subdir="$CURSOR_DIR/rules/$rule_set"
    
    if [[ ! -d "$source_dir" ]]; then
        echo -e "${YELLOW}Warning: Rule set '$rule_set' not found, skipping...${NC}"
        return
    fi
    
    echo -e "${GREEN}Importing $rule_set rules...${NC}"
    mkdir -p "$target_subdir"
    
    # Import files based on link type
    case "$LINK_TYPE" in
        copy)
            # Copy files, skip if they exist and force is not enabled
            find "$source_dir" -type f -exec bash -c '
                rel_path="${1#'"$source_dir"'/}"
                target_file="'"$target_subdir"'/$rel_path"
                mkdir -p "$(dirname "$target_file")"
                if [[ ! -f "$target_file" ]] || [[ "'"$FORCE"'" == true ]]; then
                    cp "$1" "$target_file"
                    echo "  Copied: $rel_path"
                else
                    echo "  Skipped (exists): $rel_path"
                fi
            ' _ {} \;
            ;;
        symlink)
            # Create symlinks for each file, skip if they exist
            find "$source_dir" -type f -exec bash -c '
                rel_path="${1#'"$source_dir"'/}"
                target_file="'"$target_subdir"'/$rel_path"
                mkdir -p "$(dirname "$target_file")"
                if [[ ! -e "$target_file" ]] || [[ "'"$FORCE"'" == true ]]; then
                    [[ "'"$FORCE"'" == true ]] && rm -f "$target_file"
                    ln -s "$1" "$target_file"
                    echo "  Symlinked: $rel_path"
                else
                    echo "  Skipped (exists): $rel_path"
                fi
            ' _ {} \;
            ;;
        hardlink)
            # Create hard links for each file recursively, skip if they exist
            find "$source_dir" -type f -exec bash -c '
                rel_path="${1#'"$source_dir"'/}"
                target_file="'"$target_subdir"'/$rel_path"
                mkdir -p "$(dirname "$target_file")"
                if [[ ! -f "$target_file" ]] || [[ "'"$FORCE"'" == true ]]; then
                    [[ "'"$FORCE"'" == true ]] && rm -f "$target_file"
                    ln "$1" "$target_file"
                    echo "  Hardlinked: $rel_path"
                else
                    echo "  Skipped (exists): $rel_path"
                fi
            ' _ {} \;
            ;;
    esac
}

# Determine which rule sets to import
if [[ "$RULE_SETS" == "all" ]]; then
    # Import all available rule sets
    for rule_dir in "$RULES_SOURCE"/*; do
        if [[ -d "$rule_dir" ]]; then
            rule_set=$(basename "$rule_dir")
            import_rule_set "$rule_set"
        fi
    done
else
    # Import specific rule sets
    IFS=',' read -ra RULE_ARRAY <<< "$RULE_SETS"
    for rule_set in "${RULE_ARRAY[@]}"; do
        rule_set=$(echo "$rule_set" | xargs) # trim whitespace
        import_rule_set "$rule_set"
    done
fi

# Create a .cursorignore file to avoid tracking the rules themselves
if [[ ! -f "$TARGET_DIR/.cursorignore" ]]; then
    echo -e "${BLUE}Creating .cursorignore file...${NC}"
    cat > "$TARGET_DIR/.cursorignore" << EOF
# Cursor rules directory (if using symlinks/hardlinks)
.cursor/

EOF
fi

# Success message
echo ""
echo -e "${GREEN}✅ Cursor rules successfully imported to $TARGET_DIR${NC}"
echo -e "${BLUE}Link type: $LINK_TYPE${NC}"
echo -e "${BLUE}Rule sets: $RULE_SETS${NC}"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "1. Navigate to your project: cd $TARGET_DIR"
echo "2. Open the project in Cursor"
echo "3. The rules will be automatically applied"
echo ""

if [[ "$LINK_TYPE" == "symlink" ]] || [[ "$LINK_TYPE" == "hardlink" ]]; then
    echo -e "${YELLOW}Note: Using $LINK_TYPE means changes to rules in the source will affect this project${NC}"
fi 