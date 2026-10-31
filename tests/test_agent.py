from unittest.mock import patch

from stockadvisor import agent as agent_module
from stockadvisor.prompts import SYSTEM_PROMPT
from stockadvisor.tools.news import get_news
from stockadvisor.tools.stocks import get_stock_info


def test_build_agent_uses_model_tools_and_system_prompt():
    with patch("stockadvisor.agent.create_deep_agent") as create_deep_agent:
        result = agent_module.build_agent()

    create_deep_agent.assert_called_once_with(
        model="ollama:qwen3.5:9b",
        tools=[get_stock_info, get_news],
        system_prompt=SYSTEM_PROMPT,
    )
    assert result is create_deep_agent.return_value


def test_module_exposes_an_agent_for_langgraph():
    assert agent_module.agent is not None
