# Skills

This directory contains custom Skills for Claude to use when performing specialized tasks.

## What are Skills?

Skills are organized packages of instructions, executable code, and resources that give Claude specialized capabilities for specific tasks. They follow Anthropic's Skills architecture pattern.

For more information about Skills, see:
- [Skills Documentation](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
- [Skills Blog Post](https://www.anthropic.com/news/skills)
- [Engineering Deep Dive](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

## Available Skills

### Retrieving Web Documentation
**Location:** `skills/web-docs-retrieval/`

Fetches web documentation (blog posts, articles) and saves them locally with all images downloaded and proper formatting.

**Capabilities:**
- Fetch web content from URLs
- Download all images referenced in content
- Organize images in structured directories
- Update markdown to reference local image paths
- Generate YAML frontmatter with metadata
- Follow project conventions for file naming

**Usage:**
```
"Retrieve the blog post at https://example.com/article"
```

**Output:**
- Markdown file: `blogs/[article-slug].md`
- Images: `blogs/images/[article-slug]/`
- Index updated: `blogs/README.md`

See `skills/web-docs-retrieval/SKILL.md` for full documentation.

## Skill Structure

Each skill follows this structure:
```
skill-name/
├── SKILL.md           # Skill definition and documentation
├── scripts/           # Executable Python/bash scripts
│   └── *.py
└── resources/         # Templates, data files (optional)
```

## Creating New Skills

To create a new skill:

1. Create a directory with a descriptive name (use gerund form: "doing-something")
2. Add `SKILL.md` with:
   - YAML frontmatter (name, description)
   - Capabilities section
   - Usage examples
   - Input/output format
   - Best practices and limitations
3. Add executable scripts in `scripts/` directory
4. Add any resources needed in `resources/` directory
5. Update this README with the new skill

## Requirements

Skills dependencies are defined in the project's `requirements.txt` file.

For the web-docs-retrieval skill:
- requests
- beautifulsoup4
- html2text
