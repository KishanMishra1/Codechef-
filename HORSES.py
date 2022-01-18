for _ in range(int(input())):
    n=int(input())
    res=[]
    arr=list(map(int,input().split()))
    arr.sort()
    for i in range(len(arr)-1):
        res.append(abs(arr[i]-arr[i+1]))
    print(min(res))
