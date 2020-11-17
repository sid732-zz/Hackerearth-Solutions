string=input()

res=""
for i in range(1,len(string)+1):
        res+= string[-i]
if string==res:
    print("YES")
else:
    print("NO")
