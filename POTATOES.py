for i in range(int(input())):
    a,b=map(int,input().split())
    d= a+b+1
    y=0
    while y==0:
        x= 0
        for i in range(1,d+1):
            if d%i==0:
                x+=1    
        if x==2:
            y=1
            print(d-(a+b))
        else :
            d+=1
