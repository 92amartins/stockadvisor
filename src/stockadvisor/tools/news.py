from typing import Any
from datetime import datetime, timedelta

from gnews import GNews
from langchain_core.tools import tool
import logging


@tool
def get_news(symbol: str) -> list[dict[str, Any]]:
    """Retrieve the latest Google News articles matching the relevant symbol."""
    start_date = datetime.now() - timedelta(days=30)

    news_client = GNews(
        start_date=start_date
    )	
    logging.warning(f"Retrieving news for symbol: {symbol} since {start_date}")

    return news_client.get_news(symbol)