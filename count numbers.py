for _ in range(int(input())):
  n=int(input())
  s=input()
  count=0
  for i in range(n-1):
    if((s[i].isnumeric() and s[i+1].isalpha()) or ((i==n-2) and s[i+1].isnumeric())):
      count+=1
  print(count)
