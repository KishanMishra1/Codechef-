num=int(input())
count,ld=0,0
temp=num
while(temp>0):
    ld=temp%10
    count+=1
    temp//=10
if count>3:
    print("More than 3 digits")
else:
    print(count)
