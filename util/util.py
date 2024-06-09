
from datetime import datetime

def append_ticker_and_time(input_array, ticker_symbol_array):
    timestamp_str = str(int(datetime.now().timestamp() * 1000))
    print("Current Timestamp:", timestamp_str)
    output_array = []
    i=0
    for element in input_array:
        # Append "TSLA" and timestamp to each element
        new_element =  "\"" + ticker_symbol_array[i] + "\",\"" + timestamp_str + "\"," + element
        i=i+1
        output_array.append(new_element)
    return output_array

def get_first_word(input_string):
    # Split the input string by commas
    words = input_string.split(',')

    # Return the first word
    return remove_dollar_sign(words[0])

def remove_dollar_sign(input_string):
    if input_string.startswith('$'):
        return input_string[1:]
    return input_string