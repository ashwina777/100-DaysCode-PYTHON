# string slicing
names="ashwina,avantika,bhumika,shubham,virat"
name="ashwina"
print(len(names))
print(names[0:5]) # 0-4 index ashwi (include 0 not 5)
print(names[:5])   # python applies 0 by default here
print(names[2:5]) # include index 2,3,4
print(names[:])   # all index
print(names[2:-4]) # negative slicing here -> 2 : len(names)-4
print(names[2:len(names)-4]) # equivalent to above
print(names[-2:len(names)-4]) # len(names)-2:len(names)-4 = 36:34 X
print(names[-4:len(names)-2]) # len(names)-2:len(names)-4 = 34:36 
print(names[-16:len(names)-24])
print(names[-24:len(names)-16])
print(name[-2:-1])
#print(names[2-5]) # 

# quick quiz
word = "apple"
print(word[-4:-2])

# output 
# word[5-4 : 5-2] -> word[1:3] -> index 1,2 = pp (OUTPUT)

# string multiplication
greeting = "Hello "
repeat_greeting = greeting * 3
print(repeat_greeting)  # Output: Hello Hello Hello 