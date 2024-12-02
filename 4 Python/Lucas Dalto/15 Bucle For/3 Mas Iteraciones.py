
Frutas = ["Banano", "Sandia", "Pina", "Melocoton", "Melon", "Papaya", "Naranja", "Mandarina"]

#Evitando que compre la sandia con sentencia continua
for Fruta in Frutas:
    if Fruta == 'Sandia':
        continue
    print(f'Lista De Frutas A Comprar: {Fruta}')
    
print("-------------------------------")


#Evitar que el bucle se siga ejecutando | Darle un fin a un bucle sin que recorra todos los elementos
#El else no se ejecuta despues de break | El break frena todo el proceso
for Fruta in Frutas:
    print(f'Lista De Frutas A Comprar: {Fruta}')
    if Fruta == 'Melocoton':
        break
else:
    print("No se muestra")
    
print("Se detuvo el bucle")

    
print("-------------------------------")



#Recorrer una cadena de texto

cadenas = "Jose esta recibiendo clases con el Profe Dalto"

for letra in cadenas:
    print(letra)
    

print("--------------------------------")
print(" ")



print("-----------Sin X2---------------")
Numeros = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(Numeros)
print(" ")



print("-------------X2-----------------")
#For en varias lineas de codigo
num_du = list()
for Numero in Numeros:
    num_du.append(Numero * 2)
print(num_du)
print(" ")



print("-------En una sola linea--------")
#For en una sola linea de codigo
duplicados = [x * 2 for x in Numeros]
print(duplicados)