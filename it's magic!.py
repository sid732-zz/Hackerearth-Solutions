n=int(input())
index=-1
arr1=list(map(int,input().split()))
arr=sorted(arr1)

a=sum(arr)
for i in range(n):
    if((a-arr[i]) % 7 == 0 ):
        index=arr[i]
        break

if(index == -1):
    print(index)
else:
    print(arr1.index(index))
    
