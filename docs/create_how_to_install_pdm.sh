#!/bin/bash

# URL to download
URL="https://raw.githubusercontent.com/pdm-project/pdm/refs/heads/main/README.md"

# Path to save the file
OUTPUT_FILE="./src/how_to_install_pdm.md"

if [ -f "${OUTPUT_FILE}" ]; then
  echo "File ${OUTPUT_FILE} already exists, skipping download"
else
  # Download the file and trim content to start from "## Installation"
  curl -s "$URL" | awk '/^## Installation/ {print_flag=1} print_flag' > "$OUTPUT_FILE"
  echo "Trimmed content starting from '## Installation' and saved to $OUTPUT_FILE"
fi


