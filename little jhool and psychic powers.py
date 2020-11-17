'''
ip=input()
if(("000000" in ip) or ("111111" in ip) ):
  print("Sorry, sorry!")
else:
  print("Good luck!")
'''

# Write your code here
n = list(map(int,input()))
#print(n)
#print(len(n))

for i in range(len(n)):
    
    if n[i] == 0:
        c = 0
        for j in range(i+1,len(n)+1):
            if len(n) - (i+1) < 6:
                #print("Good luck!")
                pass
            elif n[j-1] == 0:
                c = c + 1
                if c > 6:
                    print("Sorry, sorry!")
                    exit(0)
    elif n[i] == 1:
        c = 0
        for j in range(i+1,len(n)+1):
            if len(n) - (i+1) < 6:
                #print("Good luck!")
                pass
            elif n[j-1] == 1:
                c = c + 1
                if c >6 :
                    print("Sorry, sorry!")
                    exit(0)
if c < 6:
    print("Good luck!")
