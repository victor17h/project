
menu_prompt = """
Select an operation:
-add
-subtract
-multiply
-divide
-quit
"""

decision = input(menu_prompt).strip().lower()


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x // y


while decision != 'quit':
    number1 = int(input("Insert a number: "))
    number2 = int(input("Insert another number: "))
    if decision == 'add':
        print(f"{number1} + {number2} = {add(number1, number2)}")
    elif decision == 'subtract':
        print(f"{number1} - {number2} = {subtract(number1, number2)}")
    elif decision == 'multiply':
        print(f"{number1} * {number2} = {multiply(number1, number2)}")
    elif decision == 'divide':
        print(f"{number1} // {number2} = {divide(number1, number2)}")
    else:
        print("Please enter a valid operation or quit")

    decision = input(menu_prompt).strip().lower()
