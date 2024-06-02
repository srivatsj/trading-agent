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
    template = """You're a helpful Tweet Stock Tweet Inspection Agent that gets a tweet and determine which company stock ticker symbols are mentioned in tweet an return a comma separate list of stock ticker symbols where each stock ticker symbol is prefixed with '$', like $GOOGL.
    If the stock ticker symbol is not mentioned but a company or product name is mentioned return the stock ticker symbol for the company only if it exists.   If the stock ticker symbol for the company does not exist for cases where the company is a private company return 'UNKNOWN'.   
    If no companies are/or stock ticker symbols are mentioned in the whole tweet return 'NONE'.
    Always prefix each stock ticker symmbol with a '$' in the comma separate list unless the answer is 'UNKNOWN' or 'NONE'

Example output:
$GOOGL,$AAPL,$TSLA,$CRM
 
Tweets:
{tweet}

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

def get_answer(tweet):
    # Generate the answer by calling OpenAI's Chat Model
    inputs = RunnableMap({
        'tweet': lambda x: x['tweet']
    })
    chain = inputs | prompt | chat_model
    response = chain.invoke({'tweet': tweet})
    answer = response.content
    return answer


# Start with empty messages, stored in session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Draw a title and some markdown
# Draw a title and some markdown
st.title("~~~Tweet Ticker Extractor Agent~~~")
st.markdown("""Tweet Ticker Extractor Agent""")

# Draw all messages, both user and bot so far (every time the app reruns)
#for message in st.session_state.messages:
#    st.chat_message(message['role']).markdown(message['content'])

# Draw the chat input box
if tweet := st.chat_input("Enter a tweet"):
    
    # Store the user's tweet in a session object for redrawing next time
    st.session_state.messages.append({"role": "human", "content": tweet})

    # Draw the user's tweet
    with st.chat_message('human'):
        st.markdown(tweet)

    # Generate the answer by calling OpenAI's Chat Model
    #inputs = RunnableMap({
     #   'tweet': lambda x: x['tweet']
    #})
    #chain = inputs | prompt | chat_model
    #response = chain.invoke({'tweet': tweet})
    #answer = response.content

    answer = get_answer(tweet)
    # Store the bot's answer in a session object for redrawing next time
    st.session_state.messages.append({"role": "ai", "content": answer})

    # Draw the bot's answer
    with st.chat_message('assistant'):
        st.markdown(answer)
