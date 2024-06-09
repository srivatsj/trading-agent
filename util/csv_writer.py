import csv

def write_array_to_csv(data):
    with open('assets/tweets.csv', mode='a') as file:
        writer = csv.writer(file)
        for item in data:
            file.write(item + "\n")

def append_prefix_to_csv():
    with open('assets/tweets.csv', mode='r') as file:
        lines = file.readlines()

    prefix = '"TSLA","1717372497000"'
    with open('assets/tweets.csv', mode='a') as file:
        for line in lines:
            line = f'{prefix},{line}'
            file.write(line)