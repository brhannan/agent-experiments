# Agent Development Guidelines

## Core Principles

When working on agent-related tasks in this project:

1. **Follow the agent loop pattern**: gather context -> take action -> verify work -> repeat
2. **Use existing templates**: Use the existing AGENTS.md as a template for new agent instructions
3. **Proper organization**: Store agent configuration files in the appropriate directories
4. **Clear documentation**: Document all agent capabilities and limitations clearly

## Agent Loop Components

### 1. Gather Context
- Use file system structure to organize information
- Implement agentic search when needed
- Consider using subagents for parallel processing
- Use compaction for long-running agents

### 2. Take Action
- Define clear, focused tools for primary actions
- Leverage bash/scripts for flexible operations
- Use code generation for precise, reusable outputs
- Integrate MCPs for external service connections

### 3. Verify Work
- Implement rule-based validation where possible
- Use visual feedback for UI/visual tasks
- Consider LLM-as-judge for subjective evaluations
- Test thoroughly and iterate on failures

## Best Practices

- Start with simple, clear instructions
- Build feedback loops into agent workflows
- Test with representative data and scenarios
- Document failure modes and recovery strategies
- Keep agent capabilities focused and well-defined
