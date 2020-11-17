U="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
L="abcdefghijklmnopqrstuvwxyz"
N="0123456789"
string=""
ip=input()
cp=int(input())
for i in range(len(ip)):
    if(ip[i] in U):
        a= U.index(ip[i])+cp
        if(a>=26):
           string+=U[a%26]
        else:
            string+=U[a]
    if(ip[i] in L):
        a= L.index(ip[i])+cp
        if(a>=26):
           string+=L[a%26]
        else:
            string+=L[a]
    if(ip[i] in N):
        a=N.index(ip[i])+cp
        if(a>10):
            string+=N[a%10]
        else:
            string+=N[a]
    if((ip[i] not in U) and (ip[i] not in L) and (ip[i] not in N) ):
        
        string+=ip[i]
print(string)

        


