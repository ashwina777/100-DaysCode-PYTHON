# public : all variables are accessible  (default modifier)
# private : cannot (but still can be used indirectly) use outside class ' __ ' double underscore used
# protected : accessible within class and with subclass ('_')
class Employee:
    def __init__(self):
        self.__name="ashwina"
    def _funName(self):
        return "Protected"
a=Employee()
# print(a.__name) cannot be accessed directly
print(a._Employee__name) # name mangling - used to protect class private and superclass private attr from accidently being overwritten by subclass
print(a.__dir__()) # list of all the method that can be used on a
print(a._funName())
# print(dir(a))