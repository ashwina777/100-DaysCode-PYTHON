# finally code block is also part of exception handling
# The finally block is always executed
def func(i):
    try:
        l=[123,22,39,42,51]
        # i=int(input("Enter the index: "))
        print(f"elememt at index {i} is {l[i]}")
        return 0
    except:
        print("Error occured")
        return 1
    finally:
        print("whether the control goes to try/catch..")
        print("Finally is always executed") 
    print("Hello world") #this does not print because this is not in identation with finally block
func(0)
func(1)
func(3)
func(5)
func(7)
'''
We see the main utility of finally in functions ..
In the above code "Hello World" is not executed because values are returned in try and except block.
In such scenarios we use finally for the statement we want to definitely execute 
irrespective of whether the flow of control is in try or except block'''