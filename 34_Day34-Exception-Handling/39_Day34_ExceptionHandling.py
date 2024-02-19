a = input("Enter the number : ")
print(f"Multiplication table of {a} is : ")
try:
    for i in range(1,11):
       print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)
    print("Invalid Input!!")
print("If error occur this code will not run")
print("Therefore we use exception handling to handle unexpected errors and maintain normal flow of program")

try:
    num=int(input("Enter an integer : "))
    a=[3,6]
    print(a[num])
except ValueError:
    print("Number entered is not an integer...")
except IndexError:
    print("Index Error...")