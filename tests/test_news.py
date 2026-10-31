from datetime import datetime, timedelta
from unittest.mock import patch

import pytest

from stockadvisor.tools.news import get_news


@pytest.fixture
def gnews_cls():
    with patch("stockadvisor.tools.news.GNews") as gnews_cls:
        yield gnews_cls


def test_returns_articles_for_symbol(gnews_cls):
    articles = [
        {"title": "Article 1", "url": "https://example.com/1", "published date": "today"},
        {"title": "Article 2", "url": "https://example.com/2", "published date": "yesterday"},
    ]
    gnews_cls.return_value.get_news.return_value = articles

    result = get_news.invoke({"symbol": "PETR3.SA"})

    gnews_cls.return_value.get_news.assert_called_once_with("PETR3.SA")
    assert result == [
        {"title": "Article 1", "published date": "today"},
        {"title": "Article 2", "published date": "yesterday"},
    ]


def test_removes_url_from_every_article(gnews_cls):
    gnews_cls.return_value.get_news.return_value = [
        {"title": "Article", "url": "https://example.com", "description": "desc"},
    ]

    result = get_news.invoke({"symbol": "AAPL"})

    assert "url" not in result[0]
    assert result[0]["description"] == "desc"


def test_handles_articles_without_url(gnews_cls):
    gnews_cls.return_value.get_news.return_value = [
        {"title": "No URL article", "description": "desc"},
    ]

    result = get_news.invoke({"symbol": "AAPL"})

    assert result == [{"title": "No URL article", "description": "desc"}]


def test_queries_articles_from_the_last_30_days(gnews_cls):
    gnews_cls.return_value.get_news.return_value = []

    get_news.invoke({"symbol": "AAPL"})

    start_date = gnews_cls.call_args.kwargs["start_date"]
    assert isinstance(start_date, datetime)
    assert timedelta(days=29, hours=23) < datetime.now() - start_date < timedelta(days=30, hours=1)


def test_returns_empty_list_when_no_articles_found(gnews_cls):
    gnews_cls.return_value.get_news.return_value = []

    result = get_news.invoke({"symbol": "UNKNOWN"})

    assert result == []
