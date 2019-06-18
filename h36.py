q=input()
t=input().split()
p=[]
f=''
for i in (t):
    p.append(i)
p.reverse()
for i in range(len(p)-1):
    f+=str(p[i])+"->"
print(f+str(p[-1]))
