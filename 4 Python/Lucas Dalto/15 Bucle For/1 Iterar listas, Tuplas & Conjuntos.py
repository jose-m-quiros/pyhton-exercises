#For es un bucle que nos permite iterar | El Python los bucles son for in 

#For in es un bucle que justamente lo que hace es crear una variable, que en cada vuelta va hacer igual 
#a ese pedacito de variable que estamos igualando

#Estas lista TAMBIEN SE PUEDEN HACER CON TUPLAS NO AFECTA en nada

#Recorriendo la lista de animales
nombres = ["Jose", "Lucas", "Volcom", "Nike", "Adidas", "Kai", "Jordan", "Sneakers", "Tenis"]

for nombre in nombres: 
    print(f'La variable nombre es igual a: {nombre}')
    
print("----------------------------")



#Recorriendo la lista numeros y multiplicando cada valor x2
numeros = [10, 21, 32, 43, 54, 67, 75, 90, 95]

for numero in numeros: 
    resultado = numero * 2
    print(resultado)

print("----------------------------")
print("----------------------------")



#Iterando dos lista del mismo tamaño al mismo tiempo
nombres1 = ["Jose", "Lucas", "Volcom", "Nike", "Adidas", "Kai", "Jordan", "Sneakers", "Tenis"]
numeros1 = [12, 23, 52, 63, 76, 77, 89, 90, 99]

for nombre1, numero1 in zip(nombres1, numeros1):
    print(f'Recorriendo lista 3: {nombre1}')
    print(" ") 
    print(f'Recorriendo la lista 4: {numero1}')
    print(" ")

print("----------------------------")



#Mostrando un rango de numeros con 2 parametros
for num in range(1,20): #El 1 donde comienza Y el 20 donde termina | SIEMPRE el segundo parametro se le resta: 1 cuando se imprime.
                        #Ejemplo: range(1,20) comienza en 1 y termina en 19 ya que el 20 no lo cuenta.
    print(num)
    
print("----------------------------")



#Mostrando un rango de numeros con 1 parametro
#Y si solo se le pone un parametro arranca de 0 al numero que le indicamos.
for num2 in range(5): 
    print(num2)
        
print("----------------------------")



#NO FUNCIONA EN CONJUNTOS
#FORMA NO OPTIMA DE RECORRER UNA LISTA | NO HACER YA QUE SE VE MUY MAL Y SE VAN A REIR
#Recorriendo una lista por el indice
#Le estamos pidiendo que que muestre la cantidad de elementos que tiene
for num in range(len(numeros)):
    print(numeros[num])
    
print("----------------------------")    



#FORMA CORRECTA DE RECORRER UNA LISTA
for optima in enumerate(numeros):
    indice = optima[0]
    valor = optima[1]
    print(f"Indice: {indice} | Valor: {valor}")
    
print("----------------------------")



#Usando el for / else
for els in numeros:
    print(f"Ejecutando el ultimo bucle. | Valor Actual {els}")
else:
    print("Fin De Bucle")
    
    
#TODO LO ANTERIOR FUNCIONA EXACTAMENTE IGUAL PARA LAS TUPLAS & CONJUNTOS