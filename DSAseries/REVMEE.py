n=int(input())
list1=list(map(int,input().split()))
print(" ".join(str(i) for i in list1[::-1]))
