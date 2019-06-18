a=input()
b=input().split()
c=[]
d=''
for i in (b):
    c.append(i)
c.reverse()
for i in range(len(c)):
    d+=str(c[i])+"_>"
print(d+"_")
