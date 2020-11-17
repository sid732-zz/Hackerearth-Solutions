t=int(input())
def isprime(n):
        for x in range(2,n):
            if(n % x==0):
                return False
        return True
                
def low(no):
    for k in range(no,64,-1):
                if(isprime(k)):
                    return k
                    break

    
def high(no):
    for k in range(no,123):
                if(isprime(k)):
                    return k
                    break
    

for i in range(t):
    ans=""
    n=int(input())
    string=input()
    for j in range(len(string)):
        no=ord(string[j])
        if(no<65):
            ans+="C"
            continue

        if isprime(no):
            ans+=string[j] 
        else:
            if(no==65):
                b=high(no)
                ans+=chr(b)
            elif(no==122):
                b=low(no)
                ans+=chr(b)
            
            
            else:
                a=low(no)
                b=high(no)
                if(a==None):
                        ans+=chr(b)
                if(b==None):
                        
                        ans+=chr(a)
                if(a!=None) and(b!=None):
                        if(abs(no-a) < abs(no-b)):
                            ans+=chr(a)
                        if(abs(no-a) > abs(no-b)):
                            ans+=chr(b)
                        if(abs(no-a) == abs(no-b)):
                            ans+=chr(a)
                
    print(ans)
            

        
        
        
