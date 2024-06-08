from crewai import Task
from textwrap import dedent

class TradingTasks():
  def ticker_analysis(self, agent, text):
    return Task(description=dedent(f"""You're a helpful Inspection Agent that gets a {text} and determines which company stock ticker symbol(s) are mentioned in the {text} and returns a comma separated list of stock ticker symbols where each stock ticker symbol is prefixed with '$', like $GOOGL.
    If the stock ticker symbol is not mentioned but a company or product name is mentioned return the stock ticker symbol for the company only if it exists.   If the stock ticker symbol for the company does not exist for cases where the company is a private company return 'UNKNOWN'.   
    If no companies are/or stock ticker symbols are mentioned in the whole tweet return 'NONE'.
    Always prefix each stock ticker symmbol with a '$' in the comma separate list unless the answer is 'UNKNOWN' or 'NONE'

    Example output:
    $GOOGL,$AAPL,$TSLA,$CRM
    {self.__tip_section()}
    """),
      agent=agent
    )
    
  def sentiment_analysis(self, agent, tweet, ticker): 
    return Task(description=dedent(f"""Known as the BEST twitter tweet sentiment analyst for a {tweet} regarding a particular stock ${ticker}, you're
      skilled at reading through tweets and determine whether the specified stock tweet is 'bullish', 'bearish', 'neutral' for ${ticker}
      and if it's not clear if the tweet is about ${ticker} return 'unknown'
      Example output:
      bullish
      {self.__tip_section()}     
      """),
      agent=agent
    )

  def summarization_analysis(self, agent, tweets, ticker):
    return Task(description=dedent(f"""
        Analyze the list of {tweets} and return the over recommendation for the {ticker} of 'bullish', 'bearish', or 'neutral'.
        If it's not clear what the overall recommendation is for the stock return 'unknown'.
        Also provide what was your reasoning for comming up with this recommendation.
        {self.__tip_section()}        
      """),
      agent=agent
    )

  def recommend(self, agent):
    return Task(description=dedent(f"""
        Review and synthesize the analyses provided by the
        Financial Analyst and the Research Analyst.
        Combine these insights to form a comprehensive
        investment recommendation. 
        
        You MUST Consider all aspects, including financial
        health, market sentiment, and qualitative data from
        EDGAR filings.

        Make sure to include a section that shows insider 
        trading activity, and upcoming events like earnings.

        Your final answer MUST be a recommendation for your
        customer. It should be a full super detailed report, providing a 
        clear investment stance and strategy with supporting evidence.
        Make it pretty and well formatted for your customer.
        {self.__tip_section()}
      """),
      agent=agent
    )

  def __tip_section(self):
    return "If you do your BEST WORK, I'll give you a $10,000 commission!"