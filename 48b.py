q=int(input())
g=input().split()
k=0
for i in range(len(g)):
    k=int(g[i])+k
h=k//q
print(h)
