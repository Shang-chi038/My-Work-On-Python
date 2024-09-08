#difference(): this is a function that differentiate b/w a global and local variable using the same variable

def difference():
    sth = "Inside the function"
    return sth

sth = "Outside function"
print(difference())
print(sth)
