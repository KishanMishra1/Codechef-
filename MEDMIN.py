for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    x=sorted(x)
    print(x[n//2]-x[(n//2)-1])
