path1="lemontree.txt"
f1=open(path1,'r')
for line1 in f1.readlines():
    newline1=line1.rstrip()
    newwords1=newline1.split(",")
    print(newwords1)
f1.close()
