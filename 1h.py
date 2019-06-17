q=int(input())
t=input().split()
y=[]
for i in range(q):
    for j in range(i+1,len(t)):
        if(t[j]==t[i]):
            y.append(t[i])
if(len(y)==0):
    print("unique")
else:
    y.sort()
    h=set(y)
    for i in h:
        print(i,end=" ")
