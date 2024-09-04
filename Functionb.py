#square function - takes any number as input and gives you the square as an output

def square(n):
    n = int(n) ** 2
    return n

num = input('Enter a number, any number: ')
print(square(num))