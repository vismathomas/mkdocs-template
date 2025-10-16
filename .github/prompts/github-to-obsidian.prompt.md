---
description: "Prompt to convert GitHub Markdown → Obsidian Markdown using AI"
tags: [markdown, conversion, github, obsidian, ai]
---

# Prompt: Convert GitHub Markdown to Obsidian Markdown

## Objective
Transform GitHub-flavored Markdown into **Obsidian-compatible Markdown**, keeping all structure and readability while ensuring compatibility inside **Obsidian’s Live Preview** and **Reading Mode**.

---

## Conversion Rules

1. Convert GitHub callouts:
   - `> [!NOTE]` → `> [!note]`
   - All callout types must be lowercased.

2. Keep footnotes intact but normalize spacing:
   - `[ ^1 ]:` → `[ ^1 ]: ` (ensure single space)

3. Preserve Mermaid blocks, code fences, tables, headings, and blockquotes as-is.

4. Remove or simplify unsupported inline HTML (e.g., `<details>`, `<summary>`).

5. Do **not** add new formatting, emojis, or commentary — perform a pure syntax transformation.

6. Remove trailing whitespace and normalize blank lines to one between blocks.

---

## Instruction to AI
> Reformat the provided Markdown text so it renders correctly in **Obsidian**, using the above rules.  
> Output the full converted Markdown only — no explanations or commentary.

---

### Example Input
```markdown
> [!NOTE]
> This section is important.
