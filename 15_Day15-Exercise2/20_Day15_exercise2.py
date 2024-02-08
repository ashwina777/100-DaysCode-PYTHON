# Exercise 2 : Good Morning Sir
# Create a python program capable of greeting you with GoodMorning,Good afternoon and Good Evening.
# Your program should use time module to get the current hour.

import time
# TimeStamp1 = time.gmtime()
# print(TimeStamp1)
# TimeStamp2 = time.localtime()
# print(TimeStamp2)

timenow = time.strftime("%H:%M:%S")
print("current time :",timenow)
timenow=int(time.strftime("%H"))
#print(timenow)
if(timenow >=4 and timenow<12):
    print("Good Morning!")
elif(timenow>=12 and timenow<16):
    print("Good Afternoon!")
elif(timenow>=16 and timenow <21):
    print("Good Evening!")
else:
    print("Good Night!")