numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Creando una funcion comun que me diga si es par o no
#PAR
# def par(num):
#     if (num%2==0):
#         return True

# #NO PAR
# def inpar(num):
#     if (num%2==1):
#         return True

# #Usando filter con una  funcion comun 

# #PAR
# pares2 = filter(par, numeros)

# #NO PAR
# pares3 = filter(inpar, numeros)

# print(list(pares2))
# print(list(pares3))



#Beneficios:
    #1. Lo podemos usar cuando queremos hacer algo sencillo y rapido 
    #2. Retornan automaticamente

#Desventaja:
    #1. No es son aptas cuando queremos hacer mas de una instrucciones

    
#Creando una funcion lambda para multiplicar x*2

multiplicar_por_dos = lambda x : x*2
print(multiplicar_por_dos(5))


print("")
print("Lo mismo pero mas barato | Mejorado")
#Creando lo mismo que antes pero con LAMBDA
#Par
num_pares = filter(lambda numeros1: numeros1 %2 == 0, numeros)
print(list(num_pares))


#No Par
num_inpares = filter(lambda numeros2: numeros2 %2 == 1, numeros)
print(list(num_inpares))