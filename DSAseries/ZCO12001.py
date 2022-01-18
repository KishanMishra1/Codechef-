n=int(input())
s=input().replace(" ","")
l,lseq,m,k=0,0,0,0
for i in range(1,n+1):
    if s[i-1]=="1":
        k+=1
        if k>m:
            indep=i
            m=k
    else:
        k-=1
    l+=1
    if k==0:
        if l>lseq:
            ilseq=i-l+1
            lseq=l
        l=0
ndep=m
print(ndep,indep,lseq,ilseq)
