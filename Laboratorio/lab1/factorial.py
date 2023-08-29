n = int(input("Factorial de n: "))
resp=1
for i in range(1,n+1):
    resp*=i
    
print(f'su factorial es {resp}')