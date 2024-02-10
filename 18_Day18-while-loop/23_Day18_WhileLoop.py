# keep entering value until value is more 38
i=int(input("Enter a number "))
while(i<=38):
    i=int(input("Enter a number "))
    print(i)
    i=i+1

#decrementing while loop
count = 5
while(count >= 0):
    print(count)
    count=count-1

# else with while loop
count = -5
while(count >= 0):
    print(count)
    count=count-1
else:
    print("i am inside else block") 

# emulate do-while loop
flag = True
while flag:
    print("trying to emulate do-while loop")
    user_input = input("do you want to continue... true/ false : ")
    if user_input.lower() == "false":
        flag = False
'''
flag=bool(input("do you want to continue... true/false"))

The bool() function converts its argument to a Boolean value. 
When you input any non-empty string (such as "false" or "True"), bool() will return True. 
This is because any non-empty string in Python is considered True.
'''
flag = bool(input("Enter a boolean value "))
print(flag)
# as above explaination states : even if we enter a false value it will display it as true