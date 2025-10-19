# Web Research Agent

An autonomous agent that performs web research by browsing multiple sources, synthesizing information, and creating comprehensive research reports with citations.

## What is this?

This project demonstrates a **sequential workflow with centralized planning** combined with **browser automation** where a single Claude agent:
1. **Plans research strategy** (orchestrator role) - breaks down the research question into searchable topics
2. **Gathers information** (worker role) - visits multiple web sources one by one
3. **Synthesizes findings** - combines information from all sources
4. **Verifies quality** - checks citations and validates claims
5. **Iterates** - performs follow-up searches if needed

**Note on Pattern**: While this uses orchestrator-like planning, it's implemented as a single agent executing tasks sequentially. A true orchestrator-workers pattern would use separate worker agents running in parallel (see "Extending to True Orchestrator-Workers" below).

## Key Concepts Demonstrated

### 1. **Browser Automation**
- Uses the `browser_action` tool to navigate websites
- Takes screenshots to verify page content
- Extracts information from live web pages
- Handles dynamic content and navigation

### 2. **Sequential Workflow with Planning**
- Single agent acts as both orchestrator and worker
- Plans the overall research strategy upfront
- Executes each sub-task sequentially (source by source)
- Synthesizes results after gathering all information
- **Learning path**: This simpler pattern helps you understand the orchestration concepts before building true multi-agent systems

### 3. **Information Quality**
- Tracks sources and citations
- Cross-references claims across sources
- Identifies conflicting information
- Maintains research provenance

### 4. **Iterative Research**
- Can perform follow-up searches based on findings
- Refines search strategy based on results
- Fills knowledge gaps discovered during synthesis

## Project Structure

```
agent-web-researcher/
├── README.md              # This file (for humans)
├── AGENTS.md              # Instructions for the AI agent
├── queries/               # Input research questions
│   └── sample-query.txt   # Example research question
└── output/                # Generated research outputs
    ├── research-report.md # Main synthesized report
    ├── sources.json       # Structured source metadata
    └── screenshots/       # Page screenshots from research
```

## How to Use It

### Prerequisites

No special dependencies needed - the agent uses Claude's built-in browser_action tool available in Claude Code (Cline).

### Option 1: Use the Sample Query (Recommended for First Try)

The project includes a pre-written research question about LLM agent developments.

**Step 1**: Open this project in your IDE with Claude Code installed

**Step 2**: Prompt Claude with:
```
Research the question in queries/sample-query.txt following AGENTS.md
```

**Step 3**: Watch the agent work autonomously:
- It will read the query file
- Plan which sources to visit
- Launch browser for each source (you'll see screenshots)
- Extract and synthesize information
- Generate the research report

**Step 4**: Review the outputs in the `output/` directory:
```bash
# Read the research report
cat output/research-report.md

# View source metadata  
cat output/sources.json

# Browse screenshots taken during research
open output/screenshots/
```

### Option 2: Provide Your Own Research Question

You can research any topic by directly prompting Claude.

**Basic prompt:**
```
Research [your question] following AGENTS.md. Search at least 3 sources.
```

**Better prompt with specifics:**
```
Research the latest developments in LLM agents from the past 3 months.
Search Anthropic blog, Simon Willison's blog, and ArXiv papers.
Create a comparison table of different agent patterns.
```

**Advanced prompt with constraints:**
```
Research best practices for building production-ready AI agents.
Focus on:
- Security considerations
- Deployment patterns  
- Tool design principles
Sources: Anthropic blog, GitHub engineering blogs, LangChain blog
Time frame: Last 6 months
Format: Executive summary + detailed sections + comparison table
```

### Option 3: Create a Query File

For complex research questions, create a text file in the `queries/` directory:

**Step 1**: Create your query file
```bash
# Create a new query file
cat > agent-web-researcher/queries/my-research.txt << 'EOF'
Research Question: [Your question here]

Context: [Background and specific areas of interest]

Sources to Consult:
1. [Source 1 URL]
2. [Source 2 URL]
3. [Source 3 URL]

Output Requirements:
- [Specific format or focus areas]

Time Frame: [Date range if relevant]
EOF
```

**Step 2**: Run the agent
```
Research the question in queries/my-research.txt following AGENTS.md
```

### What to Expect During Execution

The agent will work autonomously through these phases:

**1. Planning (30 seconds - 1 minute)**
- Reads and analyzes the research question
- Identifies key topics and sources to search
- Plans the research strategy

**2. Information Gathering (3-7 minutes)**
For each source:
- Launches browser at the target URL
- Takes screenshots (you'll see these in the output)
- Scrolls and navigates as needed
- Extracts relevant information
- Closes browser before moving to next source

**3. Synthesis (1-2 minutes)**
- Organizes findings by themes
- Cross-references information
- Identifies patterns and contradictions
- Maintains citation tracking

**4. Report Generation (1 minute)**
- Creates structured markdown report
- Generates sources.json metadata
- Ensures all claims are cited

**Total time**: Typically 5-10 minutes depending on number of sources and complexity

### Example Research Questions

Here are some good research questions to try:

**AI/ML Topics:**
```
Research the latest developments in LLM agents from the past 3 months.
Search Anthropic blog, Simon Willison's blog, and ArXiv papers.

Compare different approaches to tool use in LLM frameworks.
Focus on LangChain, Anthropic SDK, and other major frameworks.

What are the emerging patterns in production agent deployments?
Include security and reliability considerations.
```

**Technical Topics:**
```
Research best practices for API design in 2025.
Search GitHub engineering blogs, Martin Fowler's blog, and API design communities.

What are the current trends in frontend frameworks?
Compare React, Vue, and Svelte approaches. Focus on developer experience.
```

**Industry Research:**
```
Research how companies are using AI coding assistants in production.
Find case studies and implementation patterns.

What are the key considerations for building developer tools?
Focus on UX, performance, and integration patterns.
```

### Viewing Results

After completion, explore the outputs:

**Research Report:**
```bash
# View in terminal
cat output/research-report.md

# Or open in your editor
code output/research-report.md
```

**Source Metadata:**
```bash
# View structured data about sources
cat output/sources.json

# Pretty print with jq
cat output/sources.json | jq
```

**Screenshots:**
```bash
# Browse all screenshots
open output/screenshots/

# List what was captured
ls -lh output/screenshots/
```

### Tips for Best Results

**✓ Be specific** - "Latest agent patterns in production" > "Tell me about agents"

**✓ Specify sources** - Name 3-5 authoritative sources you want checked

**✓ Set constraints** - Time frame, focus areas, output format

**✓ Request comparisons** - "Compare X vs Y" often yields great insights

**✓ Use YOLO mode safely** - This project is designed for safe autonomous operation

**✗ Avoid vague prompts** - "Research AI" is too broad

**✗ Don't over-constrain** - Let the agent adapt its strategy as needed

## Agent Workflow

### Phase 1: Research Planning
The agent analyzes the research question and creates a search strategy:
- Identifies key topics to investigate
- Determines authoritative sources to consult
- Plans the sequence of searches

### Phase 2: Information Gathering
For each source, the agent:
- Launches browser and navigates to the source
- Takes screenshots to verify page content
- Extracts relevant information
- Records citations and metadata
- Closes browser

### Phase 3: Synthesis
The agent combines findings:
- Identifies common themes across sources
- Notes conflicting information
- Organizes information by topic
- Maintains source attribution

### Phase 4: Quality Check
The agent verifies:
- All claims are cited
- Sources are authoritative
- Information is recent (when relevant)
- No knowledge gaps remain

### Phase 5: Report Generation
Creates final output:
- Structured markdown report
- Executive summary
- Detailed findings by topic
- Full source list with URLs
- Timestamps and metadata

## Advanced Features

### Multiple Search Strategies

The agent can adapt its search strategy:
- **Broad exploration**: Survey many sources quickly
- **Deep dive**: Thoroughly analyze fewer sources
- **Comparative**: Side-by-side comparison of different perspectives
- **Timeline**: Track how information evolved over time

### Smart Screenshot Management

Screenshots serve multiple purposes:
- Visual verification of page content
- Fallback if text extraction fails
- Evidence for fact-checking
- Debug aid for troubleshooting

### Source Quality Assessment

The agent evaluates sources based on:
- Domain authority (e.g., official blogs, academic papers)
- Publication date (freshness)
- Author credentials
- Citation/reference quality
- Cross-validation with other sources

## Extending This Project

### Easy Extensions
- Add more sources to search (Reddit, GitHub, Stack Overflow)
- Request specific output formats (table, timeline, mindmap)
- Filter by date range (last week, month, year)

### Medium Extensions
- Add automatic fact-checking against multiple sources
- Generate comparison tables for competitive analysis
- Create visual diagrams from findings (with Mermaid/Graphviz)
- Export to different formats (PDF, HTML, Notion)

### Advanced Extensions
- Implement recursive research (agent identifies gaps and researches them)
- Build a knowledge graph from research findings
- Create a research dashboard with metrics
- Add sentiment analysis across sources
- Implement automated follow-up questions

### Extending to True Orchestrator-Workers Pattern

To implement a true orchestrator-workers pattern, you would need to modify the agent to:

**Current (Sequential)**: Single agent does everything in sequence
```
Agent: Plan → Source 1 → Source 2 → Source 3 → Synthesize
```

**True Orchestrator-Workers**: Separate orchestrator and worker agents
```
Orchestrator: Analyzes task → Creates worker instructions
  ↓
Worker 1: Researches Source 1 → Reports findings
Worker 2: Researches Source 2 → Reports findings  
Worker 3: Researches Source 3 → Reports findings
  ↓
Orchestrator: Synthesizes all worker reports → Creates final report
```

**Implementation approaches**:
1. **Using Python Agent SDK**: Create separate agent instances for orchestrator and workers, with message passing between them
2. **Using Sub-agents in AGENTS.md**: Have the main agent create separate AGENTS.md files for workers and coordinate their execution
3. **Using MCP Multi-Agent Tools**: Leverage MCP servers that provide multi-agent coordination capabilities

**When to use true orchestrator-workers**:
- When you need actual parallel execution for speed
- When workers need different specialized prompts/tools
- When the task naturally divides into independent sub-tasks
- When you're building production systems at scale

**Why this project uses sequential workflow instead**:
- Simpler to understand and debug
- Browser automation is inherently sequential (can't run multiple browsers in parallel with current tools)
- Perfect for learning the orchestration concepts
- Sufficient for most research tasks
- Can be extended to parallel when needed

## Tips for Effective Research

### 1. Be Specific in Your Questions
**Less effective:**
- "Tell me about AI"

**More effective:**
- "What are the key architectural differences between ReAct and Reflexion agent frameworks?"

### 2. Specify Your Sources
**Generic:**
- "Research this topic"

**Better:**
- "Research this topic using Anthropic blog, ArXiv, and recent Hacker News discussions"

### 3. Set Context and Constraints
**Basic:**
- "What's new in agents?"

**Better:**
- "What agent patterns have emerged in production systems in the last 6 months? Focus on enterprise deployments."

### 4. Request Specific Output Formats
- "Create a comparison table of approaches"
- "Generate a timeline of developments"
- "List pros and cons for each approach"

## Learning Resources

This project builds on concepts from:
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) - Anthropic's guide on agent patterns
- [Computer Use](https://docs.anthropic.com/en/docs/build-with-claude/computer-use) - Documentation on browser automation with Claude
- [Tool Use](https://docs.anthropic.com/en/docs/build-with-claude/tool-use) - How Claude interacts with tools

## Troubleshooting

### Browser won't launch
- Check that browser_action tool is available in your Claude Code version
- Try with a simpler URL first (e.g., example.com)
- Review the error message for specific issues

### Can't find information on page
- Agent might need to scroll down (use scroll_down action)
- Page might require interaction (clicking, typing)
- Try a different source URL

### Research takes too long
- Reduce the number of sources
- Use more specific search queries
- Set a time limit in your prompt

### Low-quality synthesis
- Request more specific output format
- Ask agent to cite all claims
- Specify minimum number of sources to check

## Comparison to CSV Analyzer

| Aspect | CSV Analyzer | Web Research Agent |
|--------|--------------|-------------------|
| **Complexity** | Beginner | Intermediate |
| **New Tools** | File operations | Browser automation |
| **Pattern** | Linear workflow | Orchestrator-workers |
| **Output** | Visualizations + report | Research report + citations |
| **Iteration** | Error correction | Strategic refinement |
| **Autonomy** | Structured steps | Self-directed search |
| **Learning Focus** | Basic agent loop | Advanced patterns + tools |

## What's Next?

After mastering this project:
1. Try the **Code Review Bot** (evaluator-optimizer pattern)
2. Build an **API Integration Generator** (full autonomy)
3. Create a **Multi-Agent Research System** (complex coordination)
4. Experiment with **Custom Tools via MCP** (extensibility)

## Success Criteria

Your agent is working well when it:
- ✓ Successfully navigates to all specified sources
- ✓ Extracts relevant information from each source
- ✓ Cites all claims with specific URLs
- ✓ Synthesizes findings into coherent themes
- ✓ Identifies and notes conflicting information
- ✓ Generates a well-structured, readable report
- ✓ Completes research within reasonable time (5-10 minutes)

## License

MIT - Use this as a template for your own research agents!
