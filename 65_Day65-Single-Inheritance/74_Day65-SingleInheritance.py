# single parent class
class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def make_sound(self):
        print("sound..")
class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species='dog')
        self.breed=breed
    def make_sound(self):
        print("woof woof!!")
dg=Dog('sandy','pitbull')
dg.make_sound()
a=Animal("hippo",'NA')
a.make_sound()