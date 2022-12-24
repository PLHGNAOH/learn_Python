def kiemtrasonnguyento(n):
    if n<2:
        print("khong phai la so nguyen to ")
        return 0
    i=2
    count=0
    while i<n:
        if n%i==0:
            count=count+1
        i=i+1
    if count==0 and n!=1 :
        print("la so nguyen to ")
    else:
        print("khong la so nguyen to ")
print("nhap n")
n=int(input())
kiemtrasonnguyento(n)    
