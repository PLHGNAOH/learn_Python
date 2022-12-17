print("nhap so nguyen duong n")
n=int(input())
i=1
s=0
while i<=n:
    if n % i == 0:
     if i%2==0:
        print("danh sach uoc so chan "+str(i))
        s=s+i
    i=i+1
print("tong tat ca cac uoc chan cua so nguyen duong n la "+str(s))        