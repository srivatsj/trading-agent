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

    # Get the thrid column(twitter content) of each of these rows
    third_column_values = random_rows.iloc[:, 2].tolist()

    return third_column_values