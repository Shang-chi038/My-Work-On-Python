#greet() function - takes a person's name as input and greets the person

def greet(n):
    greet = (f'Good day, {n}')
    return greet

name = input('Enter your name: ')
print(greet(name))