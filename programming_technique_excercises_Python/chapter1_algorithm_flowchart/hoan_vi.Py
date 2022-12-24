a=5
b=6
temp=0

def hoan_vi(a,b):
    temp=a
    a=b
    b=temp   
    return a, b

a1, a2 = hoan_vi(a,b)
print(a1)
print(a2)

