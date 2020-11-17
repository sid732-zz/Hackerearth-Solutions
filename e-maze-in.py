string=input()
a=0
b=0
for i in range(len(string)):
    if(string[i] == "L"):
        a=a-1
    if(string[i] == "R"):
        a=a+1
    if(string[i] == "U"):
        b=b+1
    if(string[i] == "D"):
        b=b-1
print(str(a)+ " "+str(b))

    
