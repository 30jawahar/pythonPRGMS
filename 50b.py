a=int(input())
for i in range(a):
    k=2**i
    l=0
    if(k==a):
        l=k
        break
if(l==a):
    print("yes")
else:
    print("no")
