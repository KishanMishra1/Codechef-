for _ in range(int(input())):
    n,k=map(int,input().split())
    count=0
    list1=list(map(int,input().split()))
    for i in range(n):
        list1[i]=list1[i]+k
    for i in range(n):
        if list1[i]%7==0:
            count+=1
    print(count)
