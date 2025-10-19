# Web Documentation Retrieval Rules

## Process

When retrieving web documentation for the blogs/ directory:

1. **Use the web-docs-retrieval skill** (fetch_web_docs.py script) to retrieve content from the provided URL
   - The script automatically handles HTML-to-markdown conversion
   - Downloads all images locally
   - Handles Next.js and other image proxy URLs
2. **Format with YAML frontmatter** including:
   - title: Article title
   - url: Original URL
   - retrieved: Date in YYYY-MM-DD format
   - tags: Array of relevant tags (e.g., [agents, claude, sdk, tool-use])
   - description: Brief 1-2 sentence summary of the content
3. **Save to ./blogs/ directory** with descriptive kebab-case filename (e.g., building-agents-with-claude-sdk.md)
4. **Images are automatically**:
   - Downloaded to ./blogs/images/[article-slug]/ directory
   - Referenced with local paths in the markdown
   - Extracted from proxy URLs (e.g., Next.js image optimization URLs)
5. **Maintain original structure**:
   - Keep all headings, code blocks, lists, and formatting
   - Preserve code examples with proper syntax highlighting
   - Clean up any HTML artifacts that remain after conversion
6. **Update blogs/README.md** index file after adding new content

## File Naming Convention

- Use kebab-case (lowercase with hyphens)
- Make filenames descriptive of the content
- Use .md extension for markdown files
- Example: `building-agents-with-claude-sdk.md`

## Image Handling

The web-docs-retrieval skill automatically handles various image URL formats:

- **Direct image URLs**: Standard `<img src="https://example.com/image.png">`
- **Next.js proxy URLs**: `/_next/image?url=https%3A%2F%2Fcdn.example.com%2Fimage.png&w=3840&q=75`
- **Relative URLs**: Converted to absolute URLs before downloading
- **CDN URLs**: Extracted from proxy/optimization wrappers

All images are:
1. Downloaded to `blogs/images/[article-slug]/` 
2. Saved with their original filename (or hash-based filename if needed)
3. Referenced in markdown with local paths like `images/[article-slug]/image.png`

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

[Content with local image references...]
