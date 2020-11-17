T=int(input())
A=0
B=7

for i in range(1,T+1):
    call=int(input())
    liftA=abs(call-A)
    liftB=abs(call-B)
    if(liftA < liftB):
        print("A")
        A=call
    if(liftA > liftB):
        print("B")
        B=call
    if(liftA == liftB):
        if(A < B):
            print("A")
            A=call
        if(A > B):
            print("B")
            B=call
