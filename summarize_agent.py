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
   

# Cache OpenAI Chat Model for future runs
def load_chat_model():
    return ChatOpenAI(
        temperature=0.3,
        model='gpt-3.5-turbo',
        streaming=True,
        verbose=True
    )

def get_tweet_summary(tweets):
    # Generate the answer by calling OpenAI's Chat Model
    #print("tweet summary debug2")
    #print(tweets)
    chat_model = load_chat_model()
    prompt = load_prompt()

    inputs = RunnableMap({
        'tweets': lambda x: x['tweets']
    })
    chain = inputs | prompt | chat_model
    response = chain.invoke({'tweets': tweets})
    return response.content


def main():
    """
    This is the main function of the script.
    """
    input_array = ['Tesla is doing great!!!'
 "Tesla's upcoming earnings report is highly anticipated by investors, with expectations of strong financial performance. #TSLA"
 "Despite challenges in the global supply chain, Tesla's resilient business model has helped it navigate through uncertainties. #TSLA"
 "Tesla's commitment to sustainability and innovation sets it apart from traditional automakers. #TSLA"
 "Tesla's stock price has been on a steady upward trend, reflecting investor confidence in the company's future prospects. #TSLA"
 "The demand for Tesla's Model 3 remains strong, indicating continued growth for the company. #TSLA"
 "Tesla's recent partnership with a leading battery manufacturer is a strategic move to secure its supply chain. #TSLA"
 "Elon Musk's vision for Tesla's future includes expanding into the renewable energy sector. #TSLA"
 "Tesla's innovative Autopilot technology continues to set the standard for autonomous driving systems. #TSLA"
 "Analysts predict that Tesla's Cybertruck will be a game-changer in the electric vehicle market. #TSLA"]
    answer = get_tweet_summary(input_array)
    print(answer)


if __name__ == "__main__":
    main()
