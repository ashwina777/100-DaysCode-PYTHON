import time 
# from time import localtime
print(dir(time))
# print(time.localtime,type(time.localtime))
# print(time.gmtime,type(time.gmtime))
a=time.localtime()
print(a)
# a=time.gmtime()
# print(a)
def greet():
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
        