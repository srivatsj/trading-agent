import pandas as pd
import random

def read_random_rows_from_csv():
    # Read the CSV file
    df = pd.read_csv('assets/tweets.csv')

    # Ensure there are enough rows to pick from
    if len(df) < 10:
        raise ValueError("The CSV file has fewer than 10 rows")

    # Randomly pick 10 rows
    random_rows = df.sample(n=10)

    # Get the first column of each of these rows
    first_column_values = random_rows.iloc[:, 0].tolist()

    return first_column_values