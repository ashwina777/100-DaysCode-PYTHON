# for loops can iterate over a sequence of iterable objects in python
name = "ashwina"
for i in name:
    print(i,end="-")
    if(i=="w"):
        print("This is a special alphabet!\n")
print("\n")
colors = ["Red","green","blue","yellow","violet"]
for color in colors:
    print(color)
    for c in color:
        print(c)

for i in range(5): # 0 to 4
    print(i)
for i in range(0,101): # 0 to 100
    print(i)
# range(start,stop,jump) has 3 args start, stop and jump (skips)
for i in range(3,32,3):
    print(i)