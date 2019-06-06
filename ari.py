a,n,d=input().split()
h=(int(n)+((int(a)-1)*int(d)))
avg=((int(n)+int(h))//2)
ng=((int(h)-int(n))//int(d))+1
sum=avg*ng
print(sum)
