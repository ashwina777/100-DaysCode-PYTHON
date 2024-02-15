# tuples are immutable i.e they cannot be changed
tup=(1,2,3.3,True,"ash")
# tup[0]=90 TypeError: 'tuple' object does not support item assignment
print(type(tup))
tup1=(1) # int type
print(type(tup1)) 
tup2=(1,) #tuple type

print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[-3])
if True in tup:
    print("yes")
else:
    print("no")
#slicing Tuple[start:end:jumpIndex]
tup3 =tup[1:4]
print(tup3)
print(tup[:]) # -> tup[0:len(tup)]