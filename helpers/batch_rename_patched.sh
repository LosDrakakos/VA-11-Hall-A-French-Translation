#!/usr/bin/env bash

find . -depth -type f -name 'patched_*' -print0 |
while IFS= read -r -d '' file; do
    dir="$(dirname "$file")"
    base="$(basename "$file")"
    new_name="${base#patched_}"
    new_path="$dir/$new_name"

    echo "Renaming: '$file' -> '$new_path'"
    mv -- "$file" "$new_path"
done