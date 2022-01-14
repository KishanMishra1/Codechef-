for _ in range(int(input())):
    n,x=map(int,input().split())
    ncoin=sorted(list(map(int,input().split())),reverse=True)
    #print(ncoin)
    sum1=0
    c= False
    for i in range(n):
        sum1+=ncoin[i]
        if sum1>=x:
            c=True
            break
    if(c):
        print(i+1)
    else:
        print(-1)
    
