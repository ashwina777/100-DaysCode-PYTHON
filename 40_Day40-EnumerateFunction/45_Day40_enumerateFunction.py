a=[34,2,45,67,98,67,75]
index=0
for mark in a:
    print(mark)
    if(index==4):
        print(f"Topper : roll no {index+1} marks {mark}")
    index+=1
# enumerate function is a built-in function that allows us to loop over a sequence(list,tuple or str)
# and get the index and value of each element in the sequence
print("Using enumerate:")
for index,mark in enumerate(a): # first variable store index second variable store value ..
    print(mark)
    if(index==4):
        print(f"Topper : roll no {index+1} marks {mark}")
print("------------------------------")
for index in enumerate(a):
    print(index)
    print(mark)
print("------------------------------")
for index,mark in enumerate(a):
    print("index : ",index ," ->  mark : ",mark)
print("------------------------------")
for index,mark in enumerate(a,start=2):
    print("index : ",index ," ->  mark : ",mark)