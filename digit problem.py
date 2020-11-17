x,k=input().split()
k=int(k)
x=list(x)

for i in range(len(x)):
    if(x[i]!="9" and k>0):
            x[i]="9"
            k-=1

print("".join(x))
