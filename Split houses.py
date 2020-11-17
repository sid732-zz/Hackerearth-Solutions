n=int(input())
str=input()
boo=True
s=list(str)   
for i in range(1,n+1):
    if(i != n): '''sometimes n-1'''

        if((s[i]=="H")and (s[i+1]=="H") ):
            boo=False
            break
        
     

if(boo==False):
    print("NO")

else:
    print("YES")
    for i in range(n):
        if(s[i]=="."):
            s[i]="B"
    print("".join(s))
