a=input()

z=0
o=0
for i in range(len(a)):
    if a[i]=="z":
        z+=1
    if a[i]=="o":
        o+=1

if z*2==o:
    print("Yes")
    
