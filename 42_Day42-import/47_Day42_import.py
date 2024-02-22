import math
from ashwina import greet,a
# print(math.sqrt(2))
# print(math.pi * math.sqrt(4))

# from math import * -> will work but not recommended
# import math as m # this will work
from math import sqrt,pi,pow # importing specific functions
from math import cos as c
# from math import sin,tan as s,t -> X
print(sqrt(9))
print(pi)
print(pow(2,5))
print(c(1))

print(dir(math))
print(math.nan,type(math.nan))

print("-----------------------------------------")
print("Self created module : ")
greet()
print(a)