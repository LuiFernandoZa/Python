letras="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
escri=input("escribe un texto: ")
escri=escri.upper()
num=int(input("cuanto de dezplazamiento: "))
pala=""
for i in escri:
    if i in letras:
        nume=letras.index(i)
        palas=letras[nume+num]
        pala+=palas
print(pala)