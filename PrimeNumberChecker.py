n = int(input('Enter a number let me check if it is a prime number: '))#Takes an input and converts it to int
checker = 1

if n > 2:
    for i in range(2, n):
        if(n%i) == 0:
            print(f'\n{n} is not a prime number.')
            print(f'Its first factor is {i} x {n//i} = {n}.\n')
            checker = 0
        
        elif (checker == 1):
            print(f'\n{n} is a prime number.\n')
        break

else:
    print(f'\n{n} is a prime number.\n')
