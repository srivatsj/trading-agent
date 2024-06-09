from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_openai import ChatOpenAI, OpenAI

def read_most_recent_rows_from_csv(number_of_tweets, ticker_symbol):
    agent = create_csv_agent(
        OpenAI(temperature=0),
        'assets/tweets.csv',
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )

    #agent.run("how many rows are there?")

    #agent.run("What are the 3 tweets with the largest timestamp values?")

    # Use format method to insert the variable into the string
    query = "Find the 'Tweet Content' of {} tweets with the largest timestamp values where 'Ticker Symbol' is {}? Return the result as a string array".format(number_of_tweets, ticker_symbol)

    # Run the query
    result = agent.run(query)

    # Print the result
    print(result)

    # Return the twitter content of each of these n rows
    return result