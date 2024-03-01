f=open('myfile.txt','r') # to open file in read mode,it must be present in folder
f=open('myfile.txt','rt') # read as text default 
f=open('myfile.txt','rb') # binary content
print(f)
text=f.read()
print(text) #b'Hello this is a text file.\r\nI am Ashwina and i am learning python..'
f.close()
f=open('myfile.txt','w')
f.write("opened existing file in write mode") # overwritten
f.close()
f1=open('myfile2.txt','w')  # creates file
# text=f1.read() # io.UnsupportedOperation: not readable
# directly reading a file that is opened in write mode is wrong
f1.write("Hello this is file 2 created by ASHWINA.")
f1.close()
f1=open('myfile2.txt','a') # append hello world only once
f1.write("\nHELLO WORLD!")
f1.close()
f2=open('file1.txt','a') # it will keep appending text as many times we run the file
f2.write("Hello world\n")
f2.close()
with open('myfile.txt','a') as f:
    f.write("\nI am inside with...")
# various modes in python
# read(r) [default mode]
# write(w)
# append(a)
# create(x)
# text(t)
# binary(b)