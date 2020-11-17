ip=int(input())
summ=0
while ip!=0:
    if(ip>5):
        ip=ip-5
        summ=summ+1
    else:
        ip=ip-ip
        summ=summ+1

        
if(ip<5 and ip!=0):
    summ=summ+1
print(summ)
