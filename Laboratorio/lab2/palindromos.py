cadena=input("Insertar una palabra: ")
if " " in cadena:
    cadena=cadena.replace(" ","")
if "á" in cadena:
    cadena=cadena.replace("á","a")
if "é" in cadena:
    cadena=cadena.replace("e","e")
if "í" in cadena:
    cadena=cadena.replace("í","i")
if "ó" in cadena:
    cadena=cadena.replace("ó","o")
if "ú" in cadena:
    cadena=cadena.replace("ú","u")
if "." in cadena:
    cadena=cadena.replace(".","")
if "," in cadena:
    cadena=cadena.replace(",","")
cadena2=cadena[::-1]
if cadena2 == cadena:
    print("la palabra es palindroma")
else:
    print("la palabra no es palindroma")