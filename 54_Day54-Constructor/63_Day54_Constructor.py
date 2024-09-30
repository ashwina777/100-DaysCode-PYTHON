class Person:
    def __init__(self,name,o): #parameterized constructor 
        # when only self - default constructor
        print('this is a constructor')
        self.name=name
        self.occ=o
    # name='a'
    # occ="web dev"
    def info(self):
        print(f"{self.name} is a {self.occ}")
a=Person('ashwina','analyst')
print(a.info())     
b=Person('a','manager')
print(b.info())     