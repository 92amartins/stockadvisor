from pydantic import BaseModel, Field

class Recommendation(BaseModel):
    """A structured recommendation for buying or selling a stock."""
    symbol: str = Field(description="The stock symbol for the recommendation")
    current_price: float = Field(description="The current price of the stock")
    change_percentage: float = Field(description="The percentage change in the stock price over the last 30 days")
    recommendation: str = Field(
        description="The recommendation (Buy|Sell|Hold)"
    )    
    news_sentiment: str = Field(description="The sentiment of the news articles (Positive|Negative|Neutral)")
    explanation: str = Field(description="A brief explanation for the recommendation")