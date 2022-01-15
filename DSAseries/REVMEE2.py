n=int(input())
list1=list(map(int,input().split()))
for i in range(n-1,-1,-1):
    print(list1[i],end=" ")
