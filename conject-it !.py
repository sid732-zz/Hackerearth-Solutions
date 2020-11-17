t = int(input())
for i in range(t):
    n=int(input())
    a=n
    for i in range(10000000):
        if(a%2==0):
           a=a//2
           if(a==1):
               break
        if(a%2 != 0):
            a=(3*a)+1
            if(a==1):
                break
    if(a==1):
        print("YES")
    else:
        print("NO") 
