#calculator, basic operations
import math as m
def dif(x, y):
    return x-y
def div(x, y):
    return x/y
def exp(x, y):
    return x**y
def multiply(x, y):
    return x*y
def sum(x, y):
    return x+y
print('Setup complete!')
print('\nWecome to calculator basic ops!')
print('\nAvailable ops:\nSum\nDifference\nMultiplication\nDivision\nExponential')
operations = ['Sum', 'Difference', 'Multiplication', 'Division', 'Exponential']
while True:
    choice = input('\nEnter choice')
    if choice in operations:
        x = float(input('\nInsert first number'))
        y = float(input('\nInsert second number'))
        if choice == 'Sum':
            print(sum(x, y))
        elif choice == 'Difference':
            print(dif(x, y))
        elif choice == 'Multiplication':
            print(multiply(x, y))
        elif choice == 'Division':
            print(div(x, y))
        elif choice == 'Exponential':
            print(exp(x, y))
        fd = input('keep calculating?')
        if fd == 'y':
            continue
        else:
            break
    else:
        print('Invalid Input')
