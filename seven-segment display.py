li=[6,2,5,5,4,5,6,3,7,6]
t = int(input())
for i in range(t):
    
    sticks=0
    ip=list(map(int,input()))
    for j in range(len(ip)):
        sticks=sticks+li[ip[j]]
    if(sticks%2==0):
        print("1"*(sticks//2))
    else:
        print("7"+"1"*((sticks-3)//2))
        
