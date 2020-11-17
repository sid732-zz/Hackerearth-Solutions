s=input()
a=0
lst=[]
boo=True
for i in range(len(s)-1):
  if(s[i]==s[i+1]):
    if(a==0):
      lst.append(i+1)
      a=i+1  
    else:
      lst.append((i+1)-a)
      a=i+1
    boo=False
  if(i==len(s)-2):
      lst.append(len(s)-a)
if(boo==True):
  print(len(s))
else:
  print(max(lst))

  
