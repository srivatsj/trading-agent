import os
import time
from agents.csv_agent import *
from agents.sentiment_agent import *
from agents.stock_extractor_agent import *
from agents.summarize_agent import *

class Nodes():
    def __init__(self):
        self.gmail = ""

    def get_latest_tweets(self, state):
        print("## Checking for most recent tweets")

        # Use CSV agent to get latest tweets about a certain stock
        tweets = read_most_recent_rows_from_csv(10, state["ticker_symbol"])
        print('Most recent 10 tweets from csv ', tweets)

        return {
          **state,
          "tweets": tweets
        }

    def get_tweet_sentiment(self, state):
        print("## Get Tweet sentiment")

        # Use Sentiment agent to get sentiment
        sentiment = get_tweet_sentiment(state["tweets"])
        print('Tweets sentiment ', sentiment)

        return {
          **state,
          "tweet_sentiment": sentiment
        }

    def get_tweet_summary(self, state):
        print("## Get Tweet summary")

        # Use Summary agent to summarize
        summary = get_tweet_summary(state["tweets"])
        print('Tweets summary ', summary)

        return {
          **state,
          "tweet_summary": summary
        }

    def send_email(self, state):
        print("## Send email")

        # Use Email agent to send email
        return