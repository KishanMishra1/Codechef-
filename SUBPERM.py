'''A permutation of length N is an array of N integers P=[P1,P2,…,PN] such that every integer from 1 to N (inclusive) appears in it exactly once. For example, [2,3,4,1] is a permutation of length 4.

A subsegment of an array A[L…R]=[AL,AL+1,…,AR] is called good if the subsegment is a permutation of length (R−L+1). For example, the array A=[2,3,1,4,2] contains 3 good subsegments: A[3…3]=[1], A[1…3] =[2,3,1], A[2…5]=[3,1,4,2].

You are given two integers N and K. Find a permutation of length N such that it contains exactly K good subsegments. Print -1 if no such permutation exists'''

def solve():
    n,k=map(int,input().split())
    if n==1 and k==1:
        print(1)
    else:
        if k<2 or k>n:
            print(-1)
        else:
            kis=0
            for i in range(k-1):
                print(i+1,end=" ")
                kis=i
            for i in range(n-kis-1):
                print(n-i,end=" ")
            print()

if __name__=="__main__":
    for _ in range(int(input())):
        solve()
