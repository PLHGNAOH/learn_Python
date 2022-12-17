print("nhap so nguyen duong n ")
n=int(input())
i=1
tong=0
while i<n:
    if n%i==0:
        print("danh sach cac uoc so nho hon chinh no la "+str(i))
        tong=tong+i
    i=i+1    
print("tong cac uoc so nho hon chinh no la "+str(tong))        