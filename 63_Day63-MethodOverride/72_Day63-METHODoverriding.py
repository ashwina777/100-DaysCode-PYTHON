# redefining parent class method in child class
class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius)
    # def area(self):
    #     return 3.14 *self.radius*self.radius
    def area(self):
        return 3.14 *super().area()

squ=Shape(3,5)
print(squ.area())

c=Circle(5)
print(c.area())