from dotenv import load_dotenv
load_dotenv()

from langgraph.graph import StateGraph, END

from .state import State
from .nodes import Nodes

class ChatWorkFlow():
	def __init__(self):
		nodes = Nodes()
		workflow = StateGraph(State)

		workflow.add_node("extract_stock_from_input", nodes.extract_stock_from_input)
		workflow.add_node("get_latest_tweets", nodes.get_latest_tweets)
		workflow.add_node("get_tweet_sentiment", nodes.get_tweet_sentiment)
		workflow.add_node("get_tweet_summary", nodes.get_tweet_summary)

		workflow.set_entry_point("extract_stock_from_input")
		
		workflow.add_edge('extract_stock_from_input', 'get_latest_tweets')
		workflow.add_edge('get_latest_tweets', 'get_tweet_sentiment')
		workflow.add_edge('get_tweet_sentiment', 'get_tweet_summary')
		workflow.add_edge("get_tweet_summary", END)
		
		self.app = workflow.compile()