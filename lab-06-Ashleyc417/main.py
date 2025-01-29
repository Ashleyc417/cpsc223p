from calculator import *
from json import dump

def get_float_input(prompt):
    try:
        user_input = float(input(prompt))
        return user_input
    except ValueError:
        print("Invalid Input. Please enter a different decimal value.")
        return get_float_input(prompt)

def main():
    print("Welcome to your calculator!")
    num1 = get_float_input("Please enter your first decimal number.")
    num2 = get_float_input("Please enter your second decimal number.")

    print(f'{num1} + {num2} = {add(num1, num2)}')
    print(f'{num1} - {num2} = {subtract(num1, num2)}')
    print(f'{num1} * {num2} = {multiply(num1, num2)}')
    try:
        print(f'{num1} / {num2} = {divide(num1, num2)}')
    except ZeroDivisionError:
        print("Division by zero is not allowed.")

    operation_results =  {}
    operation_results['+'] = num1 + num2
    operation_results['-'] = num1 - num2
    operation_results['*'] = num1 * num2
    operation_results['/'] = num1 / num2

    results = {}
    results[f'{num1}, {num2}'] = operation_results

    file_name = input("Specify the name of the json file: ")
    json_file = open(file_name, 'w')
    dump(results, json_file)
    json_file.close()
