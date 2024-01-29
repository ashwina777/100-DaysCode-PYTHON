a=12786876
a1=875.8
print(a)
b="ashwina"
print(b)
c = True
d = None
e=complex(3,6)
# print(a+b) error int + str X
print(a+a1)
print("The datatype of a is ",type(a))
print("The datatype of a1 is ",type(a1))
print("The datatype of b is ",type(b))
print("The datatype of c is ",type(c))
print("The datatype of d is ",type(d))
print("The datatype of e is ",type(e))

# other datatypes
list1=[8,2.3,[4,5],['apple','orange']] #collection of different data elements (mutable)
print("List is :",list1,type(list1))
tuple1 = ("parrot","sparrow",("Lion",'Tiger'))
print("Tuple(immutable) is :",tuple1,type(tuple1))
dict1={"name":"ashwina","age":20,"canVote":True} # dictionary is collection of key-value pairs
print(dict1,type(dict1))