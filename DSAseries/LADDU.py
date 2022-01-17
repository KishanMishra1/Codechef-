t=int(input())
for i in range(t):
    f=0
    act,origin=map(str,input().split())
    for i in range(int(act)):
        arr=list(map(str,input().split()))
        if arr[0]=="TOP_CONTRIBUTOR":
            f=f+300
        elif arr[0]=="CONTEST_WON":
            f=f+(300+(max(0,20-int(arr[1]))))
        elif arr[0]=="BUG_FOUND":
            f=f+int(arr[1]) 
        else:
            f=f+50      
        if origin=="INDIAN":
            mnladdu=f//200
        else:
            mnladdu=f//400
    print(mnladdu)
