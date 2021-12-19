for _  in range(int(input())):
    a,b,c=map(str,input().split())
    d,e=map(str,input().split())
    if a==d:
        print(d)
    elif a==e:
        print(e)
    elif b==d:
        print(d)
    else:
        print(e)
