a=int(input())
b=list(map(int,input().split()))
c=[]
for i in range(a):
    for j in range(i+1,len(b)):
        if(b[j]==b[i]):
            c.append(b[i])
            print(c)
if(len(c)==0):
    print("unique")
else:
    h=set(c)
    print(h)
    for i in h:
        print(i,end=" ")
