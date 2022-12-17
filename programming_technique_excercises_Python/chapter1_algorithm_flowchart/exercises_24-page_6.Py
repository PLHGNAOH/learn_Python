print("nhap so nguyen duong n ")
n=int(input())
i=0
while i<n:
 i=i+1
 if n % i == 0:
   if i % 2 ==1:
    print("danh sach uoc so le cua so nguyen duong n la "+str(i))    