print("Nhap vao so xe cua ban")
n=int(input())
soxe=0
while n>0:
    soxe=soxe+n%10
    n=n//10
print("So xe cua ban la "+str(soxe%10))    