x=8 #global var
print(x)
def hello():
    x=9 #local var
    y=10
    print(f"The local x is {x}")
    print("Hello world!")
    # local variable is destroyed when function returns/exits
hello()
print(f"The global x is {x}")
# print(f"The local y is {y}") #NameError: name 'y' is not defined

def myFunc():
    global x  # global keyword is used to change the value of global variable
    x=45
    print(x)
print(x) # here x=8
myFunc()
print(x) # here x=45 after calling function the global value is changed
