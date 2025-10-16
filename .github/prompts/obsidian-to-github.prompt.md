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
````

### Example Output

```markdown
> [!note]
> This section is important.
```

````

---

```markdown
---
description: "Prompt to convert Obsidian Markdown → GitHub Markdown using AI"
tags: [markdown, conversion, obsidian, github, ai]
---

# Prompt: Convert Obsidian Markdown to GitHub Markdown

## Objective
Transform Obsidian-style Markdown into **GitHub-flavored Markdown** that renders cleanly on GitHub Pages and repositories.

---

## Conversion Rules

1. Convert Obsidian callouts:
   - `> [!note]` → `> [!NOTE]`
   - Capitalize all callout types (NOTE, TIP, WARNING, IMPORTANT).

2. Replace internal Obsidian links:
   - `[[Page Name]]` → `Page Name`
   - `[[Page Name|Label]]` → `Label`

3. Keep footnotes intact but normalize spacing:
   - `[ ^1 ]:` → `[ ^1 ]: `

4. Preserve Mermaid diagrams, fenced code blocks, tables, and blockquotes.

5. Remove any Obsidian-only frontmatter or plugin-specific syntax (Dataview, callout folding, etc.).

6. Maintain consistent blank lines and trim trailing spaces.

---

## Instruction to AI
> Convert the Markdown text to be **GitHub-renderable**, applying the above transformations.  
> Output the clean, GitHub-ready Markdown with no additional commentary.

---

### Example Input
```markdown
> [!note]
> This document shows internal logic.

[[System Overview|View System Diagram]]
````

### Example Output

```markdown
> [!NOTE]
> This document shows internal logic.

View System Diagram
```
