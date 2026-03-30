#!/usr/bin/env bash

shopt -s nullglob

find . -type f -name '*.ini' -print0 |
while IFS= read -r -d '' ini; do
    base="${ini%.ini}"
    txt="${base}.txt"

    if [[ -f "$txt" ]]; then
        output="$(dirname "$ini")/patched_$(basename "$ini")"
        echo "Processing: txt='$txt' ini='$ini' -> output='$output'"
        python3 txt_to_ini_transposer.py "$txt" "$ini" "$output"
        echo
    fi
done