#!/bin/sh

# Define the directory containing the .adoc files
APP_DIR=/srv/app
DOC_DIR=${DOC_DIR:-"/documents"}
RESOURCES_DIR="${DOC_DIR}/resources"
BASE_OUTPUT_DIR="${DOC_DIR}/output"
OUTPUT_DIR="${BASE_OUTPUT_DIR}/adoc"
LOG_FILE="${BASE_OUTPUT_DIR}/md2adoc.log"
DCATAPES_IMG_DIR="${DOC_DIR}/img"
DEFAULT_THEME="${DEFAULT_THEME:-"datosgobes-theme.yml"}"

# Create output directories if they don't exist
mkdir -p ${OUTPUT_DIR}

# Function to process AsciiDoc content
process_asciidoc() {
    local file="$1"
    local temp_file="${file}.tmp"
    local date=$(date '+%Y%m%d')
    local backup_file="${file}.${date}.bak"
    echo "Processing file: $file"

    # Create backup with date
    cp "$file" "$backup_file"

    # Add PDF theme to header if not present
    if ! grep -q "^:pdf-theme:" "$file"; then
        # Create temporary file with new header
        {
            echo ":pdf-theme: ${DEFAULT_THEME}"
            cat "$file"
        } > "$temp_file"
        mv "$temp_file" "$file"
    fi

    # 1. Fix code blocks - multiline pattern
    awk '
        BEGIN { in_block = 0 }
        /^!!! info.*/ { 
            in_block = 1
            next
        }
        in_block && /`\+turtle linenums="1"/ {
            print "[source,turtle]"
            print "----"
            next
        }
        in_block && /--8<-- "/ {
            gsub(/"/, "", $0)
            gsub(/--8<-- /, "", $0)
            # Remove leading/trailing spaces and tabs
            gsub(/^[ \t]+|[ \t]+$/, "", $0)
            print "include::" $0 "[]"
            next
        }
        in_block && /\+`/ {
            print "----"
            in_block = 0
            next
        }
        { print }
    ' "$file" > "$temp_file" && mv "$temp_file" "$file"

    # # 2. Fix admonitions with content - corrected syntax
    # awk '
    # BEGIN { 
    #     in_admonition = 0;
    #     content = "";
    #     type = "";
    #     title = "";
    # }
    # /^!!! must/ || /^!!! should/ || /^!!! may/ {
    #     in_admonition = 1;
    #     type = $2;
    #     $1 = ""; $2 = "";  # Remove !!! and type
    #     # Extract title if present
    #     if (match($0, /"([^"]+)"/, arr)) {
    #         title = arr[1];
    #     }
    #     # Convert type
    #     if (type == "must") { type = "CAUTION"; }
    #     if (type == "should") { type = "WARNING"; }
    #     if (type == "may") { type = "TIP"; }
    #     next;
    # }
    # in_admonition == 1 && /^[[:space:]]*$/ {  # Empty line
    #     # Print collected content
    #     if (title != "") {
    #         print type ": " title;
    #     }
    #     if (content != "") {
    #         print content;
    #     }
    #     # Reset
    #     in_admonition = 0;
    #     content = "";
    #     title = "";
    #     next;
    # }
    # in_admonition == 1 {  # Collect content
    #     if (content == "") {
    #         content = $0;
    #     } else {
    #         content = content "\n" $0;
    #     }
    #     next;
    # }
    # {
    #     print;
    # }
    # END {
    #     if (in_admonition == 1) {
    #         if (title != "") {
    #             print type ": " title;
    #         }
    #         if (content != "") {
    #             print content;
    #         }
    #     }
    # }' "$file" > "$temp_file" && mv "$temp_file" "$file"

    # # 3. Add document header for all AsciiDoc files
    # {
    #     # Save original content without header and doctype
    #     awk '!/^[[:space:]]*\[#.*\]/ && !/^[[:space:]]*=/ && !/^:doctype:/' "$file" > "${temp_file}.content"

    #     # Create new file with header
    #     {
    #         echo "= Título del documento"
    #         echo ":sectnums:"
    #         echo ":toc:"
    #         echo ":toc-title: Table of Contents"
    #         echo ":source-highlighter: rouge"
    #         echo ":rouge-style: github"
    #         echo ":autofit-option:"
    #         echo ":icons: font"
    #         echo ":imagesdir: ."
    #         echo ":front-cover-image: image::img/cover-dcat-ap-es-conventions.en.png[]"
    #         echo
    #         cat "${temp_file}.content"
    #     } > "$temp_file"

    #     # Replace original with new version
    #     mv "$temp_file" "$file"
    #     rm -f "${temp_file}.content"

    #     # Convert first-level heading to second-level
    #     sed -i '0,/^= / s/^= /== /' "$file"
    # }

    # Debug output
    echo "File processed. Checking results..."
    grep -A 2 "CAUTION:\|WARNING:\|TIP:" "$file" || echo "No admonitions found"
    grep -A 3 "\[source,turtle\]" "$file" || echo "No code blocks found"
}

# Convert all markdown files in DOC_DIR
find ${DOC_DIR} -name "*.md" -type f | while read -r file; do
    # Get relative path from DOC_DIR
    rel_path=${file#${DOC_DIR}/}
    # Create output directory structure
    mkdir -p "${OUTPUT_DIR}/$(dirname "${rel_path}")"
    output_file="${OUTPUT_DIR}/${rel_path%.md}.adoc"
    
    # Convert file to AsciiDoc
    kramdoc --auto-ids \
           --auto-id-prefix=_ \
           --auto-id-separator=_ \
           --imagesdir=img \
           -o "$output_file" \
           "$file"
           
    # Process the generated AsciiDoc
    process_asciidoc "$output_file"
done

echo "Conversion completed. Check ${OUTPUT_DIR} for the AsciiDoc files."