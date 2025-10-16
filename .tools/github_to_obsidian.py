"""
Convert GitHub-flavored Markdown to Obsidian-compatible Markdown.
Handles:
- GitHub callouts -> Obsidian callouts
- Normalizes footnotes and Mermaid formatting
"""

import re
from pathlib import Path

def convert_github_to_obsidian(text: str) -> str:
    # Convert GitHub callouts > [!NOTE] -> Obsidian style > [!note]
    text = re.sub(r"^> \[!(\w+)\]", lambda m: f"> [!{m.group(1).lower()}]", text, flags=re.MULTILINE)

    # Normalize footnote markers spacing
    text = re.sub(r"\[\^(\d+)\]:\s*", r"[^\1]: ", text)

    # Fix mermaid syntax if missing language marker
    text = re.sub(r"```mermaid\s*\n", "```mermaid\n", text)

    # Optional: strip trailing whitespace
    text = "\n".join(line.rstrip() for line in text.splitlines())

    return text


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Convert GitHub Markdown to Obsidian-compatible format.")
    parser.add_argument("input", type=Path, help="Input .md file")
    parser.add_argument("output", type=Path, help="Output .md file")
    args = parser.parse_args()

    text = args.input.read_text(encoding="utf-8")
    converted = convert_github_to_obsidian(text)
    args.output.write_text(converted, encoding="utf-8")
    print(f"Converted {args.input} → {args.output}")

if __name__ == "__main__":
    main()
