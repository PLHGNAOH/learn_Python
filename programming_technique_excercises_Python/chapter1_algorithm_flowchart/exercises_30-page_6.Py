print("nhap vao so nguyen duong n ")
n=int(input())
i=1
sum=0
while i<n:
    if n%i==0:
        sum=sum+i
    i=i+1        
if sum==n:
 print("la so hoan thien")    
else:
  print("khong la so hoan thien")    
  