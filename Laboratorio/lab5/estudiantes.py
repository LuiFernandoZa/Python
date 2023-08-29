edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
edades.sort()
maximo=max(edades)
minimo=min(edades)
result=0
print(f'la edad maxima es {maximo} y la edad minima es {minimo}')
rango=maximo-minimo
for i in edades:
    result+=i
result=result/len(edades)
media=(edades[4]+edades[5])/2
print(f"La media es {media}")
print(f'El promedio es {result}')
print((f"El ranfo es {rango}"))
comparar=abs(minimo-result)
comparar2=abs(maximo-result)
print(f"priera comparacion es {comparar} y la segunda es {comparar2}")