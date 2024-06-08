import os
import time
from csv_agent import *
from sentiment_agent import *
from stock_extractor_agent import *

class Nodes():
    def __init__(self):
        self.gmail = ""

    def get_latest_tweets(self, state):
        print("## Checking for new tweets for Tesla")

        # Use CSV agent to get latest tweets about Apple or some harcoded stock
        tweets = read_most_recent_rows_from_csv(10, "Tesla")
        print('Tweets for Tesla from csv ', tweets)

        return {
          **state,
          "tweets": tweets
        }

    def get_tweet_sentiment(self, state):
        print("## Get Tweet sentiment")

        # Use Sentiment agent to get sentiment
        sentiment = get_tweet_sentiment(state["tweets"])
        print('Tweets sentiment for Apple ', sentiment)

        return {
          **state,
          "tweet_sentiment": sentiment
        }

    def get_tweet_summary(self, state):
        print("## Get Tweet summary")

        # Use Summary agent to summarize
        return {
          **state,
          "tweet_summary": ""
        }

    def send_email(self, state):
        print("## Send email")

        # Use Summary agent to summarize
        return