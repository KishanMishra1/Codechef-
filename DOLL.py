t = int(input())
for i in range(t):
    c = 0
    a, b = map(int,input().split())
    l = list(map(int,input().split()))
    for j in l:
        if(j>b):
            c+=1
    print(c)
