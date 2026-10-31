from unittest.mock import patch

import pandas as pd
import pytest

from stockadvisor.tools.stocks import get_stock_info


def make_history(closes: list[float]) -> pd.DataFrame:
    return pd.DataFrame({"Close": closes})


@pytest.fixture
def ticker_cls():
    with patch("stockadvisor.tools.stocks.yf.Ticker") as ticker_cls:
        yield ticker_cls


def test_returns_price_and_change_for_period(ticker_cls):
    ticker_cls.return_value.history.return_value = make_history([100.0, 105.0, 110.0])

    result = get_stock_info.invoke({"symbol": "petr3.sa", "period": "1mo"})

    ticker_cls.assert_called_once_with("PETR3.SA")
    ticker_cls.return_value.history.assert_called_once_with(period="1mo")
    assert result == "Stock info for PETR3.SA: Price: $110.00, Change (last 1mo): +10.00%"


def test_uses_default_period_when_omitted(ticker_cls):
    ticker_cls.return_value.history.return_value = make_history([100.0, 90.0])

    get_stock_info.invoke({"symbol": "AAPL"})

    ticker_cls.return_value.history.assert_called_once_with(period="1mo")


def test_single_data_point_reports_zero_change(ticker_cls):
    ticker_cls.return_value.history.return_value = make_history([50.0])

    result = get_stock_info.invoke({"symbol": "AAPL"})

    assert result == "Stock info for AAPL: Price: $50.00, Change (last 1mo): +0.00%"


def test_empty_history_returns_not_found_message(ticker_cls):
    ticker_cls.return_value.history.return_value = pd.DataFrame()

    result = get_stock_info.invoke({"symbol": "UNKNOWN"})

    assert result == "No stock information found for UNKNOWN."
