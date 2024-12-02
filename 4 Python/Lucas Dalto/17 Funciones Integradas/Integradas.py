#Sirve como tupla, lista o conjunto | Por ley deben ser numeros
numeros = [1, 2, 3, 4, 5]


#Encontrando el numero mayor de una lista 
MasAlto = max(numeros)
print(MasAlto)
print("--------------------------")


#Encontrando el numero menor de una lista 
MasEnano = min(numeros)
print(MasEnano)
print("--------------------------")


#Redondeando numeros de la FORMA CORRECTA
numeros1 = round(12.3456, 1) #Lo que estamos asiendo despues de la coma es indicar cuantos decimales queremos despues del punto
print(numeros1)
print("--------------------------")
#De aqui para arriba van los que deben por ley ser numeros


#Retorna False -> 0, vacio, False o None
#Retorna True -> Distinto a 0, True, Cadena, Datos no Vacios
reseultado_bool = bool(0)

print(reseultado_bool)

print("--------------------------")

#Retorna True SI TODOS los valores son verdaderos
reseultado_all = all([222, True, ["Pollo", 17]])
print(reseultado_all)

print("--------------------------")

#Suma todos los valores  de un iterable
sum_numeros = sum(numeros)
print(sum_numeros)