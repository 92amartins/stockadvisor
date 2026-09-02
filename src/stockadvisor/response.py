from pydantic import BaseModel, Field

class Recommendation(BaseModel):
    """A structured recommendation for buying or selling a stock."""
    symbol: str = Field(description="The stock symbol for the recommendation")
    current_price: float = Field(description="The current price of the stock")
    recommendation: str = Field(
        description="The recommendation (Buy|Sell|Hold)"
    )    
    news_sentiment: str = Field(description="The sentiment of the news articles (Positive|Negative|Neutral)")
    stock_info: str = Field(description="A brief summary of the stock information")
    explanation: str = Field(description="A brief explanation for the recommendation")
    warning: str | None = Field(default=None, description="Any warnings or disclaimers related to the recommendation")