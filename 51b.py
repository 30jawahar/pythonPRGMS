k=input()
b=[]
d=''
for i in k:
    l=i
    b.append(i)
for i in range(len(b)-1):
    d+=str(b[i])+" "
print(d+str(b[-1]))
