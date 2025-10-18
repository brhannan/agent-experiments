---
name: Retrieving Web Documentation
description: Fetches web documentation (blog posts, articles) and saves them locally with all images downloaded and proper formatting
---

# Web Documentation Retrieval

This skill retrieves web content and saves it to the local blogs/ directory with all images downloaded, proper YAML frontmatter, and formatted markdown.

## Capabilities

- Fetch web content from URLs (blog posts, articles, documentation)
- Download all images referenced in the content
- Organize images in structured directories (`blogs/images/[article-slug]/`)
- Update markdown to reference local image paths
- Generate YAML frontmatter with metadata (title, url, retrieved date, tags, description)
- Follow project conventions for file naming (kebab-case)
- Handle network errors and missing images gracefully

## When to Use

Use this skill when you need to:
- Retrieve and archive blog posts or articles from the web
- Create complete local copies of web documentation
- Ensure all images are available offline
- Build a local knowledge base from web content

## How to Use

1. **Provide URL**: Give the URL of the web page to retrieve
2. **Skill executes**: Automatically fetches content and downloads images
3. **Files created**: 
   - Markdown file saved to `blogs/[article-slug].md`
   - Images saved to `blogs/images/[article-slug]/`
   - Index updated in `blogs/README.md`

## Input Format

Simply provide the URL:
- "Retrieve the blog post at https://example.com/article"
- "Fetch and save this documentation: [URL]"
- "Archive this article locally: [URL]"

## Output Format

**Markdown file** (`blogs/[article-slug].md`):
```markdown
---
title: Article Title
url: https://original-url.com
retrieved: 2025-10-18
tags: [tag1, tag2, tag3]
description: Brief 1-2 sentence summary
---

# Article Title

Content with local image references...
```

**Images**: Saved to `blogs/images/[article-slug]/image1.png`, etc.

**Index**: Entry added to `blogs/README.md`

## Example Usage

**Input**: "Retrieve the blog post at https://www.anthropic.com/engineering/building-agents"

**Output**:
- File: `blogs/building-agents-with-claude-sdk.md`
- Images: `blogs/images/building-agents-with-claude-sdk/diagram1.png`, etc.
- Index updated with new entry

## Scripts

- `fetch_web_docs.py`: Main script that handles:
  - Web content fetching and HTML-to-markdown conversion
  - Image downloading and local storage
  - Markdown reference updates
  - YAML frontmatter generation
  - Error handling and validation

## Best Practices

1. **Validate URLs** before fetching to ensure they're accessible
2. **Handle missing images** gracefully (log warnings, continue processing)
3. **Use descriptive filenames** derived from article titles
4. **Preserve content structure** (headings, code blocks, lists, tables)
5. **Generate meaningful tags** based on content analysis
6. **Update index atomically** to avoid partial updates on errors

## Configuration

**File naming**: kebab-case (e.g., `building-agents-with-claude-sdk.md`)
**Image storage**: `blogs/images/[article-slug]/`
**Metadata format**: YAML frontmatter
**Working directory**: `/Users/bhannan/code/hello-world-agent`

## Limitations

- Requires internet connectivity to fetch content and images
- Some websites may block automated requests
- Dynamic content (JavaScript-rendered) may not be fully captured
- Image downloads depend on original URLs being accessible
- Very large images may take time to download
- Cannot retrieve content behind authentication/paywalls

## Error Handling

The skill handles:
- Network timeouts and connection errors
- Missing or broken image links
- Invalid URLs
- HTML parsing failures
- File system errors

Errors are logged and processing continues when possible.
