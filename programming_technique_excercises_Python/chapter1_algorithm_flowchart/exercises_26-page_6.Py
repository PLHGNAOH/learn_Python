print("nhap so nguyen duong n ")
n=int(input())
i=1
tich=1
while i<=n:
    if n % i == 0:
        if i %2 == 1:
         tich=tich*i
         print("danh sach tat ca uoc so le cua so nguyen duong n la "+str(i))
    i=i+1      
print("tich tat ca uoc so le cua so nguyen duong n la "+str(tich))
