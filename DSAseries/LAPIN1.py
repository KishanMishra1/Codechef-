for _ in range(int(input())):
    st=input()
    d1={}
    d2={}
    n=len(st)
    s=0
    e=n-1
    while(s<e):
        l=st[s]
        r=st[e]
        if l in d1:
            d1[l]+=1
        else:
            d1[l]=1
        if r in d2:
            d2[r]+=1
        else:
            d2[r]=1
        s+=1
        e-=1
    print(d1)
    print(d2)
    if d1==d2:
        print("YES")
    else:
        print("N0")
