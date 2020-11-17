n=int(input())
a=list(input().split())
a1=a[0:n//2]
a2=a[n//2:n]
no=""
for i in range(len(a1)):
    temp=a1[i]
    for j in range(1):
        no= no + temp[j]
for i in range(len(a2)):
    temp=a2[i]
    for j in range(1):
        no= no + temp[-1]
        
no=int(no)
if(no%11==0):
    print("OUI")
else:
    print("NON")
    
