import math
t=int(input())
for _ in range(t):
    a,b,c=input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    aa=math.ceil(a/c)
    bb=math.floor(b/c)

    if(aa>bb):
      print(-1,-1)
    else:
      print(aa,bb)
      
    
