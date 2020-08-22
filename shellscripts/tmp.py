n=int(input())
l=[]
for i in range(n):
    s=input()
    l.append(s)
for i in range(n):
    temp=l[i]
    rev=temp[::-1]
    if rev in l:
        rlen=len(rev)
        print(rlen,end=" ")
        pos=rlen//2
        mchar=rev[pos]
        print(mchar)
        break
    else:
        continue
        

