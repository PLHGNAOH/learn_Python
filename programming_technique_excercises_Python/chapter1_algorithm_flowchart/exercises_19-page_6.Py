n=5
i=1
x=3
S=1+x
mau=1
while i<=n:
    tu=pow(x,2*i+1)
    a=i*2+1
    mau=mau*a*(a-1)
    S=S+tu/mau
    i+=1
print("S=",float(S))    

