ip=list(input())
vovel = ["A","E","I","O","U","Y"]
boo1=True
boo=True
if(ip[2] in vovel):
    print("invalid")
    boo1=False
else:
    del(ip[2])
    del(ip[5])
    ip = list(map(int,ip))
    
    for i in range(len(ip)-1):
        
        if i==1 or i==4:
            continue
        
        
        
        if( (ip[i]+ip[i+1]) %2 != 0 ):
            boo=False
            
if boo1 != False:
    if(boo==False):
        print("invalid")
    else:
        print("valid")
