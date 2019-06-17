a=int(input())
b=input().split()
c=[]
d=''
for i in (b):
    c.append(i)
c.sort(reverse=True)
for i in range(len(c)):
    d+=str(c[i])
print(d)
