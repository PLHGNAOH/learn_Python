print("nhap so nguyen duong n ")
n=int(input())
i=1
max=0
while i<=n:
    if n%i==0:
        if i%2==1:
            print("danh sach uoc so le cua so nguyen n la "+str(i))
            if i>max:
                max=i
    i=i+1
print("uoc so le lon nhat la "+str(max))