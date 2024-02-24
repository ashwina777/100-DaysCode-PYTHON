def greet():
    print("Hello dear!")
print(__name__)
if __name__ == "__main__":
    greet()
# if __name__== "__main__" is used to avoid the execution of the code in the imported file
# we use it in the module which can be imported at a later time