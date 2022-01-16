s=[]
for _ in range(int(input())):
    arr=[]
    k=int(input())
    s.append(k)
arr=sorted(s)
n=len(arr)
arr2=[]
for i in arr:
    arr2.append(i*n)
    n-=1
print(max(arr2))
