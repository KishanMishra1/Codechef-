n=int(input())
list1=[1]
for i in range(2,n+1):
    if n%i==0:
        list1.append(i)
print(len(list1))
print(" ".join(str(i) for i in list1))
