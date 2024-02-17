# set are unordered,unchangeable and unrepeated(no duplicate items) collection of data items
s={1,2,3,4,5}
print(type(s),s)
s={1,2,1,2}
print(s) # output: {1, 2}
set1={True,"ash","ashwina",1,2.3,3445,234.45}
print(set1)
s={} # <class 'dict'> {} 
print(type(s),s)
# to make empty set
s=set()
print(type(s),s)
for value in set1:
    print(value)