# cook your dish here
for _ in range(int(input())):
    scoreD=list(map(int,input().split()))
    scoreS=list(map(int,input().split()))
    #0-DSA 1-TOC 2-DM
    totalD=sum(scoreD)
    totalS=sum(scoreS)
    if totalD>totalS:
        print("DRAGON")
    elif totalS>totalD:
        print("SLOTH")
    if totalD==totalS and scoreD[0]>scoreS[0]:
        print("DRAGON")
    elif totalD==totalS and scoreD[0]<scoreS[0]:
        print("SLOTH")
    if totalD==totalS and scoreD[0]==scoreS[0] and scoreD[1]>scoreS[1]:
        print("DRAGON")
    elif totalD==totalS and scoreD[0]==scoreS[0] and scoreS[1]>scoreD[1]:
        print("SLOTH")
    elif totalD==totalS and scoreD[0]==scoreS[0] and scoreS[1]==scoreD[1]:
        print("TIE")
