class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showDetails(self):
        print(f"Name of Employee (id:{self.id}) is {self.name}")
class Programmer(Employee):
    def showLanguage(self):
        print("The default language is PYTHON!")
e1=Employee('ashwina',400)
e1.showDetails()
e2= Employee('ABC',401)
e2.showDetails()
# e2.showLanguage() error
p1=Programmer("AHSWINA",402)
p1.showDetails()
p1.showLanguage()