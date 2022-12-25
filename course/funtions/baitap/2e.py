def tongsole(n):
    sum=0
    i=1
    while i<=n:
        if i%2==1:
            sum=sum+i
        i=i+1
    print("tong cac so le la "+str(sum))
    return sum
print("nhap n ")
n=int(input())
tongsole(n)