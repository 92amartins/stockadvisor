from deepagents import create_deep_agent

from stockadvisor.prompts import SYSTEM_PROMPT
from stockadvisor.tools.stocks import get_stock_info
from stockadvisor.tools.news import get_news


def build_agent():
    """Create the stock advisor agent."""
    return create_deep_agent(
        model="ollama:qwen3.5:9b",
        tools=[get_stock_info, get_news],
        system_prompt=SYSTEM_PROMPT,
    )


agent = build_agent()


if __name__ == "__main__":
    result = agent.invoke(
        {"messages": [{"role": "user", "content": "What is the capital of the United States?"}]}
    )

    print(result["messages"][-1].content)
