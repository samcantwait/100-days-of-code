from calculator_art import logo


# Add
def add(n1, n2):
    return n1 + n2

# Subtract


def subtract(n1, n2):
    return n1 - n2

# Multiply


def multiply(n1, n2):
    return n1 * n2

# Divide


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    print(logo)
    num1 = float(input("What is the first number?  "))
    for operator in operations:
        print(operator)

    should_continue = True
    while should_continue == True:
        operator = input('Please choose an operator:  ')
        num2 = float(input('What is the next number?  '))
        result = operations[operator](num1, num2)
        print(f'{num1} {operator} {num2} = {result}')
        calculate_again = input(
            f'Type "y" if you would like to continue with {result}, "n" if you would like to start a new calculation, or "exit" if you would like to exit:  ')
        if calculate_again == 'n':
            should_continue = False
            calculator()
        elif calculate_again == 'y':
            num1 = result
        else:
            should_continue = False


calculator()
