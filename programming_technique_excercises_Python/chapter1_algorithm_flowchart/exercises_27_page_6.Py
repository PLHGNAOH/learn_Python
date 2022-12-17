print("nhap vao so nguyen duong n")
n=int(input())
i=1
dem=0
while i<=n:
    if n%i==0:
        if i%2==0:
            print("danh sach uoc so chan cua so nguyen duong n la "+str(i))
            dem=dem+1
    i=i+1        
print("so luong uoc so chan cua so nguyen duong n la "+str(dem))    