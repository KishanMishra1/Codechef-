'''Chef is asked to write a program that takes an array A of length N and two integers X,Y as input and modifies it as follows:

Choose a random subset of elements of A (possibly empty)
Increase all the elements of the chosen subset by X
Increase the remaining elements in A by Y
You are given N, X, Y, A and the array B that is returned by Chef's program. Determine whether Chef's program gave the correct output.'''

class Solution:
    def solve(self,x,y,a,b):
        for i in range(n):
            if b[i]-a[i]==x or b[i]-a[i]==y:
                continue
            else:
                return False
            break
        return True



if __name__=="__main__":
    obj=Solution()
    for _ in range(int(input())):
        n,x,y=map(int,input().split())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        k=obj.solve(x,y,a,b)
        if k:
            print("YES")
        else:
            print("NO")
