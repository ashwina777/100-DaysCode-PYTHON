class Person:
    name='ashwina'
    occupation='student'
    networth=343498
    def info(self):
        print(f"{self.name} is a {self.occupation} and has net worth {self.networth}\n")
a=Person()
# print(a.name)
# print(a.occupation,a.networth)
a.info()
a.name='t123'
a.occupation='data scientist'
a.info()
b=Person()
b.name="ash"
b.occupation="HR"
b.networth=340000 
b.info()