#!/usr/bin/env python3
"""
Refill a template .ini with lines taken from a .txt file.

Use case:
- old version: translated dialogue stored as a flat .txt
- new version: same dialogue stored in grouped .ini sections

This script preserves the template .ini structure and replaces each
`l_<n> = "..."` entry in order with the next non-empty line from the .txt.

Usage:
    python txt_to_ini_transposer.py translated.txt template.ini output.ini

Notes:
- The template .ini controls the exact output structure.
- Blank lines in the .txt are ignored by default.
- Literal double quotes in the .txt are converted to INI_QUOTS, because the
  sample .ini files encode quotes that way.
- If the template line starts with a BOM character (U+FEFF), it is preserved.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from codecs import BOM_UTF8


L_ENTRY_RE = re.compile(r'^(\s*l_\d+\s*=\s*")(.*)("(\s*)?)$')


def read_text_preserve_newlines(path: Path, encoding: str) -> str:
    with path.open("r", encoding=encoding, newline="") as f:
        return f.read()


def file_has_utf8_bom(path: Path) -> bool:
    return path.read_bytes().startswith(BOM_UTF8)


def read_txt_lines(path: Path, keep_empty: bool = False) -> list[str]:
    text = read_text_preserve_newlines(path, encoding="utf-8-sig")
    lines = text.splitlines()

    if keep_empty:
        return lines

    return [line for line in lines if line.strip() != ""]


def encode_for_ini(line: str) -> str:
    """
    Convert a txt dialogue line into the format expected inside the ini value.
    """
    return line.replace('"', 'INI_QUOTS')


def extract_template_entries(template_lines: list[str]) -> list[tuple[int, str]]:
    """
    Return a list of (line_index, current_value) for all l_<n> entries in order.
    """
    entries: list[tuple[int, str]] = []

    for idx, raw_line in enumerate(template_lines):
        line = raw_line.rstrip("\r\n")
        match = L_ENTRY_RE.match(line)
        if match:
            current_value = match.group(2)
            entries.append((idx, current_value))

    return entries


def replace_template_entries(
    template_lines: list[str],
    translated_lines: list[str],
) -> list[str]:
    entries = extract_template_entries(template_lines)

    if len(entries) != len(translated_lines):
        raise ValueError(
            f"Line count mismatch: template expects {len(entries)} dialogue lines, "
            f"but txt provides {len(translated_lines)} non-empty lines."
        )

    result = template_lines[:]

    for translated, (line_idx, current_value) in zip(translated_lines, entries):
        original_line = result[line_idx]
        newline = ""
        if original_line.endswith("\r\n"):
            newline = "\r\n"
        elif original_line.endswith("\n"):
            newline = "\n"

        stripped = original_line.rstrip("\r\n")
        match = L_ENTRY_RE.match(stripped)
        if not match:
            raise ValueError(f"Internal parsing error at template line {line_idx + 1}")

        prefix, _old_value, suffix = match.group(1), match.group(2), match.group(3)

        new_value = encode_for_ini(translated)

        # Preserve an initial BOM if the template stored one inside the first value.
        if current_value.startswith("\ufeff") and not new_value.startswith("\ufeff"):
            new_value = "\ufeff" + new_value

        result[line_idx] = f"{prefix}{new_value}{suffix}{newline}"

    return result


def validate_counts(template_text: str) -> None:
    """
    Basic sanity check: total of `count = N` should match the number of l_<n> entries.
    """
    count_values: list[int] = []
    l_entry_count = 0

    for line in template_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("count"):
            match = re.fullmatch(r'count\s*=\s*(\d+)', stripped)
            if match:
                count_values.append(int(match.group(1)))
        elif re.match(r'^l_\d+\s*=\s*".*"$', stripped):
            l_entry_count += 1

    if count_values and sum(count_values) != l_entry_count:
        raise ValueError(
            "Template ini looks inconsistent: sum(count) does not match the number "
            "of l_<n> entries."
        )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Fill a template .ini with dialogue lines from a .txt file."
    )
    parser.add_argument("txt", type=Path, help="Translated .txt file")
    parser.add_argument("template_ini", type=Path, help="Template .ini file")
    parser.add_argument("output_ini", type=Path, help="Output .ini file to create")
    parser.add_argument(
        "--keep-empty-lines",
        action="store_true",
        help="Do not ignore empty lines in the txt file",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if not args.txt.is_file():
        print(f"Error: txt file not found: {args.txt}", file=sys.stderr)
        return 1

    if not args.template_ini.is_file():
        print(f"Error: template ini file not found: {args.template_ini}", file=sys.stderr)
        return 1

    try:
        translated_lines = read_txt_lines(args.txt, keep_empty=args.keep_empty_lines)

        template_has_bom = file_has_utf8_bom(args.template_ini)
        template_encoding = "utf-8-sig" if template_has_bom else "utf-8"

        template_text = read_text_preserve_newlines(args.template_ini, encoding=template_encoding)
        validate_counts(template_text)
        template_lines = template_text.splitlines(keepends=True)

        output_lines = replace_template_entries(template_lines, translated_lines)

        args.output_ini.parent.mkdir(parents=True, exist_ok=True)
        output_encoding = "utf-8-sig" if template_has_bom else "utf-8"
        with args.output_ini.open("w", encoding=output_encoding, newline="") as f:
            f.write("".join(output_lines))

    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"Created: {args.output_ini}")
    print(f"Replaced {len(translated_lines)} dialogue lines.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
