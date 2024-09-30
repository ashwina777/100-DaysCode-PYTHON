class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod # used as alternative constructors
    def fromStr(cls,string):
        return cls(string.split('-')[0],int(string.split('-')[1]))
e1=Employee("ashwina",3434345)
print(e1.name)
print(e1.salary)
string="ashwina-34435"
e2=Employee(string.split('-')[0],int(string.split('-')[1]))
print(e2.name)
print(e2.salary)
e3=Employee.fromStr(string)
print(e3.name)
print(e3.salaryf)