import streamlit as st
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import AstraDB
from langchain.schema.runnable import RunnableMap
from langchain.prompts import ChatPromptTemplate

# Cache prompt for future runs

def load_prompt():
    template =  """You're a helpful AI Trading Agent that gets a list of the latest tweets please summarize the tweets and give an overall recommendation of bullish, bearish or neutral for the given stock.
 
Tweets:
{tweets}

YOUR ANSWER:"""
    return ChatPromptTemplate.from_messages([("system", template)])
   

def load_chat_model():
    return ChatOpenAI(
        temperature=0.3,
        model='gpt-3.5-turbo',
        streaming=True,
        verbose=True
    )

def get_summarization(tweets):
    # Generate the answer by calling OpenAI's Chat Model
    chat_model = load_chat_model()
    prompt = load_prompt()
    inputs = RunnableMap({
        'tweets': lambda x: x['tweets']
    })
    chain = inputs | prompt | chat_model
    response = chain.invoke({'tweets': tweets})
    answer = response.content
    return answer


def main():
    """
    This is the main function of the script.
    """
    input_array = ["TSLA is up", "TSLA is bullish", "TSLA is a sell", "TSLA should be bought", "TSLA stock up"]
    answer = get_summarization(input_array)
    print(answer)


if __name__ == "__main__":
    main()
