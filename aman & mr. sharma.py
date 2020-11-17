t=int(input())
toffee=0
for i in range(t):
    
    r,x=map(int,input().split())
    if((22/7)*r*2 <= x*100 ):
        toffee = toffee +1
print(toffee)
