A=input()
B=input()
lA=list(A)
lB=list(B)
count=0
for i in range(len(A)-1):
    if lA[i]==lB[i]:
        continue
    else:
        if lB[i+1]==lA[i]:
            lB[i],lB[i+1]=lB[i+1],lB[i]
            count+=1
        else:
            continue
A="".join(map(str,lA))
B="".join(map(str,lB)) 
if A==B:
    print(count)
else:
    print(-1)

