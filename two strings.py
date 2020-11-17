t=int(input())

for i in range(t):
    s1,s2 = input().split()
    s11=sorted(s1)
    s22=sorted(s2)
    if(s11 == s22):
        print("YES")
    else:
        print("NO")
        
