To run the app:
```bash
streamlit run app_1.py
```

This will start the application server and will bring you to the web page you just created.

To install packages:
```bash
pip3 install -r requirements.txt
```

----------------------------------

# Team Name 
**Trading Agent**

## Team Members 
- Andy Lai
- Esra Ku
- Srivats Jayram

## Github Repo
[https://github.com/srivatsj/trading-agent/tree/main](https://github.com/srivatsj/trading-agent/tree/main)

## Project Brief

### MVP (for the class project)
1. Sentiment for Nvidia/Tesla over today or some interval
2. Twitter feed post from influencer filtered by this stock
3. Bloomberg/CNBC articles about this stock
4. Fine tune some model on the above dataset for classification
   - Use 50% to train, 20% to validate
   - Classify entire article or a tweet into bullish/bearish 
   - Store remaining 30% in database to simulate real time ingestion of data 
5. A sentiment analysis on a specific stock (Nvidia/Tesla)
6. Answers questions related to a stock (Nvidia/Tesla)

### Version 1.0 
- Extend it to MAG7+.
- Live evaluation based on most recent tweets/articles.
- Almost-Live evaluation based on the streaming tweets/articles.

### Advanced
- Email/notification to the user what stock to buy or sell.
- Auto purchase - based on bullish/bearish analysis, trading volume, etc.

## Components

### Component 1: Chat Bot
- Interacts with the users.
- Sample user query: “Can you tell me about TSLA”
- Sample answer: Based on these 10 latest Tesla tweets, we are bullish.

### Component 2: Tweet Injector / Simulator
- Helps simulate streaming tweets.
- Sample query: “Inject 10 bullish tweets about NVDA” (use a mix of Ticket symbol, hashtags, company name, typos).
  - Creates 10 tweets.
  - Injects tweets with the ticker symbol and date to csv file.
  - Call the email agent if the new sentiment is different.

## Agents
1. Extract Ticker symbol via LLM
2. If (1) is not possible, use a web search agent to find a ticker symbol.
3. Sentiment of 1 tweet.
4. Summarization/aggregation of n=10 tweets.
5. Email agent.
6. (Optional) post on twitter agent.
7. Query understanding agent (To avoid answering questions outside of stock).

## CSV Format
```
<Ticker Symbol>, <Timestamp>, <Tweet Content>, <Sentiment>
```


## Workflow Link

TODO