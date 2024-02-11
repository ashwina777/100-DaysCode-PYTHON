# default argument
def average(a=2,b=3):
    print("The average is : ",(a+b)/2)
average(2,3)
average(1) # here b =3 will work
#average(,6) # not correct
# keyword arguments -> providing arg with key = value, order does not matter
average(b=2,a=3) # also possible
average(b=3) # here a = 2 will work

# Required arg -> necessary to pass arg
def average(a,b=3): # here value of a is compulsory
    print("The average is : ",(a+b)/2)
#average(b=4) TypeError: average() missing 1 required positional argument: 'a'
average(6)
average(3.4,6)

# variable length argument
def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum+=i
    # print("Average is ",sum/len(numbers))
    # return 7 -> first return work rest all ignored
    return sum/len(numbers)
c=average(1,2,3,4,5,6,7,8,10)
print("Average is : ",c)

def name(**name):  # dict key-value pair
    print(type(name))
    print("Hello",name["fname"],name["mname"],name["lname"])
name(fname="ashwina",lname="rawat",mname="NA")
