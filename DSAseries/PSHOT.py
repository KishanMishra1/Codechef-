def solve():
    n = int(input())
    s = input()
    ans  = 0
    ashoots = 0
    bshoots = 0
    for i in range(2*n):
        if(ashoots > bshoots + (2*n - i +1)//2): return i
        if(bshoots > ashoots + (2*n - i)//2): return i
        if(i%2==0): ashoots += int(s[i])
        else: bshoots += int(s[i])
    return i+1


for _ in range(int(input())):
    print(solve())
    
