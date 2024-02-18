# dictionaries are ordered(python 3.7 onwards) key value pair type data
info={'name':"ashwina",'age':20,'CanVote':"yes"}
print(type(info),info)
print(info['name'])
# print(info['course']) # KeyError: 'course' throws error
print(info.get('name'))
print(info.get('course')) #doesn.t throw error if key does not exits
print(info.keys())
print(info.values())
for key in info.keys():
    print(info[key])
    print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items()) 
for key,value in info.items():
    print(f"The value corresponding to the key {key} is {info[key]}")