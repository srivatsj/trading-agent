import os
import time

class Nodes():
    def __init__(self):
        self.gmail = ""

    def get_latest_tweets(self, state):
        print("## Checking for new tweets for Apple")

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

    def send_email(self, state):
        print("## Send email")

        # Use Summary agent to summarize
        return