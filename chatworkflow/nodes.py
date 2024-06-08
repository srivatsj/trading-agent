import os
import time

class Nodes():
    def __init__(self):
        self = ""

    def extract_stock_from_input(self, state):
        print("## Extract stock from input")

        # Use Stock extractor agent to get stock symbol
        return {
          **state,
          "stock": ""
        }
    
    def get_latest_tweets(self, state):
        print("## Checking for new tweets for ", state["stock"])

        # Use CSV agent to get latest tweets about Apple or some harcoded stock
        return {
          **state,
          "tweets": ""
        }

    def get_tweet_sentiment(self, state):
        print("## Get Tweet sentiment")

        # Use Sentiment agent to get sentiment
        return {
          **state,
          "tweet_sentiment": ""
        }

    def get_tweet_summary(self, state):
        print("## Get Tweet summary")

        # Use Summary agent to summarize
        return {
          **state,
          "tweet_summary": ""
        }