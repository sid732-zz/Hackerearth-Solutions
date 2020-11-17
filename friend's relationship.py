t=int(input())
for tt in range(t):
    n=int(input())
    string='*'+ ((2*n)-2)*'#' + '*'
    string=list(string)
    print("".join(string))
    for i in range(1,n):
        string[i]='*'
        string[-i-1]='*'
        print("".join(string))
