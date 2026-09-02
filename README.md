# StockAdvisor

Langchain agent for analyzing stock data and generating simple investment insights.

## Features

- System Prompt
- Structured Output
- Tools (i.e. External Data (Stock) and News)

## Tools

- Gather stock data from `yfinance`
- Collect news from Google News (`gnews` package)

## Quick start

1. Install the project dependencies:
```bash
uv sync
```

2. Run the demo:
```bash
uv run python .\src\stockadvisor\agent.py

symbol='PETR3.SA' current_price=12.34 recommendation='Buy' news_sentiment='Positive' stock_info='Current price: $12.34' explanation="The currentprice of PETR3.SA is $12.34. The latest news articles suggest a positive outlook for the company's future performance, with potential growth opportunities in the pipeline. Based on this analysis, I recommend buying PETR3.SA as it appears to be a promising investment opportunity with good growth potential. However, it's important to do additional research and consider your personal investment goals and risk tolerance before making a decision." warning=None
```