def even(n):
    cu=2
    sum1=0
    i=0
    while i<n:
        sum1+=cu
        cu+=2
        i+=1
    return sum1
n=int(input())
k=even(n)
print("{} {}".format(n*n,k))
