a,k=input().split()
b=input().split()
i=0
n=0
while i<len(b):
    j=i+1
    while j<len(b):
        if(((int(b[i])+int(b[j]))==int(k))or(k in b)):
           n=True
           break
        else:
           n=False
        j+=1
    i+=1
if(n==True):
           print("yes")
else:
           print("no")
