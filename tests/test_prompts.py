from stockadvisor.prompts import SYSTEM_PROMPT


def test_prompt_mentions_the_available_tools():
    assert "get_stock_info" in SYSTEM_PROMPT
    assert "get_news" in SYSTEM_PROMPT


def test_prompt_restricts_answers_to_stocks():
    assert "only answer" in SYSTEM_PROMPT.lower()
    assert "decline" in SYSTEM_PROMPT.lower()


def test_prompt_requires_a_concrete_recommendation():
    for option in ("Buy", "Sell", "Hold"):
        assert option in SYSTEM_PROMPT
