def greet(fx):
    def mfx(*args,**kwargs):
        print("good Morning!\t-------decorator-------")
        fx(*args,**kwargs)
        print("----------thanks for using this function-----END")
    return mfx
# @greet
def hello():
    print("Hello World!! MAIN FUNCTION")
# @greet
def add(a,b):
    print(a+b)
# hello()
# OR
greet(hello)() #remove @greet then 
greet(add)(1,2) # compulsory use-> *args,**kwargs