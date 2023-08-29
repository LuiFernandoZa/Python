try:
    valor=int(input("Insertar valor que se desea convertir: "))
    op=input("Insertar a que se quiere convertir celcius(C) o fahrenheit(F): ")
    if op=="F":
        valor=valor*1.8+32
    elif op=="C":
        valor=valor-32/18
    print(f"El resultado de la convercion es {valor}°{op}")
except FileNotFoundError:
    print("El resultado no se encontro")
except ValueError:
    print("Error de valor: ")
else:
    print("Error desconocido")