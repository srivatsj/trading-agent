from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import AstraDB
from langchain.schema.runnable import RunnableMap
from langchain.prompts import ChatPromptTemplate

def extract_stock(tweet):
    chat_model = load_chat_model()
    prompt = load_prompt()

    # Generate the answer by calling OpenAI's Chat Model
    inputs = RunnableMap({
        'tweet': lambda x: x['tweet']
    })
    chain = inputs | prompt | chat_model
    response = chain.invoke({'tweet': tweet})
    return response.content

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

def load_chat_model():
    return ChatOpenAI(
        temperature=0.3,
        model='gpt-3.5-turbo',
        streaming=True,
        verbose=True
    )
