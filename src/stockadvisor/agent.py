from deepagents import create_deep_agent
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain_ollama import ChatOllama

from stockadvisor.prompts import SYSTEM_PROMPT
from stockadvisor.tools.stocks import get_stock_info
from stockadvisor.tools.news import get_news
from stockadvisor.response import Recommendation
from langchain.agents.structured_output import ToolStrategy

checkpointer = InMemorySaver()

agent = create_deep_agent(
    model="ollama:qwen3.5:4b",
    tools=[get_stock_info, get_news],
    system_prompt=SYSTEM_PROMPT,
    checkpointer=checkpointer,
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What is the current price of PETR3.SA?"}]},
    config={"configurable": {"thread_id": "thread-1"}}
)

structured_model = ChatOllama(model="mistral", temperature=0.0).with_structured_output(Recommendation)
recommendation = structured_model.invoke(result["messages"][-1].content)
print(recommendation)