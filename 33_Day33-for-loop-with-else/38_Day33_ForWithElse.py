# the statement in the else block will be excuted after all iterations are completed
for i in range(3):
    # print(f"this is iteration no {i} in for loop")
    print("this is iteration no {} in for loop".format(i+1))
else:
    print("Loop successfully executed")

for i in range(6):
    print(i)
    if i==4:
        break
else:
    print("loop executed/n")
# Since the loop is terminated prematurely, the else block is not executed because
#  it only runs when the loop completes all its iterations without interruption. 

print("-------while loop------")
i=0
while i<5:
    print(i)
    i+=1
    if i==4:
        break
else:
    print("this will not execute")
