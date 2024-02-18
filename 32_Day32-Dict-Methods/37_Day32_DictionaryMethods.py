emp1 = {101:"ashwina",102:"mahak",103:"arti",104:"eshika"}
emp2= {110:"a",111:"b",112:"c"}
emp1.update(emp2)
print(emp1)
print(emp2)
emp2.clear()
print(emp2)
empt={}
print(empt) # empty dictionary
emp1.pop(111)
# emp1.pop("a") #argument can be only key -> KeyError: 'a'
print(emp1)
emp1.popitem() # removes last item
print(emp1)
 
del emp1[110]
print(emp1)
del emp1
print(emp1) # delete full dictionary if key is not provided