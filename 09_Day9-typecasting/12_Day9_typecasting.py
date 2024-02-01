# typecasting is changing one data type to other data type
# for typecasting we use various functions like int(),float(),str(),ord(),hex(),oct(),tuple(),set(),list(),dict(), etc.
a = '1'
b = '2'
n = 'a'
print(a+b) # performing concatenation of strings
print(int(a)+int(b)) # convert only for valid string (explicit typecasting)
# print(int(a)+int(b)+ int(n)) # error

#implicit typecasting - performed by python automatically

a1=34
print(type(a1))
b1=45.6
print(type(b1))
print(a1+b1) #implicit conversion