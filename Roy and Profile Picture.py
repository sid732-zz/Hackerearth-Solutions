L=int(input())
N=int(input())
for i in range(1,N+1):
    W,H=input().split()
    W=int(W)
    H=int(H)
    
    if(W < L or H < L):
        print("UPLOAD ANOTHER")
    else:
        if((W >= L and H >= L)and(W==H)):
            print("ACCEPTED")
        else:
            print("CROP IT")

