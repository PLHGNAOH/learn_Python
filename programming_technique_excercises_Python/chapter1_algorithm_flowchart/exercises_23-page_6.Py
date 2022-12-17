print("Nhap so nguyen duong n")
n=int(input())
dem=0
i=0
while i<n:
     i=i+1 
     if(n % i == 0):
       dem=dem+1

print("Uoc so la "+str(dem))    

