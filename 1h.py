f=int(input())
g=list(map(int,input().split()))
c=[]
for i in range(f):
    for j in range(i+1,len(g)):
        if(g[j]==g[i]):
            c.append(g[i])
if(len(c)==0):
    print("unique")
else:
    h=set(c)
    print(h)
    for i in h:
        print(i,end=" ")
