a=int(input())
b=int(input())
c=int(input())
if a>=b and a>=c:
    if b>=c:
        sl=b
    else:
        sl=c
elif b>=a and b>=c:
    if a>=c:
        sl=a
    else:
        s1=c
elif a>=b:
    sl=a
else:
    sl=b
print(sl)

NOTE: IT GIVES NZEC ERROR , BUT ITS O(1) APPROACH.
