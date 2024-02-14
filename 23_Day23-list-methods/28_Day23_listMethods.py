l=[12,34,56,2,1,2,2.3]
print(l)
# l.append("ash") -> sorting does't work on string
l.append(34.23)
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)
print(l.index(2)) # returns first occurence of item
print(l.count(2))
m=l # remember both point to same reference
m[0] = 0
print(l)
n = l.copy()
n[0]=123
print(l)
l.insert(2,3443)
print(l)
p=[100,200,300,400,500]
l.extend(p) #p's elements will be added to l
print(l)
q=p+l
print(q)