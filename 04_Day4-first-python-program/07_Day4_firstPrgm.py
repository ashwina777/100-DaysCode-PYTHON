# DIFFERENT PRINT STATEMENTS
print("Hello World")
print(5)
print(5 + 3)
print(3.14)
print("Bye" + "World")
print("Bye", "World")
print("Bye" + "World", 5)
print
print("Bye" + "World", 5, 3.14)
print("Bye" + "World", 5, 3.14, sep="---")
print("Bye" + "World", 5, 3.14, sep="---", end="***")
print("Bye" + "World", 5, 3.14, sep="---", end="***\n")

"""
---output---
Hello World
5
8
3.14
ByeWorld
Bye World
ByeWorld 5
ByeWorld 5 3.14
ByeWorld---5---3.14
"""