n=int(input())
a=0
for i in range(n):
    a=a+i
    if(a>=n):
        print("Patlu")
        break
    a=a+i*2
    if(a>=n):
        print("Motu")
        break

