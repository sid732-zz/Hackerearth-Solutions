t=int(input())
for i in range(t):
    sh,sm,eh,em = map(int,input().split())
    hr=eh-sh
    mn=em-sm
    
    if( mn < 0):
        hr=hr-1
        mn=60+(mn)
        print(hr,end=" ")
        print(mn)
    else:
        print(hr,end=" ")
        print(mn)
