import math
print("enter n ")
n=int(input())
print("enter x ")
x=float(input())
S=0
M=0
i=1
while i<=n:
    T=math.pow(x,i)
    M=M+i
    S=S+T/M
    i+=1
print("Sum ="+str(S))