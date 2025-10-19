# CSV Data Analyzer Agent

A "Hello World" project for learning how to build agent loops with Claude Code (or Cline CLI). This project demonstrates the core concepts from the Anthropic and Simon Willison blog posts on building effective coding agents.

## What is this?

This is a simple but complete example of an **agentic loop** where Claude:
1. **Gathers context** - reads CSV files and understands their structure
2. **Takes action** - generates Python code to analyze data and create visualizations
3. **Verifies work** - runs the code and checks outputs
4. **Iterates** - fixes errors and improves results

## Project Structure

```
hello-world-agent/
├── AGENTS.md              # Instructions for the AI agent
├── README.md              # This file (for humans)
├── requirements.txt       # Python dependencies
├── data/                  # Input CSV files
│   └── sales_data.csv     # Sample sales dataset
├── output/                # Generated analysis (created by agent)
│   ├── analysis.py        # Python script (generated)
│   ├── report.md          # Findings report (generated)
│   └── *.png              # Visualizations (generated)
├── skills/                # Custom Skills for Claude
│   └── web-docs-retrieval/  # Skill for fetching web docs with images
├── blogs/                 # Archived web documentation
│   └── images/            # Downloaded images from blog posts
└── workflows/             # Workflow templates (deprecated)
```

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Agent

Open this project in your IDE with Claude Code or Cline CLI installed, then prompt:

```
Analyze the CSV file in the data/ directory following the instructions in AGENTS.md
```

Claude will:
- Read `AGENTS.md` to understand its task
- Explore the CSV file
- Generate Python code to analyze it
- Create visualizations and a report
- Iterate until everything works

### 3. View Results

After the agent completes, check the `output/` directory:

```bash
# View the report
cat output/report.md

# View generated visualizations
open output/
```

## Key Concepts Demonstrated

### 1. **Agent Instructions (AGENTS.md)**
- Clear task definition
- Available tools and packages
- Step-by-step process
- Success criteria
- This is the "playbook" for the agent

### 2. **Safe Environment**
- No dangerous commands (no `rm -rf`, no deployments)
- Local file operations only
- Easy to reset (just delete `output/`)
- Safe to run in YOLO mode

### 3. **Feedback Loop**
- Agent generates code
- Runs it to see results
- Checks for errors
- Iterates to fix issues
- Self-verifies success

### 4. **Code Generation**
Rather than using pre-built tools, the agent writes Python code on the fly. This is more flexible than fixed APIs and demonstrates Claude's strength at code generation.

## Extending This Project

Once you understand the basics, try:

### Easy Extensions
- Add more CSV files to analyze
- Request different types of visualizations
- Ask for specific insights (e.g., "find the top 3 products by revenue")

### Medium Extensions
- Add data cleaning requirements to AGENTS.md
- Request comparative analysis across multiple CSV files
- Generate PowerPoint presentations with findings

### Advanced Extensions
- Connect to live APIs for data
- Add statistical testing (t-tests, correlations)
- Create an interactive dashboard with Plotly
- Set up scheduled analysis runs

## Learning Resources

This project is based on concepts from:
- [Designing agentic loops](https://simonwillison.net/2025/Feb/10/designing-agentic-loops/) by Simon Willison
- [Building agents with the Claude Agent SDK](https://www.anthropic.com/news/building-agents-with-claude-code-sdk) by Anthropic

## Tips for Success

1. **Be specific in prompts**: Instead of "analyze this", try "create a bar chart showing total sales by category"

2. **Let the agent iterate**: Don't interrupt - let it try, fail, and fix its own errors

3. **Check AGENTS.md first**: Make sure the instructions are clear before running

4. **Start simple**: Get basic analysis working before requesting complex features

5. **Use YOLO mode safely**: This project is designed to be safe, but always review what commands will run

## Troubleshooting

**Agent doesn't start**
- Make sure AGENTS.md exists and is readable
- Try a more explicit prompt

**Python errors**
- The agent should fix these automatically
- If stuck, you can manually run: `python output/analysis.py`

**Missing visualizations**
- Check that dependencies installed: `pip list | grep matplotlib`
- Agent should detect and retry

**No output directory**
- The agent will create it automatically
- Or create manually: `mkdir output`

## What's Next?

Now that you have a working agent loop, you can:
1. Try the other project ideas from the plan (code quality, screenshots, research)
2. Adapt this pattern to your own workflows
3. Experiment with MCP servers for external API access
4. Read more about [Safe YOLO mode](https://docs.anthropic.com/en/docs/agents/safe-yolo-mode)

## License

MIT - Feel free to use this as a template for your own agent projects!
