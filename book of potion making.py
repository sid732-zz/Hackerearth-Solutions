ip = list(map(int,input()))

if(len(ip) !=10):
    print("Illegal ISBN")
    exit()
    
summ=0
for i in range(len(ip)):
    summ = summ + ((i+1) * ip[i])

if summ%11==0:
    print("Legal ISBN")
else:
    print("Illegal ISBN")
