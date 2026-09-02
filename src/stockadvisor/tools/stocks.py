from langchain.tools import tool
import yfinance as yf

@tool
def get_stock_info(symbol: str, period: str = "30d") -> str:
    """Get the latest stock information for a given symbol."""
    ticker = yf.Ticker(symbol.upper())
    history = ticker.history(period=period)

    if history.empty:
        return f"No stock information found for {symbol}."

    earliest = history.iloc[0]
    latest = history.iloc[-1]
    change = 0.0
    if len(history) > 1:
        previous = earliest["Close"]
        if previous:
            change = (latest["Close"] - previous) / previous * 100

    return f"Stock info for {symbol.upper()}: Price: ${latest['Close']:.2f}, Change (last {period}): {change:+.2f}%"