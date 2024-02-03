name = "ashwina"
course ='BCA'
greet1='she said "hello everyone"'
greet2="she said \"hello everyone\""
greet3="she said 'hello everyone'"
print("Hello"+name,"course"+course)
print("Hello",name,"course",course)
print(greet1,"\n",greet2,"\n",greet3)

# multi line string literal
greet='''hello sir/mam.
how are you doing?
Is everything alright?'''
print(greet)

print(name[0],name[1])
# print(name[7]) -> IndexError: string index out of range 
for i in greet:
    print(i)

# string multiplication
greeting = "Hello "
repeat_greeting = greeting * 3
print(repeat_greeting)  # Output: Hello Hello Hello 
