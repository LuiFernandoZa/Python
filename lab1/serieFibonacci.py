n= int(input("Insertar cuantos numeros se desea ver de la serie: "))
a=0
b=1
c=1
num=[0,1]
for i in range(2,n):
    c=a+b
    num.append(c)
    a=b
    b=c
print(num)