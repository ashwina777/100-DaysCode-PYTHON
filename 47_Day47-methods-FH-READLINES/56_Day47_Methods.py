f=open('myfile.txt','r')
i=0
per=0.0
while True:
    i=i+1
    line=f.readline()
    if not line:
        print(line,type(line))
        break
    m1=int(line.split(",")[0])
    m2=int(line.split(",")[1])
    m3=int(line.split(",")[2])
    print(f"Marks of student {i} in maths is : {m1}")
    print(f"Marks of student {i} in science is : {m2}")
    print(f"Marks of student {i} in SST is : {m3}")
    per=((m1+m2+m3)//3)
    print(f"Percentage of student {i} : {per}(approx.)")
    print(line)

    # writelines() method
f=open('myfile2.txt','w')
lines=['line1\n','line2\n','line3\n']
f.writelines(lines)
f.close()