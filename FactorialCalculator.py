""" #Factorial Calculator
#Using a for loop
n = int(input('\nPlease enter a number, let my calculator calculate its factorial: '))
#takes the factorial number as str and converts it to int

if n == 1:
    print(f'{n}! = {n}\n')

else:
    fact = 1
    #I initialized the final result as the inputed number so that if starts multiplying, it will start from 'n',
        #then '1' - being the first value of our counter variable, through to 'n-1' - being the last value of our
        #counter variable

    print(n, end = '! =')
    i = 1
    for i in range(1, n):
        #I did this because if the object to be iterated over, range is just 'range(n)', the first value of our counter,
            #'i' would be '0', and 'zero' multiplied by fact will nulify everou are doing.
            #So if I declare my range to be from 1 through to 'n-1', making 'i' to start from '1' and not 
            #nullifying our end result
        print(end = f' {i} x')
        fact *= i
    print('', n)

    print(f'{n}! = {fact}\n') """

#Using a while loop
n = int(input('\nPlease enter a number, let my calculator calculate its factorial: '))
#takes the factorial number as str and converts it to int

if n == 1:
    print(f'{n}! = {n}\n')

else:
    i = 1
    fact = n
    #I initialized the final result as the inputed number so that if starts multiplying, it will start from 'n',
        #then '1' - being the first value of our counter variable, through to 'n-1' - being the last value of our
        #counter variable
    print(n, end = '! =')
    while i < n:
        print(end = f' {i} x')
        fact *= i
        i += 1
    print('',n)

    print(f'{n}! = {fact}\n')