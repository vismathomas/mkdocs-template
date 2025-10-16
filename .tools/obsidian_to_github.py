"""
Convert Obsidian-flavored Markdown to GitHub-compatible Markdown.
Handles:
- Obsidian callouts -> GitHub callouts
- Cleans up unsupported syntax
"""

import re
from pathlib import Path

def convert_obsidian_to_github(text: str) -> str:
    # Convert Obsidian callouts > [!note] -> GitHub style > [!NOTE]
    text = re.sub(r"^> \[!(\w+)\]", lambda m: f"> [!{m.group(1).upper()}]", text, flags=re.MULTILINE)

    # Normalize footnotes (same syntax, ensure spacing)
    text = re.sub(r"\[\^(\d+)\]:\s*", r"[^\1]: ", text)

    # Ensure Mermaid blocks are preserved correctly
    text = re.sub(r"```mermaid\s*\n", "```mermaid\n", text)

    # Remove Obsidian-only internal links (if present)
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)

    # Strip trailing whitespace
    text = "\n".join(line.rstrip() for line in text.splitlines())

    return text


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Convert Obsidian Markdown to GitHub-compatible format.")
    parser.add_argument("input", type=Path, help="Input .md file")
    parser.add_argument("output", type=Path, help="Output .md file")
    args = parser.parse_args()

    text = args.input.read_text(encoding="utf-8")
    converted = convert_obsidian_to_github(text)
    args.output.write_text(converted, encoding="utf-8")
    print(f"Converted {args.input} → {args.output}")

if __name__ == "__main__":
    main()
