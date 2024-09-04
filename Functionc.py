#is_even function - takes any number as input and chexks if it is even or not, and returns an answer with true or false
import time

def is_even(n):
    if (n%2) == 0:
        print('Comp: Hmmm...')
        time.sleep(1)
        print('\tTrue')
    
    else:
        print('Comp: Hmmm...')
        time.sleep(1)
        print('\tFalse')

num = int(input('Enter a number: '))

print('\nUser: Computer')
time.sleep(1)
print('Comp: Yes')
time.sleep(1)
print(f'User: {num} is even?')
time.sleep(1)
is_even(num)