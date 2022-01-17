for _ in range(int(input())):
        n = int(input())
        profit = []
        for _ in range(n):
            s,p,v = map(int, input().split())
            profit.append((p//(s+1))*v)
        print(max(profit))
