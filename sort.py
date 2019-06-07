a=int(input())
b=input().split()
c=''
b.sort()
for i in range(len(b)-1):
    c+=str(b[i])+" "
print(c+str(b[-1]))
