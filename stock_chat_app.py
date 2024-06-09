import streamlit as st
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import AstraDB
from langchain.schema.runnable import RunnableMap
from langchain.prompts import ChatPromptTemplate
import agents.csv_agent as cr
from chatworkflow.graph import ChatWorkFlow

# Start with empty messages, stored in session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Draw a title and some markdown
st.title("~~~Trading Agent~~~")
st.markdown("""Trading Agent""")

# Draw all messages, both user and bot so far (every time the app reruns)
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

# Draw the chat input box
if question := st.chat_input("What's up?"):
    
    # Store the user's question in a session object for redrawing next time
    st.session_state.messages.append({"role": "human", "content": question})

    # Draw the user's question
    with st.chat_message('human'):
        st.markdown(question)

    print("question: ", question)
    app = ChatWorkFlow().app
    data = app.invoke({"sentence": question})

    # Extracting the needed information
    tweets = data['tweets'].split('\n')
    tweet_sentiment_lines = data['tweet_sentiment'].split('\n')
    tweet_summary = data['tweet_summary']

    # Draw the bot's answer
    with st.chat_message('assistant'):
        st.subheader("Tweet Summary")
        st.markdown(f"{tweet_summary}")

        st.subheader("Tweets and Sentiments")
        
        for i, tweet in enumerate(tweets):
            if i < len(tweet_sentiment_lines):
                sentiment = tweet_sentiment_lines[i].split(' ', 1)[1]  # Extracting sentiment text after number
            else:
                sentiment = "No sentiment available"
            st.markdown(f"**Tweet {i+1}:** {tweet}")
            st.markdown(f"**Sentiment:** {sentiment}")
            st.markdown("---")  # Add a horizontal rule for better separation