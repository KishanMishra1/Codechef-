for _ in range(int(input())):
    ans=0
    k=0
    list=[str(i) for i in input()]
    for i in range(len(list)):
        if list[i]==">" and k==0:
            
            break
        elif list[i]=="<":
            k+=1
        elif list[i]==">":
            k-=1 
        if k==0:
            ans=i+1
    print(ans)
    list.clear()
    
