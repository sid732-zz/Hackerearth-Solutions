t=int(input())
for _ in range(t):
    l,w=map(int,input().split())
    if(l>w):
        print(l//w)
    else:
        print(w//l)
    
