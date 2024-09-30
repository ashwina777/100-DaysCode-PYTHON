# is and == are both comparison operators 
# is compare location while == compare the values
a = 4
b = '4'
c=4
print(a is b) # compares location
print(a is c) #here location is also same as it is a constant(immutable)
print(a==b)
print(a==c)
a=(1,2)
b=(1,2)
print(a is b) # returns true because tuples are immutable and thus refer to same address
a=[1,2]
b=[1,2]
print(a is b) # mutable so different memory location is used