for _ in range(int(input())):
    s1=input()
    s2=input()
    max1=0
    min1=0
    for i in range(len(s1)):
        if (s1[i]!=s2[i] and (s1[i]!='?' and s2[i]!='?')):
            min1+=1
        if ((s1[i]=='?' or s2[i]=='?') or (s1[i]=='?' and s2[i]=='?')):
            max1+=1
    print(min1,max1+min1,end="\n")
