for _ in range(int(input())):
    t=int(input())
    ld=0
    rev=0
    temp=t
    while(temp>0):
        ld=temp%10
        rev=rev*10+ld
        temp=temp//10
    print(rev)
