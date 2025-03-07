#!/bin/sh
set -e

# Define the directory containing the .adoc files
APP_DIR=/srv/app
DOC_DIR=${DOC_DIR:-"/documents"}
RESOURCES_DIR="${DOC_DIR}/resources"
OUTPUT_DIR="${DOC_DIR}/output"
LOG_FILE="${OUTPUT_DIR}/asciidoctor.log"
DCATAPES_IMG_DIR="${DOC_DIR}/img"
DEBUG=${DEBUG:-False}
# Set default language if not provided
LANG=${LANG:-"es"}
PDF_PREFIX=${PDF_PREFIX:-"dcat-ap-es"}


if [ "$DEBUG" = "True" ]; then
  echo "=== Environment variables ==="
  env
  echo "=== Directory structure ==="
  ls -la ${DOC_DIR}
  echo "=== Available .adoc files ==="
  find ${DOC_DIR} -name "*.adoc"
fi


# Function to extract theme from asciidoc header
get_theme_from_header() {
    local file="$1"
    # Try to find :pdf-theme: in the header
    local theme=$(grep -m 1 "^:pdf-theme:" "$file" | cut -d' ' -f2-)
    # If no theme found, return default
    if [ -z "$theme" ]; then
        echo "custom-theme"
        return
    fi
    # Remove .yml extension if present
    theme="${theme%.yml}"
    echo "$theme"
}

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Clear the log file
> "$LOG_FILE"

# Initialize theme name and paths
if [ -z "$DEFAULT_THEME" ]; then
  THEME_NAME="custom-theme"
else
  THEME_NAME="${DEFAULT_THEME%.*}"
fi

# Find only .adoc files in the DOC_DIR (not in subdirectories)
find "$DOC_DIR" -maxdepth 1 -name '*.adoc' | while read -r file; do
  echo "Processing file: $file"
  relative_path="${file#$DOC_DIR/}"
  basename="${relative_path%.*}"
  
  # Get theme from file header and ensure .yml extension
  THEME_NAME=$(get_theme_from_header "$file")
  
  # Configure theme options for PDF with dynamic theme
  THEME_OPTS="
    -r ${RESOURCES_DIR}/extensions/admonition-by-type.rb \
    -r ${RESOURCES_DIR}/extensions/codeblock-language-label.rb \
    -r ${RESOURCES_DIR}/extensions/admonition-labels.rb \
    -a pdf-theme=${RESOURCES_DIR}/theme/${THEME_NAME}.yml \
    -a pdf-fontsdir=${RESOURCES_DIR}/fonts;GEM_FONTS_DIR \
    -a lang=${LANG} \
    --trace
  "

  # Check if the filename contains a language suffix
  case "$basename" in
    *.en|*.es)
      # Extract language from filename
      file_lang=${basename##*.}
      base_name=${basename%.*}
      pdf_output="${OUTPUT_DIR}/${PDF_PREFIX}-${base_name}.${file_lang}.pdf"
      ;;
    *)
      # No language suffix found, use default Spanish
      pdf_output="${OUTPUT_DIR}/${PDF_PREFIX}-${basename}.es.pdf"
      ;;
  esac
  
  mkdir -p "$(dirname "$pdf_output")"
  
  # Convert to PDF with PDF theme
  echo "Converting $file to PDF: $pdf_output"
  if ! asciidoctor-pdf -r asciidoctor-diagram -a allow-uri-read $THEME_OPTS -o "$pdf_output" "$file" 2>> "$LOG_FILE"; then
    echo "Error converting to PDF. Check $LOG_FILE for details."
  fi
done

# Remove all .asciidoctor directories if they exist
find "$DOC_DIR" -type d -name '.asciidoctor' -exec rm -rf {} +

# Execute the original command
exec "$@"