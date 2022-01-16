from collections import Counter
for _ in range(int(input())):
    s=input()
    n=len(s)
    h=n//2
    if n%2==0:
        if Counter(s[:h])==Counter(s[h:n]):
            print("YES")
        else:
            print("NO")
    else:
        if Counter(s[:h])==Counter(s[h+1:n]):
            print("YES")
        else:
            print("NO")
    
