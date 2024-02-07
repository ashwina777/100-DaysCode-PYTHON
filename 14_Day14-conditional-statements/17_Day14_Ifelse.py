a = int(input("enter your age : "))
print("your age is : ",a)
# conditional operators
# >,<,>=,<=,==,!=
print(a>18)
print(a<=18)
print(a>=18)
print(a==18)
print(a!=18)
# In python we use indentation to define the scope of the code same as we use {} in java,c,c++ etc
# if statement
if(a>=18):
    print("yes")
    print("you can drive")
print("hi") # this is out of (if)'s scope and will execute even if statement is false

# if-else
if(a>=18 and a<=70): # don't use & operator it refers to bitwise and
    print("yes")
    print("you can drive")
else:
   print("NO")
   print("you cannot drive")