import string
from random import randint
try:
    def Contra(longitud=8,mayus=True,nume=True,caracter=True):
        letras=string.ascii_letters
        num=string.digits
        caract=string.punctuation
        contra=""
        for i in range(1,longitud+1):
            if mayus==True and i%2==0:
                contra+=letras[randint(26,50)]
            elif nume==True and i%3==0:
                contra+=num[randint(0,8)]
            elif caracter==True and i%5==0:
                contra+=caract[randint(0,13)]
            else:
                contra+=letras[randint(0,26)]  
        print(contra)
    long=int(input("De cuantos caracteres quieres tu contraseña: "))
    may=input("Lo quieres con mayusculas Y(si) N(no): ")
    n=input("Lo quieres con numeros Y(si) N(no): ")
    espe=input("Lo quieres con caracteres especiales Y(si) N(no): ")
    if may=="N":
        may=False
    else:
        may=True
    if n=="N":
        n=False
    else:
        n=True
    if espe=="N":
        espe=False
    else:
        espe=True
    Contra(long,may,n,espe)
except ValueError:
    print("Ocurrrio un error de valor")
except TypeError:
    print("Ocurrio un error de tipo")
