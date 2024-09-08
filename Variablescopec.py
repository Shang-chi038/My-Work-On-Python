#keyword(): this is a function that illustrate the use of keyword arguments and mix positional argument

def keyword(name = 'Mr. Frank', greeting = 'Good morning', question = 'How was your night?'):
    concatenate = (f'{greeting}, {name}. {question}')
    return concatenate

output1 = keyword()
print(output1)
#You can call this function like that

output2 = keyword(question = 'How are you doing?', greeting = 'Good afternoon', name = 'Mr Chukwuebuka')
print(output2)
#You can modify the variables in the function using their keywords

output3 = keyword('Mr Chukwuebuka', 'Good afternoon')
print(output3)
#Or you can modify the variables in the function without their key words

output4 = keyword('Mr Chukwuebuka', greeting = 'Good afternoon', 'How are you doing?')
print(output4)
#Note if you use the keyword argument along the way, you must mention the preceeding keywords even if you are not
#modifying the variables. To solve the error, add 'question =' before 'How are you doing?'.
