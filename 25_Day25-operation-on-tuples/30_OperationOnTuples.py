#  tuples are immutable if you wamt to add,remove or change tuple items , then first you must convert tuple to list.
# Then perform operations on that list and convert it back to tuple.
names=("ashwina","arti","mahak","eshika")
temp=list(names)
temp.append("ashwina rawat")
temp.pop(1)
temp2="ramesh"
names=tuple(temp)
print(names)
names2=("a","b","c","d")
nm=names+names2
print(nm)
print(names.count("ashwina")) # output - 1
tuple=(1,2,3,4,3,2,5,6,3,4,2,5,6,7,8,22,2)
print(tuple.count(2))
print(tuple.index(2)) # returns index of first occurence
print(tuple.index(2,2,-3)) # index(value,start,stop)->start,stop slice the tuple
print(len(tuple))