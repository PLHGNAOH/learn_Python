import math
def kiemtrasochinhphuong(n):
    i=1
    while i<=n:
        i==math.sqrt(n)
        if i*i==n:
            return True
        else:
            return False
def tongsochinhphuong(n):
    i=1
    sum=0
    while i<=n:
        if kiemtrasochinhphuong(i)==True:
            sum=sum+i
        print(sum)
        return sum

tongsochinhphuong(9)


