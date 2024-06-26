from typing import TypedDict

class State(TypedDict):
	sentence: str
	ticker_symbol: str
	tweets: list[dict]
	tweet_sentiment: str
	tweet_summary: str