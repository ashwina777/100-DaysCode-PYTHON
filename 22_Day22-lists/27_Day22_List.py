# list are ordered collection of data items
# they store multiple items in a single variable
l=[3,2.5,5,[2,3,4],"ashwina",True]
# print(l)
# print(type(l))
# print(l[0])
# print(l[2])
# print(l[3])
# print(l[3][0])
# print(l[3][2])
# print(l[4])
# # print(l[4]) -> IndexError: list index out of range

# # negative indexing
# print(l[-3]) # third last element -> len(l)-3
# print(l[len(l)-3])
# print(l[6-3])

# if "ashwina" in l:
#     print("yes")
# else:
#     print("no")
# #same applies for strings as well
# if "ashwi" in "ashwina rawat":
#     print("yes")
print(l[:]) #python automatically puts-> len[0:len(l)] 
print(l[:1]) # python -> l[0:1]
print(l[1:-1])
print(l[1:4]) #slicing-> [start:end:jump]
print(l[0:5:2])

#list comprehension
lst=[i for i in range(4)]
print(lst)
lst2=[i*2 for i in range(0,4)]
print(lst2)
lst2=[i*i for i in range(2,20) if i%2==0]
print(lst2)