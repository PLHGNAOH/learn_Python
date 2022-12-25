import math 

def kiemtrasochinhphuong(n):
        i=math.sqrt(n)
        if(i*i==n):
          print("la so chinh phuong  ")
        else:
          print("khong la so chinh phuong")

print("nhap n ")
n=int(input())
kiemtrasochinhphuong(n)

