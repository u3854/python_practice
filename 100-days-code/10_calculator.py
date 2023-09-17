from calculator_art import logo
import os

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    if n2>0:
        return n1/n2
    
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for op in operations:
        print(op)
    operation_symbol = input("Pick an operator from the line above: ")
    num2 = float(input("What's the second number?: "))

    continue_calc = 'y'

    while continue_calc == 'y':
        
        answer = operations[operation_symbol](num1,num2)
        if answer == None:
            print('Failed to compute. Please restart.')
            break
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        continue_calc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.\nType any other key to start a fresh calculation.\n").lower()
        if continue_calc == 'y':
            operation_symbol = input("Pick an operation: ")
            num2 = float(input("What's the next number?: "))
            num1 = answer
        elif continue_calc == 'n':
            continue
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            calculator()

calculator()
