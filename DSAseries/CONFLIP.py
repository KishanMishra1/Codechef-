for _ in range(int(input())):
    g=int(input()) #no of games played
    for i in range(g):
        i,n,q=map(int,input().split())
        h=0
        t=0
        if n%2==0:
            h=n//2
            t=n//2
        else:
            if i==1:
                h=n//2
                t=(n//2)+1
            else:
                h=(n//2)+1
                t=(n//2)
        if q==1:
            print(h)
        elif q==2:
            print(t)
