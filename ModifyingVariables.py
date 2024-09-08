#function(): this is a function that allows the modifying of a global variable inside it, with the 'global' keyword.

variable = 'I am outside the function.'
print(variable)

def function():
    global variable
    variable = 'I am inside the function.'
    return variable

print(function())
