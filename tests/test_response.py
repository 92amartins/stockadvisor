import pytest
from pydantic import ValidationError

from stockadvisor.response import Recommendation


def test_accepts_a_complete_recommendation():
    recommendation = Recommendation(
        symbol="PETR3.SA",
        current_price=12.34,
        change_percentage=1.5,
        recommendation="Buy",
        news_sentiment="Positive",
        explanation="Strong results and positive coverage.",
    )

    assert recommendation.symbol == "PETR3.SA"
    assert recommendation.current_price == 12.34
    assert recommendation.recommendation == "Buy"


@pytest.mark.parametrize(
    "missing_field",
    [
        "symbol",
        "current_price",
        "change_percentage",
        "recommendation",
        "news_sentiment",
        "explanation",
    ],
)
def test_rejects_payload_missing_required_field(missing_field):
    payload = {
        "symbol": "PETR3.SA",
        "current_price": 12.34,
        "change_percentage": 1.5,
        "recommendation": "Buy",
        "news_sentiment": "Positive",
        "explanation": "Strong results and positive coverage.",
    }
    del payload[missing_field]

    with pytest.raises(ValidationError):
        Recommendation(**payload)


def test_serializes_to_dict():
    recommendation = Recommendation(
        symbol="AAPL",
        current_price=190.0,
        change_percentage=-2.0,
        recommendation="Sell",
        news_sentiment="Negative",
        explanation="Weak guidance.",
    )

    assert recommendation.model_dump() == {
        "symbol": "AAPL",
        "current_price": 190.0,
        "change_percentage": -2.0,
        "recommendation": "Sell",
        "news_sentiment": "Negative",
        "explanation": "Weak guidance.",
    }
