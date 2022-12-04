n=24
i=1
s=0
while i<=n:
    if n%i==0:
        print(i)  
        s=s+i      
    i+=1

print("S=",int(s))    
  
