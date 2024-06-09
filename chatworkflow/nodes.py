import os
import time
from agents.csv_agent import *
from agents.sentiment_agent import *
from agents.stock_extractor_agent import *
from agents.summarize_agent import *
from util.util import *

class Nodes():
    def __init__(self):
        self = ""

    def extract_stock_from_input(self, state):
        print("\n## Extracting stock symbol from input: ", state["sentence"])

        ticker_symbol = get_first_word(extract_stock(state["sentence"]))
        print('Ticker symbol is ', ticker_symbol)

        # Use Stock extractor agent to get stock symbol
        return {
          **state,
          "ticker_symbol": ticker_symbol
        }
    
    def get_latest_tweets(self, state):
        print("\n## Checking for most recent tweets for ", state["ticker_symbol"])

        # Use CSV agent to get latest tweets about a certain stock
        tweets = read_most_recent_rows_from_csv(10, state["ticker_symbol"])
        print('Most recent 10 tweets are: \n', tweets)

        return {
          **state,
          "tweets": tweets
        }

    def get_tweet_summary(self, state):
        print("\n## Creating summary based on most recent tweets...")

        # Use Summary agent to summarize
        summary = get_tweet_summary(state["tweets"])
        print('Summary of the most recent tweets: ', summary)

        return {
          **state,
          "tweet_summary": summary
        }
        
    def get_tweet_sentiment(self, state):
        print("\n## Analyzing each tweet sentiment separately as a proof of above summary...")

        # Use Sentiment agent to get sentiment
        sentiment = get_tweet_sentiment(state["tweets"])
        print('Tweet sentiments: ', sentiment)

        return {
          **state,
          "tweet_sentiment": sentiment
        }