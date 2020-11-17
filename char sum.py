import string
li=list(string.ascii_lowercase)
summ=0
ip=input()
for i in range(len(ip)):
    a=ip[i]
    if(a in li):
       summ=li.index(a)+1 +summ
print(summ)
