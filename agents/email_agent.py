from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import AstraDB
from langchain.schema.runnable import RunnableMap
from langchain.prompts import ChatPromptTemplate
from langchain_community.agent_toolkits.gmail.toolkit import GmailToolkit
from langchain.agents import initialize_agent, AgentType
from langchain_community.tools.gmail.utils import (
    build_resource_service,
    get_gmail_credentials,
)

# Cache OpenAI Chat Model for future runs
def load_chat_model():
    return ChatOpenAI(
        temperature=0.3,
        model='gpt-3.5-turbo',
        streaming=True,
        verbose=True
    )

def send_email():
    # Generate the answer by calling OpenAI's Chat Model
    print("tweet summary debug2 inside email agent")
    #print(tweets)
    chat_model = load_chat_model()

    #credentials = get_gmail_credentials(
    #    scopes=["https://mail.google.com/"],
    #    client_secrets_file="credentials.json",
    #)
    
    #api_resource = build_resource_service(credentials=credentials)
    #toolkit = GmailToolkit(api_resource=api_resource)

    #tools = toolkit.get_tools()

    #agent = initialize_agent(tools=tools, llm=chat_model, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    #agent.run(
    #"Send email title 'Test' to andycodepath@gmail.com")


def main():
    print("send email start")
    answer = send_email()
    print("send email end")


if __name__ == "__main__":
    main()
