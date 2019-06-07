q=int(input())
g=input().split()
k=0
for i in range(len(g)+1):
    k=i+k
h=k//q
print(h)
