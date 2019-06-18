a=input()
b=[]
f=''
c=set(a)
for i in c:
    b.append(i)
b.sort()
for i in range(len(b)):
    f+=str(b[i])
print(f)
