from deepagents import create_deep_agent
from langgraph.checkpoint.memory import InMemorySaver

from stockadvisor.prompts import SYSTEM_PROMPT
from stockadvisor.tools.stocks import get_stock_info
from stockadvisor.tools.news import get_news

checkpointer = InMemorySaver()

agent = create_deep_agent(
    model="ollama:qwen3.5:4b",
    tools=[get_stock_info, get_news],
    system_prompt=SYSTEM_PROMPT,
    checkpointer=checkpointer,
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What is the capital of the United States?"}]},
    config={"configurable": {"thread_id": "thread-1"}}
)

print(result["messages"][-1].content)