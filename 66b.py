ss=int(input())
sp=0
for i in range(1,ss+1,1):
    if(ss%i==0):
        sp=sp+1
if(sp==2):
    print("yes")
else:
    print("no")
