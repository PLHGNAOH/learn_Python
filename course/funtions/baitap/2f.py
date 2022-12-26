def kiemtrasonguyento(n):
    i=1
    count=0
    while i<=n:
        if n%i==0:
            count=count+1
        i+=1
    if count==2:
        return True

    

def tongsonguyento(n):
    i=1
    sum=0
    while i<=n:
        if kiemtrasonguyento(i)==True:
            sum=sum+i
        i+=1
    print(sum)
    return sum
tongsonguyento(9)
