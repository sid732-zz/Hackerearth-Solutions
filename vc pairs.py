vovel='aeiou'
t=int(input())

for i in range(t):
    n=int(input())
    string=input()
    
    count=0
    for i in range(0,len(string)-1):
        
        if((string[i] not in vovel) and (string[i+1] in vovel)): 
            count=count + 1
    if(count!=0):
        print(count)
    else:
        print(0)
