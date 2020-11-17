from collections import Counter
t=int(input())
for i in range(t):
    a=input()
    b=input()

    c=Counter(a)
    d=Counter(b)

    ans=c & d

    ans1=list(ans.elements())
    final=''.join(ans1)
    length=len(final)
    print((len(a)-length)+(len(b)-length))
'''
n=int(input())
for _ in range(n):
    s1=list(input())
    s2=list(input())
    d=0
    m=len(s1)+len(s2)
    l1=set(s1).intersection(set(s2))
    for i in l1:
        d=d+min(s1.count(i),s2.count(i))
    print(m-2*d)
'''
