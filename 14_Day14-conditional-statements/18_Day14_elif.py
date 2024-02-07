# elif statement is used when we have to check multiple conditions
applePrice = 20
budget = 200
if(budget - applePrice >50):
    print("Siri, add 2 kg apples to the cart")
elif(budget-applePrice > 20):
    print("Siri, add 1 kg apples to the cart")
else:
    print("Siri, remove apples from the cart")

# example 2
num = int(input("enter a number : "))
if(num<0):
    print("negative")
elif(num>0):
    print("positive")
else:
    print("zero")
print("num check completed")