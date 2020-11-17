z = ['h','a','c','k','e','r','e','a','r','t','h']
n = int(input())
inp = input()
inp = list(inp)

H = inp.count('h')
A = inp.count('a')
E = inp.count('e')
R = inp.count('r')
C = inp.count('c')
K = inp.count('k')
T = inp.count('t')

count=0
while (H>=2 and A >=2 and E >=2 and R>=2 and C>=1 and K >=1 and T>=1):
    count = count+1
    H = H - 2
    A = A - 2
    E = E - 2
    R = R - 2
    C = C - 1
    K = K - 1
    T = T - 1

print(count)
