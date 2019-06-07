a=int(input())
k=0
for i in range(1,a):
    l=a%10
    k=l+k
    a=a//10
print(k) 
