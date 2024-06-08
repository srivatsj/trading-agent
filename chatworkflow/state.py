from typing import TypedDict

class State(TypedDict):
	stock: str
	tweets: list[dict]
	tweet_sentiment: str
	tweet_summary: str