# nested if statements
num = int(input("Enter a number : "))
if(num<0):
    print("number is negative")
elif(num>0):
    if(num<=10):
        print("Number is between 1-10")
    elif(num>10 and num<=50): # use and not '&'
        print("Number is between 11-50")
    else:
        print("Number is greater than 50")
else:
    print("number is 0")