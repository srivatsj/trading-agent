import streamlit as st
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import AstraDB
from langchain.schema.runnable import RunnableMap
from langchain.prompts import ChatPromptTemplate
import util.csv_writer as cw
from streamingworkflow.graph import StreamingWorkFlow
from chatworkflow.graph import ChatWorkFlow
from langchain_core.messages import HumanMessage
import agents.stock_extractor_agent as stock_extractor_agent
from util.util import *

# Cache prompt for future runs
@st.cache_data()
def load_prompt():
    template = """You're a helpful AI assistent tasked to generate N variations of tweet-sentiment pairs.
    Each tweet should be unique and clearly phrased and related to stock analysis of STOCKNAME stock.
    The corresponding sentiment should be one of bullish, bearish, neutral.
    Output should be csv format with two columns: first column is the tweet content and the second column is the sentiment which is bullish, bearish or neutral.
    Don't include header row in the output.
    Example output format:
    "Tweet content","bullish"

    User's question is in the form of "Generate N tweets for STOCKNAME" and that is how you decide how many tweets and for which stock you will be creating.
    If user specifies bullish/bearish/neutral, only generate tweets with that sentiment.
    If user does not specify or asks for random generate a variation of all 3.

    QUESTION:
    {question}

    YOUR ANSWER:"""
    return ChatPromptTemplate.from_messages([("system", template)])
prompt = load_prompt()

# Cache OpenAI Chat Model for future runs
@st.cache_resource()
def load_chat_model():
    return ChatOpenAI(
        temperature=0.3,
        model='gpt-3.5-turbo',
        streaming=True,
        verbose=True
    )
chat_model = load_chat_model()

# Start with empty messages, stored in session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Draw a title and some markdown
st.title("~~~Tweet Injector Agent~~~")
st.markdown("""Example usage: Generate N tweets for STOCKNAME""")

# Draw all messages, both user and bot so far (every time the app reruns)
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

# Draw the chat input box
if question := st.chat_input("Generate tweets?"):
    
    # Store the user's question in a session object for redrawing next time
    st.session_state.messages.append({"role": "human", "content": question})

    # Draw the user's question
    with st.chat_message('human'):
        st.markdown(question)

    # Generate the answer by calling OpenAI's Chat Model
    inputs = RunnableMap({
        'question': lambda x: x['question']
    })
    chain = inputs | prompt | chat_model
    response = chain.invoke({'question': question})
    answer = response.content

    # Store the bot's answer in a session object for redrawing next time
    st.session_state.messages.append({"role": "ai", "content": answer})

    # Convert answer into a str array.
    tweets_array = answer.split('\n')
    print("tweets_array", tweets_array)

    # Extract the ticker symbol
    ticker_symbol_array = []
    for tweet in tweets_array:
        extracted_symbol = stock_extractor_agent.extract_stock(tweet)
        # In case the tweet is about multiple stocks, extract the first symbol and ignore the rest.
        first_symbol = get_first_word(extracted_symbol)
        ticker_symbol_array.append(first_symbol)

    print("ticker_symbol_array ", ticker_symbol_array)

    # Add ticker symbol and timestamp to each element.
    final_tweets_array = append_ticker_and_time(tweets_array, ticker_symbol_array)

    # Write "Ticker Symbol","Timestamp", "Tweet Content", "Sentiment" to csv file.
    cw.write_array_to_csv(final_tweets_array)

    # Define the sentence you want to pass as a parameter
    app = StreamingWorkFlow().app
    app.invoke({"ticker_symbol": ticker_symbol_array[0]})

    # Draw the bot's answer
    with st.chat_message('assistant'):
        for tweet in final_tweets_array:
          st.markdown(tweet)
