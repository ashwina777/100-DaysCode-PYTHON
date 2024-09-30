# one child having multiple parents
class Employee:
    def __init__(self,name):
        self.name=name
        # print(self.name)
        print(name)
    def show(self):
        print('Name is : ',self.name)
class Management:
    def __init__(self,Deptname):
        self.dname=Deptname
        print('management department',self.dname)
    def show(self):
        print('The management department team is :',self.dname)
class Organisation(Employee,Management):
    def __init__(self,name,dname):
        self.name=name
        self.dname=dname
        print(name)
        print('management department',self.dname)
org=Organisation('ashwina','team1')
org.show() # whichever class is inherited first it's function will be called first
print(org.dname)
print(org.name)
e=Employee('ashwina')
print(Organisation.mro()) # tells where will be methods searched linewise