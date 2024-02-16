# DocStrings are the string literals that appear right after the definition of a function,method,class or module.
def square(n):
    '''Takes in a number n,
    returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)

# remember DocString comes just after function. Following is not a DocString
def square(n):
    print()
    '''Takes in a number n,
    returns the square of n'''
    print(n**2)
print(square.__doc__) # output : None

# PEP 8 -> Pythom Enhancement Proposal 
# it is a document that provide guidelines and best practices on how to write Python code.

