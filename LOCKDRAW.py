'''Bob and Alice are having a lockout match between them.
There are three problems in the contest worth A, B, and C points respectively.
Only the first player to solve a problem gets points for that problem.
It is impossible for Bob and Alice to solve a problem at the same time.
Chef wants to know if there is any chance of a draw if Bob and Alice manage to solve all 3 problems.
A draw occurs when both players end with equal number of points.'''

class Solution:
    def lockout(self,a,b,c):
        if a+b==c:
            print("YES")
        elif b+c==a:
            print("YES")
        elif c+a==b:
            print("YES")
        else:
            print("NO")



if __name__=="__main__":
    obj=Solution()
    for _ in range(int(input())):
        a,b,c=map(int,input().split())
        obj.lockout(a,b,c)
