with open('myfile2.txt','r') as f :
    print(type(f))
    f.seek(7) #specify postition
    print(f.tell()) #tells the seek or position from where reading will start
    data=f.read(10)# specify the number of character to be read
    print(data)

with open('file.txt','w') as f:
    f.write("hello world this is ashwina")
    # f.truncate(5)
    # truncate to n characters 
with open('file.txt','r') as f:
    print(f.read())