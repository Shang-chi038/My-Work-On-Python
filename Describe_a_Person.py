def describe_person(name, age=None):
    if age is None:
        print(f"Your name is {name}.\nYour age not specified.")
    
    elif age == 1:
        print(f"Your name is {name}.\nYou are {age} year old.")

    else:
        print(f"Your name is {name}.\nYou are {age} years old.")


describe_person('Chukwuebuka', 17)