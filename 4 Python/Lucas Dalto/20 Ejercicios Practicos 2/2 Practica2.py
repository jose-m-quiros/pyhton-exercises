#Creando una función que nos devuelva los numeros primos
#Entre 0 y el argumento que pasamos 

#Creando una funcion que verifique si un numero es primo
def primos(num):
    
    #Verificamos que el numero pasado no pueda dividirse por ningun numero entre 2 y ese mismo numero -1
    for i in range(2, num - 1):
    
    
        #Si es divisible por alguno retornamos false y termina el bucle
        if num%i==0: return False
    
    #Si termina el bucle, sigifica que no fue divisible entonces es primo
    return True


#Creando una funcion que retorne con todos los primos
def primos_uno(num):
    
    #Creamos la lista
    primos2 = []
    
    for i in range(2, num + 1):
        
        #Verificamos si el valor es primo
        resultado = primos(i)
        
        ##En caso de que sea lo agregamos la lista 
        if resultado == True: primos2.append(i)
        
    #Devolvemos la lista        
    return primos2

#Creamos el resultado llamando a la funcion y lo mostramos
resultado = primos_uno(6)
print(resultado)