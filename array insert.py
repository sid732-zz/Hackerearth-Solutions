a,q=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(q):
    a,b,c=map(int,input().split())
    if(a==1):
        arr[b]=c
    if(a==2):
        print(sum(arr[b:c+1]))
