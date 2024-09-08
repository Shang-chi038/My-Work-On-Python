#outer_function: This is a function that defines an inner function that allows change of a variable in the outer function
#from the inner function.

def outer_function():
    outer_variable = 'I am in the outer variable'

    def inner_function():
        nonlocal outer_variable
        #the 'nonlocal-function' is used to change the local scope of outer variable from the innner function to a global
        #scope of the outer function, i.e. from local scope of inner_function to local scope of the outer_function
        #'nonlocal' is just like saying you are not local to only the outer function, you are local to also the nested function.
        outer_variable = 'I am in the inner variable'
        print(outer_variable)

    inner_function()
    print(outer_variable)

outer_function()
