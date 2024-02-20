# custom error can be raised using raise keyword
a = input("Enter any value between 1 to 10 : ")
# python also handles error by itself
# e.g entering string value in a -> ValueError: invalid literal for int() with base 10: 'ashwina'
if(a=='quit'):
    print("no error")
elif(int(a)>11 or int(a)<0 ):
    raise ValueError("Value should be between 1 to 10")
else:
    print(f"You entered {a}")

# Defining custom Errors -> we can define custom exception by creating a new class 
# that is derived from the built-in Exception class.
