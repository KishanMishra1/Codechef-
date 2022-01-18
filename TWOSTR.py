t=int(input())
for i in range(t):
    s1=str(input())
    s2=str(input())
    c=0
    for i in range(0,len(s1)):
        if s1[i]!=s2[i] and s1[i]!='?' and s2[i]!='?':
            c=1
            break
    if c==1:
        print("No")
    else:
        print("Yes")
