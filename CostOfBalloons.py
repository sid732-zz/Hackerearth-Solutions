from array import *
TestCases=int(input())

for Test in range(TestCases):
    GreenB1,PurpleB1=input().split()
    GreenB=int(GreenB1)
    PurpleB=int(PurpleB1)
    Parti=int(input())
    arr1=[]
    arr2=[]
    for P in range(Parti):
        a1,b1=input().split()
        a=int(a1)
        b=int(b1)
        arr1.append(a)
        arr2.append(b)
    print(arr1)
    print(arr2)
    sumA1=0
    sumA2=0
    for i in range(len(arr1)):
        sumA1+=arr1[i]
    for j in range(len(arr2)):
        sumA2+=arr2[j]
    print(sumA1)
    print(sumA2)
    print(GreenB)
    print(PurpleB)
    
    if sumA1 > sumA2:
        if GreenB > PurpleB:
            print((sumA1*PurpleB)+(sumA2*GreenB))
         else:
            print((sumA1*GreenB)+(sumA2*PurpleB))
            
    if sumA2 > sumA1:
        
        if GreenB > PurpleB:
            print((sumA2*PurpleB)+(sumA1*GreenB))
        else:
            print((sumA2*GreenB)+(sumA1*PurpleB))
    else:
        print((sumA2*PurpleB)+(sumA1*GreenB))
   
    
