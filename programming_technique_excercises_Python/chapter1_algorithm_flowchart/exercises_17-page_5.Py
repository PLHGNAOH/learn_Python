n=5
x=3
i=1
tich=1
S=0
while i<=n:
    tu=pow(x,i)
    tich=tich*i
    mau=tich
    S=S+tu/mau
    i+=1
print("S",S)    