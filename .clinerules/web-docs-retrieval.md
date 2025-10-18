# Web Documentation Retrieval Rules

## Process

When retrieving web documentation for the blogs/ directory:

1. **Use web_fetch tool** to retrieve content from the provided URL
2. **Format with YAML frontmatter** including:
   - title: Article title
   - url: Original URL
   - retrieved: Date in YYYY-MM-DD format
   - tags: Array of relevant tags (e.g., [agents, claude, sdk, tool-use])
   - description: Brief 1-2 sentence summary of the content
3. **Save to ./blogs/ directory** with descriptive kebab-case filename (e.g., building-agents-with-claude-sdk.md)
4. **Maintain original structure**:
   - Keep all headings, code blocks, lists, and formatting
   - Preserve code examples with proper syntax highlighting
   - Clean up any HTML artifacts that remain after conversion
5. **Update blogs/README.md** index file after adding new content

## File Naming Convention

- Use kebab-case (lowercase with hyphens)
- Make filenames descriptive of the content
- Use .md extension for markdown files
- Example: `building-agents-with-claude-sdk.md`

## Standard Metadata Template

```markdown
---
title: [Article Title]
url: [Original URL]
retrieved: [YYYY-MM-DD]
tags: [tag1, tag2, tag3]
description: [Brief 1-2 sentence summary]
---

# [Article Title]

[Content here...]
