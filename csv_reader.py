import pandas as pd
import random

def read_random_rows_from_csv():
    # Read the CSV file
    # Format of csv file: "Ticker Symbol","Timestamp", "Tweet Content", "Sentiment"
    df = pd.read_csv('assets/tweets.csv')


    # Ensure there are enough rows to pick from
    if len(df) < 10:
        raise ValueError("The CSV file has fewer than 10 rows")

    # Randomly pick 10 rows
    random_rows = df.sample(n=10)

    # Get the third column(twitter content) of each of these rows
    third_column_values = random_rows.iloc[:, 2].tolist()

    return third_column_values

def read_most_recent_rows_from_csv(number_of_tweets, ticker_symbol):
    # Read the CSV file
    # Format of csv file: "Ticker Symbol","Timestamp", "Tweet Content", "Sentiment"
    df = pd.read_csv('assets/tweets.csv')

    # Filter rows by the specified ticker symbol
    df_filtered = df[df['Ticker Symbol'] == ticker_symbol]

    # Ensure there are enough rows to pick from
    if len(df_filtered) < number_of_tweets:
        raise ValueError("The CSV file has fewer than desired rows")
    
    # If we are always adding with non-decreasing timestamp, then we can probably skip this.
    # Sort the DataFrame by the 'Timestamp' column in descending order
    df_sorted = df_filtered.sort_values(by='Timestamp', ascending=False)

    # Select the most recent rows based on the specified number
    recent_rows = df_sorted.head(number_of_tweets)

    # Get the third column(twitter content) of each of these rows
    third_column_values = recent_rows.iloc[:, 2].tolist()

    return third_column_values