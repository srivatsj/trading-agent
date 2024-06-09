from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import AstraDB
from langchain.schema.runnable import RunnableMap
from langchain.prompts import ChatPromptTemplate

def get_tweet_sentiment(tweets):
    chat_model = load_chat_model()
    prompt = load_prompt()

    # Generate the answer by calling OpenAI's Chat Model
    inputs = RunnableMap({
        'tweets': lambda x: x['tweets']
    })
    chain = inputs | prompt | chat_model
    response = chain.invoke({'tweets': tweets})
    return response.content

def load_prompt():
    template = """You're a helpful AI Trading Agent that gets a list of the latest tweets. Classify each tweet as bullish, bearish or neutral.   
    If it's not clear what the sentiment of the tweet is, return unknown.
 
Tweets:
{tweets}

YOUR ANSWER:"""
    return ChatPromptTemplate.from_messages([("system", template)])

# Cache OpenAI Chat Model for future runs
def load_chat_model():
    return ChatOpenAI(
        temperature=0.3,
        model='gpt-3.5-turbo',
        streaming=True,
        verbose=True
    )
