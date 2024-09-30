#  map
def cube(x):
    return x*x*x
print(cube(4))

newl1=[]
l=[1,2,3,4,5]
for item in l:
    newl1.append(cube(item))
print(newl1)

newl2=[]
newl2=list(map(cube,l))
print(newl2)

# with lambda function
newl2=list(map(lambda x: x*x*x,l))
print('with lambda : ',newl2)
#filter
def filter_func(a):
    return a>3
# function in filter must return true or false -> if true it will be appended to list else not
newl3=list(filter(filter_func,l))
print(newl3)

# reduce (import)
from functools import reduce
num=[1,2,3,5]
sum=reduce(lambda x,y : x+y,num)
print(sum)