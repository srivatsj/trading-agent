from crewai import Agent

from tools.search_tools import SearchTools

from langchain.tools.yahoo_finance_news import YahooFinanceNewsTool

class TradingAgents():
  def ticker_analyst(self):
    return Agent(
      role='The Best Stock ticker Extractor',
      goal="""Return a comma separated list of stock ticker symbols from the {tweet}""",
      backstory="""You're a helpful Tweet Stock Tweet Inspection Agent that gets a tweet and determine which company stock ticker symbols are mentioned in tweet an return a comma separate list of stock ticker symbols where each stock ticker symbol is prefixed with '$', like $GOOGL.
    If the stock ticker symbol is not mentioned but a company or product name is mentioned return the stock ticker symbol for the company only if it exists.   If the stock ticker symbol for the company does not exist for cases where the company is a private company return 'UNKNOWN'.   
    If no companies are/or stock ticker symbols are mentioned in the whole tweet return 'NONE'.
    Always prefix each stock ticker symmbol with a '$' in the comma separate list unless the answer is 'UNKNOWN' or 'NONE'

    Example output:
    $GOOGL,$AAPL,$TSLA,$CRM
    """,
      verbose=True,
      tools=[
        SearchTools.search_internet
      ]
    )

  def sentiment_analyst(self):
    return Agent(
      role='Staff Research Analyst',
      goal="""Being the best at gather, interpret data and amaze
      your customer with it""",
      backstory="""Known as the BEST research analyst, you're
      skilled in sifting through news, company announcements, 
      and market sentiments. Now you're working on a super 
      important customer""",
      verbose=True,
      tools=[]
  )

  def investment_advisor(self):
    return Agent(
      role='Private Investment Advisor',
      goal="""Impress your customers with full analyses over stocks
      and completer investment recommendations""",
      backstory="""You're the most experienced investment advisor
      and you combine various analytical insights to formulate
      strategic investment advice. You are now working for
      a super important customer you need to impress.""",
      verbose=True,
      tools=[
        SearchTools.search_internet,
        SearchTools.search_news,
        YahooFinanceNewsTool()
      ]
    )