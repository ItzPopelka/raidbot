#!/bin/bash

echo "========================================"
echo "RaidBot Updater"
echo "========================================"
echo
BACKUP_DIR="backup_$(date +'%Y-%m-%d_%H-%M')"
GIT_REPO="https://github.com/ItzPopelka/raidbot.github.io"
EXCLUDE=("token.json" "assets/pfp.webp")
echo "Creating backup directory..."
mkdir -p "$BACKUP_DIR"
echo
echo "Backing up current files to $BACKUP_DIR..."
echo
find . -maxdepth 1 -type f -name "*" | while read -r file; do
    filename=$(basename "$file")
    exclude_file=0
    for exclude in "${EXCLUDE[@]}"; do
        if [ "$filename" = "$exclude" ] || [[ "$file" == *"/$exclude" ]]; then
            exclude_file=1
            break
        fi
    done
    if [ $exclude_file -eq 0 ]; then
        echo "Backing up: $filename"
        cp -r "$file" "$BACKUP_DIR/" 2>/dev/null
    fi
done
find . -type d -mindepth 1 -maxdepth 1 | while read -r dir; do
    dirname=$(basename "$dir")
    if [ "$dirname" != "$BACKUP_DIR" ]; then
        echo "Backing up directory: $dirname"
        mkdir -p "$BACKUP_DIR/$dirname"
        find "$dir" -type f | while read -r file; do
            relpath="${file#./}"
            exclude_file=0
            for exclude in "${EXCLUDE[@]}"; do
                if [ "$relpath" = "$exclude" ] || [[ "$relpath" == "$exclude" ]]; then
                    exclude_file=1
                    break
                fi
            done
            if [ $exclude_file -eq 0 ]; then
                cp "$file" "$BACKUP_DIR/$relpath" 2>/dev/null
            fi
        done
    fi
done
echo
echo "========================================"
echo "Downloading latest files from GitHub..."
echo "========================================"
echo
mkdir -p temp_update
cd temp_update || exit
echo "Downloading repository..."
wget -q "$GIT_REPO/archive/main.zip" -O repo.zip
echo "Extracting files..."
unzip -q repo.zip
for dir in */; do
    if [ -d "$dir" ]; then
        echo "Copying files from ${dir%/}..."
        find "$dir" -type f | while read -r file; do
            relpath="${file#$dir}"
            exclude_file=0
            for exclude in "${EXCLUDE[@]}"; do
                if [ "$relpath" = "$exclude" ] || [[ "$relpath" == "$exclude" ]]; then
                    exclude_file=1
                    break
                fi
            done
            if [ $exclude_file -eq 0 ]; then
                echo "Updating: $relpath"
                mkdir -p "../$(dirname "$relpath")"
                cp "$file" "../$relpath" 2>/dev/null
            else
                echo "Skipping: $relpath"
            fi
        done
    fi
done
cd ..
rm -rf temp_update
echo
echo "========================================"
echo "Update completed!"
echo "========================================"
echo
echo "Original files backed up to: $BACKUP_DIR"
echo "Excluded from update: ${EXCLUDE[*]}"
echo