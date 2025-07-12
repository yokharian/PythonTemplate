#!/bin/bash
cd ./overrides/.icons/ || exit
mkdir -p vscode-icons/{,folder,opened-folder}/
cd vscode-icons || exit

icons=(
  git
  gitlab
  markdown
  toml
  unlicense
  python
  yaml
)

folderIcons=(
  dist
  docs
  gitlab
  python
  test
  vscode
)

openedFolderIcons=(
  python
)

allIcons=()
allIconsPath=()

allIcons+=("default_file.svg")
allIconsPath+=("default.svg")

allIcons+=("default_folder.svg")
allIconsPath+=("folder/default.svg")

allIcons+=("default_folder_opened.svg")
allIconsPath+=("opened-folder/default.svg")

for icon in "${icons[@]}"; do
  allIcons+=("file_type_${icon}.svg")
  allIconsPath+=("${icon}.svg")
done

for icon in "${folderIcons[@]}"; do
  allIcons+=("folder_type_${icon}.svg")
  allIconsPath+=("folder/${icon}.svg")
done

for icon in "${openedFolderIcons[@]}"; do
  allIcons+=("folder_type_${icon}_opened.svg")
  allIconsPath+=("opened-folder/${icon}.svg")
done

for i in "${!allIcons[@]}"; do
  # Check if file already exists
  if [ -f "${allIconsPath[i]}" ]; then
    echo "File ${allIconsPath[i]} already exists, skipping download"
  else
    echo "Downloading ${allIcons[i]}"
    curl -s -o "${allIconsPath[i]}" "https://raw.githubusercontent.com/vscode-icons/vscode-icons/master/icons/${allIcons[i]}" \
      || echo "Error downloading ${allIcons[i]}"
  fi
done
