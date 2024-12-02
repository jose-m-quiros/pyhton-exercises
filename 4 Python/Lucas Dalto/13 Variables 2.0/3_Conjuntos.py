#Creando un conjunto con set()
conjunto = set(["Others datos 1", "Jajajajj 2"])
print(conjunto)
print(type(conjunto))
print("----------------------------------")



#Metiendo un conjunto dentro de otro conjunto
conjunto2 = frozenset(["Cocodrilo", "Guatusa"]) #frozenset: Conjunto congelado | Crea un conjunto inmutable y que puede estar 
                                                                                 #congelado, como para que se pueda meter dentro
                                                                                 #de otro conjunto
conjunto2_1 = {conjunto2, "Venado"}
print(conjunto2_1)
print(type(conjunto2_1))
print("----------------------------------")
print("----------------------------------")


#Teoria De Conjuntos

conjunto2 = {1, 3, 5, 7, 9}
conjunto2_1 = {1, 5, 9}
conjunto2_2 = {10, 59, 60}


#Verificando si es un subconjunto

                        #Subconjunto
resultado = conjunto2_1.issubset(conjunto2)
print(resultado)


#Tambien se puede usar asi
resultado = conjunto2_1 <= conjunto2
#Lo que comprueba es si conjunto2_1 es mayor o igual a conjunto2
print(resultado)
print(type(resultado))


print(" ")
                    #SuperConjunto
resultado = conjunto2_1.issuperset(conjunto2)
print(resultado)

resultado = conjunto2_1 >= conjunto2
print(resultado)
print(type(resultado))
print("----------------------------------")


#Verificar si hay algun numero en comun
resultado = conjunto2_2.isdisjoint(conjunto2) #Lo que hace isdisjoint() es verificar si hay numeros igules
                                              #Si encuentra numeros IGUALES devuelve false
                                              #Si NO encuentra numeros IGUALES devuelve true
print(resultado)
print(" ")