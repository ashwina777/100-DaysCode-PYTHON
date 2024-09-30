class Employee:
    def __init__(self,name):
        self.name=name
    def showDetails(self):
        print(f"The name of the Employee is {self.name}")

emp1=Employee("ashwina")
emp1.showDetails() #if not self TypeError: showDetails() takes 0 positional arguments but 1 was given
Employee.showDetails() #error same TypeError