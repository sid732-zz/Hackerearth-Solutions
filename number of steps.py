n = int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

minn=min(a)
steps=0
for i in range(n):
    if((a[i]>minn)):
        for j in range(n):
            if(a[i] > minn ):
                steps=steps+1
                a[i]=a[i]-b[i]             
if(max(a)!=min(a)):
   for i in range(n):
    if((a[i]>=minn)):
       
                steps=steps+1
                a[i]=a[i]-b[i]
                
if(max(a)==min(a)):
    print(steps)
else:
    print(-1)




