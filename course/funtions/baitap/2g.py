import math
def kiemtrasochinhphuong(n):
    i=1
    i==math.sqrt(n)
    while i<=n:
        if i*i==n:
            return True
        i+=1

        
        
def tongsochinhphuong(n):
    i=1
    sum=0
    while i<=n:
        if kiemtrasochinhphuong(i)==True:
            sum=sum+i
        i=i+1
    print(sum)
    return sum
tongsochinhphuong(9)


