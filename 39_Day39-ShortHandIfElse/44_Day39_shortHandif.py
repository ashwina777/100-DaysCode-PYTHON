# shorthand syntax can be a convenient way to write simple if-else statements
# especially when you want to assign a value to a variable based on a condition
a=342
b=346
print("a = ",a) if a>b else print("=") if a==b else print("b = ",b)
print(100) if b>a else ""
c=9 if b<a else 0
print(c)
c=9 if b>a else 0
print(c)
# it's not suitable for complex situations where we need to execute multiple statements