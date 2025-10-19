"""
A very small agent.
"""

import os
from anthropic import Anthropic


client = Anthropic()


def ask_claude(
        prompt: str, 
        system_prompt: str = "", 
        max_tokens: int = 1024
        ) -> str:
    """
    Make a single call to Claude.
    """
    messages = [{"role": "user", "content": prompt}]
    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=max_tokens,
        system=system_prompt,
        messages=messages,
        temperature=0.3
    )
    return response.content[0].text


def main():
    question = "What is a good wooden boatbuilding youtube channel?"
    answer = ask_claude(
        prompt=question,
        system_prompt="You are a helpful assistant who provides nice, consistent answers."
    )
    print(answer)


if __name__ == "__main__":
    main()