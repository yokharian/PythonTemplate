#!/bin/bash

# URL to download
URL="https://raw.githubusercontent.com/pdm-project/pdm/refs/heads/main/README.md"

# Path to save the file
OUTPUT_FILE="./HOW_TO_INSTALL_PDM.md"

# Download the file and trim content to start from "## Installation"
curl -s "$URL" | awk '/^## Installation/ {print_flag=1} print_flag' > "$OUTPUT_FILE"

echo "Trimmed content starting from '## Installation' and saved to $OUTPUT_FILE"
