t = int(input())
for i in range(t):
    lapindrom = input()
    l = len(lapindrom)
    if l%2==0:
        x = int(l/2)
        l1 = lapindrom[:x]
        l2 = lapindrom[x:]
    else :
        l1 = lapindrom[:int(l/2)]
        l2 = lapindrom[int(l/2)+1:]
    res = 'YES'
    for ele in l1:
        if ele not in l2:
            res = 'NO'
        elif ele in l2:
            if l1.count(ele) != l2.count(ele):
                res = 'NO'
    print(res)
