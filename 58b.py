n,k=input().split()
j=input().split()
b=0
for i in (j):
    if(int(i)%int(k)==0):
        b=i    
if(b==k):
    print("yes")
else:
    print("no")
