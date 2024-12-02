#NO HACER | NO OPTIMO
def suma(lista):
    numeros = 0 
    for numero in lista:
        numeros = numeros + numero
    return numeros

resultado = suma([10, 10, 11, 35, 65, 43])
print(resultado)
print("_________________________________________")



def suma_mas_o_menos(numeros_mas_o_menos):
    return sum([*numeros_mas_o_menos])

resultado_mas_o_menos = suma_mas_o_menos([10, 10, 11, 35, 65, 43])

print(resultado_mas_o_menos)


print("_________________________________________")
print("")
print("")

print("___________SE DEBE HACER ASI_____________")
#Forma OPTIMA | Se debe hacer asi
#Utilizando el operador * como argumento (*args)
#Algo importante de este parametro "args" = "numeros1" es que hay que usarlo al final si lo usamos antes no podemos agregar mas parametros.

def suma(nombre, *numeros1):
    return f"{nombre} la suma dio {sum(numeros1)}"
    
resultado_optimo = suma("Jose", 10, 10, 11, 35, 65, 43)
print(resultado_optimo)