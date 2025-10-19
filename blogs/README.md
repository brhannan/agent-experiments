# Blog Resources

This directory contains web documentation and blog posts related to building agents, retrieved and formatted for use as LLM context.

## Contents

### Agent Development

#### [Building agents with the Claude Agent SDK](building-agents-with-claude-sdk.md)
- **URL**: https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk
- **Retrieved**: 2025-10-18
- **Tags**: agents, claude, sdk, agentic-loops, tool-use, code-generation, mcp
- **Description**: Comprehensive guide on building powerful agents using the Claude Agent SDK, covering the agent feedback loop (gather context -> take action -> verify work -> repeat), best practices, and practical examples including email agents, finance agents, and research agents.

#### [How we built our multi-agent research system](how-we-built-our-multi-agent-research-system.md)
- **URL**: https://www.anthropic.com/engineering/multi-agent-research-system
- **Retrieved**: 2025-10-18
- **Tags**: multi-agent, research, claude, engineering, agents, architecture, agentic-systems, prompt-engineering, evaluation
- **Description**: Deep dive into the engineering challenges and lessons learned from building Anthropic's multi-agent research system, covering architecture design, prompt engineering strategies, evaluation methods, and production reliability practices.

#### [Embracing the parallel coding agent lifestyle](parallel-coding-agents.md)
- **URL**: https://simonwillison.net/2025/Oct/5/parallel-coding-agents/
- **Retrieved**: 2025-10-18
- **Tags**: coding-agents, parallel-agents, ai-assisted-programming, claude-code, workflow, llms, software-development
- **Description**: Simon Willison shares patterns for running multiple coding agents in parallel, including research tasks, system understanding, maintenance work, and carefully directed development, with practical tips on tools and workflows.

## Usage

These markdown files can be used as context for LLM prompting and agent development. Each file includes:

- Original URL for reference
- Retrieval date for freshness tracking
- Relevant tags for categorization
- Complete article content in clean markdown format

## Adding New Content

To add new blog posts or documentation:

1. Use the workflow defined in `.cline/workflows/retrieve-web-docs.md`
2. Follow the formatting guidelines in `.clinerules`
3. Update this index file with the new entry

## Organization

Files are named using kebab-case based on their content topic, making them easy to identify and reference.
