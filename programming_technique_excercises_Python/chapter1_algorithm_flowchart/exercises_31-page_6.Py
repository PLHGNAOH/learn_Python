print("nhap so nguyen duong n ")
n=int(input())
i=3
if n<2:
 print("khong phai la so nguyen to ")
elif n==2:
  print("la so nguyen to chan duy nhat ")
elif n%2==0:
    print("khong la so nguyen to ")
else:
    while i<n:
        if n%i==0:
            print("khong la so nguyen to")
            break
        i=i+2        
    else:
        print("la so nguyen to ")
    

   
