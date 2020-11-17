
N = int(input())
data = [x for x in input().split()]
b=""
for i in range(N):
    a=data[i]
    for j in range(1):
        b=b+a[len(a)-1]
b=int(b)
if(b%10==0):
    print("Yes")
else:
    print("No")

