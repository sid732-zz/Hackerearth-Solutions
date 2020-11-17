
T=int(input())

for i in range(T):
    a=int(input())
    b=a%12    


    if(b ==0):
        print(str(a-11) +" WS")

    if(b>=1 and b<=6):
        temp= 12-(b+(b-1))    
        print(str(a+temp),end="")

    if(b>=7 and b<=12):
        temp=b-((12-b)+1)
        print(str(a-temp),end="")

    if(b==1 or b==6 or b==7):
        print(" WS")
    if(b==2 or b==5 or b==8 or b==11):
        print(" MS")
    if(b==3 or b==4 or b==9 or b==10):
        print(" AS")
    
