print('\t\t\tTHIS IS A CALCULATOR')
print('''This calculator accepts two values from you the user and any operation
\t\tyou want to perform\n\n''')

#This is to initialize a counter variable for the user allow
#the user perform a calculation multiple times.
query = str(input('Do want to perform a calculation? Y/N: '))

if query=='Y' or query=='y':
    #I initialize my counter variable for various operations and
    #the operation to be carried out
    n_add = -1
    n_diff = -1
    n_product = -1
    n_div = -1
    ops = -1
    
    #The list my results and operations will be stored in
    add_list = []
    diff_list = []
    product_list = []
    div_list = []
    operations = []
        
    while query=='Y' or query=='y':
        num1 = float(input('Enter a number: '))
        num2 = float(input('Enter a second number: '))
        op = input('''Which Operation would you like to perform on the two
    \t\tnumbers, i.e., +, -, /, *: ''')
        
        #For conditional statements for performing various operation
        if op == '+':
            ops += 1
            operations.insert(ops, op)
            n_add += 1
            add = num1 + num2
            print(f'Sum of the two numbers, {num1} and {num2}, is = {add}')
            add_list.insert(n_add, add)
            

        elif op == '-':
            ops += 1
            operations.insert(ops, op)
            n_diff +=1
            diff = num1 - num2
            diff_list.insert(n_diff, diff)
            print(f'Difference of the two numbers, {num1} and {num2}, is = {diff}')
            

        elif op == '*':
            ops += 1
            operations.insert(ops, op)
            n_product += 1
            product = num1 * num2
            product_list.insert(n_product, product)
            print(f'Product of the two numbers, {num1} and {num2}, is = {product}')
            

        elif op == '/':
            ops += 1
            operations.insert(ops, op)
            n_div += 1
            div = num1 / num2
            div_list.insert(n_div, div)
            print(f'Divion of the two numbers, {num1} and {num2}, is = {div}')
            

        query = str(input('\n\nDo want to perform another calculation? Y/N: '))

    #If query eventually becomes N
    #To print performed calculations
    if ('+' in operations) and (query == 'N' or query == 'n'):
        print(f'The results of the additions you performed are : {add_list}')

    if ('-' in operations) and (query == 'N' or query == 'n'):
        print(f'The results of the subtractions you performed are : {diff_list}')

    if ('*' in operations) and (query == 'N' or query == 'n'):
        print(f'The results of the multiplications you performed are : {product_list}')

    if ('/' in operations) and (query == 'N' or query == 'n'):
        print(f'The results of the divisions you performed are : {div_list}')

    print('Thank you for using my calculator.')    

else:
    print('\nOkay, carry on boss, calculator has been terminated')
