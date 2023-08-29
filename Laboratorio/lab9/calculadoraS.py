try:
    sum = lambda a,b: a+b
    resta = lambda a,b: a-b
    multipli = lambda a,b: a*b
    divi = lambda a,b: a/b
    op=input("Elegir operacion: ")
    num1=int(input("Insertar numero 1: "))
    num2=int(input("Insertar numero 2: "))
    result=0
    if op == "suma":
        result=sum(num1,num2)
    elif op =="resta":
        result=resta(num1,num2)
    elif op =="multiplicacion":
        result=multipli(num1,num2)
    elif op =="division":
        result=divi(num1,num2)
    else:
        print("Elijauna opcion existente")
    print(f"Su resultado es {result}")
except ValueError:
    print("Ocurrio un error de valor")
except ZeroDivisionError:
    print("Los numeros no se puedem dividir por cero")
except TypeError:
    print("Ocurrio un error de tipo")
