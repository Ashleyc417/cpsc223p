# --------------------WRITE YOUR CODE BELOW-------------------#
from os import *
from re import *
from math import *
from random import *
from statistics import *
from datetime import *
import timeit 
from reprlib import *
from pprint import *
from textwrap import *
from string import *
from logging import *
from heapq import * 

# Task 1: List all files in specific directory and display their names.
def list_files_in_directory(dir):
    for root, dirs, files in walk(dir):
        for file in files:
            print(path.join(root, file))
   
# Task 2: Search for and extract email addresses from a given text.
def extract_emails(text):
    sample_email = r'\b[a-zA-Z]+@[a-zA-Z]+\b'
    emails = findall(sample_email, text)
    for email in emails:
        print(email)

# Task 3: Calculates the square root of a user-inputted number using the math module.
def calculate_square_root(num):
    print("Square Root of " , num , " is " , sqrt(num))

# Task 4: Generate and print a random integer between a specified range using the random module.
def generate_random_integer(a, b):
    print("Random integer between " , a , " and " , b , ": " , randint(a, b))

# Task 5: Compute mean and standard deviation of a list of nums.
def calculate_mean_and_stddev(nums):
    print("Mean: " , mean(nums), ", Standard Deviation: " , stdev(nums))

# Task 6: Print current date.
def print_current_datetime():
    print("Current Date and Time: " , datetime.now())
     
# Task 7: Measure time it takes to execute function using timeit.
def time_function_execution():
    print("Time taken to execute function 10000 times: " , timeit.timeit('x = 12', number=10000), " seconds")

# Task 8: Create a concise representation of a long string.
def truncate_long_string(text):
    print("Truncated String: " , repr(text))

# Task 9: Use the pprint module to pretty-print a nested dictionary.
def pretty_print_nested_dict(dict):
    pprint(dict)

# Task 10: Use the textwrap module to format a long text paragraph into multiple lines with a specified line width.  
def wrap_text_paragraph(paragraph, int):
    print(fill(paragraph, int))

# Task 11: Use the string.Template class to generate dynamic SQL queries with placeholders.  
def generate_sql_query(table_name, columns):
    print("Generated SQL Query: " , Template("SELECT $columns FROM $table_name").substitute(columns=columns, table_name=table_name))

# Task 12: Set up logging to record events to a log file using the logging module. 
def setup_logging():
    pass

# Use the heapq module to perform heap operations on a list of integers.
def perform_heap_operations(sample_nums):
    heap = sample_nums
    heapify(heap)
    print('Heapified List: ', heap)
    print("Smallest Element: " , (nsmallest(1, sample_nums))[0])

# --------------------END OF YOUR CODE------------------------#

'''
CREATE THE BELOW CALLED FUNCTION DEFINITION IN YOUR CODE!
'''

if __name__ == '__main__':

    # Sample data for tasks
    sample_text = "Sample email addresses: abc@example.com, xyz@domain.com"
    sample_numbers = [2, 4, 6, 8, 10]
    sample_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
    sample_paragraph = "This is a long paragraph that needs to be wrapped to multiple lines for better readability."
    sample_number = 12345.67
    sample_table_name = "users"
    sample_columns = "id, name, email"
    sample_numbers_for_heap = [3, 1, 4, 1, 5, 9]

    # Task executions
    list_files_in_directory(".")  # Task 1
    extract_emails(sample_text)  # Task 2
    calculate_square_root(16)  # Task 3
    generate_random_integer(1, 100)  # Task 4
    calculate_mean_and_stddev(sample_numbers)  # Task 5
    print_current_datetime()  # Task 6
    time_function_execution()  # Task 7
    truncate_long_string("This is a very long string that needs to be truncated.")  # Task 8
    pretty_print_nested_dict(sample_dict)  # Task 9
    wrap_text_paragraph(sample_paragraph, 30)  # Task 10
    generate_sql_query(sample_table_name, sample_columns)  # Task 11
    setup_logging()  # Task 12
    perform_heap_operations(sample_numbers_for_heap)  # Task 13
