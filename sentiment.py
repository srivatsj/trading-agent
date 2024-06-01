import streamlit as st
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import AstraDB
from langchain.schema.runnable import RunnableMap
from langchain.prompts import ChatPromptTemplate
import csv_reader as cr

# Cache prompt for future runs
@st.cache_data()
def load_prompt():
    template = """You're a helpful AI Trading Agent that gets a list of the 10 latest tweets. Classify each tweet as bullish, bearish or neutral.   If it's not clear what the sentiment of the tweet is, return unknown.   Additionally, please summarize the tweets and give an overall recommendation of bullish, bearish or neutral for the given stock.
 
Tweets:
{tweets}

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
# Draw a title and some markdown
st.title("~~~Trading Agent~~~")
st.markdown("""Trading Agent""")

# Get the first column values from 10 random rows
first_column_values = cr.read_random_rows_from_csv()
st.markdown("Tweets:")
st.markdown(first_column_values)

# Draw all messages, both user and bot so far (every time the app reruns)
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

# Draw the chat input box
if tweets := st.chat_input("Get me tweets?"):
    
    # Store the user's tweets in a session object for redrawing next time
    st.session_state.messages.append({"role": "human", "content": tweets})

    # Draw the user's question
    with st.chat_message('human'):
        st.markdown(tweets)

    # Generate the answer by calling OpenAI's Chat Model
    inputs = RunnableMap({
        'tweets': lambda x: x['tweets']
    })
    chain = inputs | prompt | chat_model
    response = chain.invoke({'tweets': first_column_values})
    answer = response.content

    # Store the bot's answer in a session object for redrawing next time
    st.session_state.messages.append({"role": "ai", "content": answer})

    # Draw the bot's answer
    with st.chat_message('assistant'):
        st.markdown(answer)
