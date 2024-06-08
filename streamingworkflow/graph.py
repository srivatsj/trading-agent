from dotenv import load_dotenv
load_dotenv()

from langgraph.graph import StateGraph, END

from .state import State
from .nodes import Nodes

class StreamingWorkFlow():
	def __init__(self):
		nodes = Nodes()
		workflow = StateGraph(State)

		workflow.add_node("get_latest_tweets", nodes.get_latest_tweets)
		workflow.add_node("get_tweet_sentiment", nodes.get_tweet_sentiment)
		workflow.add_node("get_tweet_summary", nodes.get_tweet_summary)
		workflow.add_node("send_email", nodes.send_email)

		workflow.set_entry_point("get_latest_tweets")
		
		workflow.add_edge('get_latest_tweets', 'get_tweet_sentiment')
		workflow.add_edge('get_tweet_sentiment', 'get_tweet_summary')
		workflow.add_edge('get_tweet_summary', 'send_email')
		workflow.add_edge("send_email", END)
		
		self.app = workflow.compile()