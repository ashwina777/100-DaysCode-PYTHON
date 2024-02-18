# union || intersection || difference
s1={1,4,3,6,7,45.3}
s2={2,3,4,6,7,1,89,4}
print(s1.union(s2)) # this does not update values
print(s1,s2)
s1.update(s2) # this update a set with union of itself and others
print(s1) # {1, 2, 3, 4, 6, 7, 45.3, 89}
s1={1,4,3,6,7,45.3}
s2={2,3,4,6,7,1,89,4}
print(s1.intersection(s2)) # intersection -> common elements
print(s1,s2)
s1.intersection_update(s2)
print(s1,s2)
s1={1,4,3,6,7,45.3,10}
s2={2,3,4,6,7,1,89,4}
print(s1.symmetric_difference(s2)) # print elements of uncommon elements
print(s1.difference(s2)) # prints elements of s1 that are not present in s2
print(s2.difference(s1)) # prints elements of s2 that are not present in s1
s1.symmetric_difference_update(s2) # updating the uncommon elements in s1
print(s1)

# isdisjoint() || issuperset() || issubset()
# disjoint set are those set which have nothing in common
s1={1,2,3,4}
s2={4,5,6,8,7}
print(s1.isdisjoint(s2))
s1={1,2,3,4,5}
s2={1,2}
print(s1.issuperset(s2)) # s1 has all the elements of s2 thus it is a superset
print(s2.issubset(s1)) # s2 is subset of s1

# add() || update() || remove()/discard()
money_heist={"tokyo","berlin","helsinki","denver"}
money_heist.add("madrid") # adds single item
print(money_heist)
#update add more than 1 item can add list, tuple or dictionary to set 
lst=[1,2,3,"rio"]
tup=("nairobi","oslo")
print(type(tup))
money_heist.update("moscow")
money_heist.update(lst,tup)
print(money_heist)

# main difference between remove and discard is that remove() raises error 
# if element is absent in set while discard does not raise error
# money_heist.remove("abc") #KeyError: 'abc'
money_heist.discard("abc")
money_heist.remove("oslo")
print(money_heist)
money_heist.pop() # removes random elemnt from set
money_heist.pop()
print(money_heist)

if "tokyo" in money_heist:
    print("yay!")
else:
    print("Noo!")

del money_heist # delete full set
print(money_heist) # NameError: name 'money_heist' is not defined 