import string
from random import randint
def generar_contra(nro=8):
    if nro<8:
        print("Deve tener 8 caracteres como minimo")
        return
    letras=string.ascii_letters
    numeros=string.digits
    punc=string.punctuation
    contraseña=""
    for i in range(nro+3):
        if 1%2==0:
            contraseña+=numeros[randint(0,8)]
        elif i%3==0:
            contraseña+=letras[randint(27,50)]
        elif i%5==0:
            contraseña+=punc[randint(0,30)]
        elif i%2!=0 and i%3!=0 and i%5!=0:
            contraseña+=letras[randint(0,26)]
        
    print(f'una contraseña segura de {nro} digitos es: {contraseña}')
nro=int(input("De cuantos digitos quieres que sea tu contraseña: "))
generar_contra(nro)
