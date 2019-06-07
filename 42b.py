a,b=input().split()
c=len(a)
d=len(b)
if(c>d):
    print(a)
elif(d>c):
    print(b)
else:
    print(a or b)
