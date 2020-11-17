import math
t=int(input())
for i in range(t):
    
    a,b,c=input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    if((b-a)==(c-a)):
        print(0)
    else:
        d=math.ceil(abs((b-a)-(c-b))/2)
        print(d)

    
