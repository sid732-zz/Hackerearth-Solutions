s=input()
l=len(s)

for i in range(len(s)):
  if(s[i]=="6"):
    l=l-1
if(s[-1]=="6"):
  print(-1)
else:
  print(l)
