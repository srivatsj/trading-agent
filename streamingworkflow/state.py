from typing import TypedDict

class State(TypedDict):
	tweets: list[dict]
	tweet_sentiment: str
	tweet_summary: str