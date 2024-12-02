#Creando una funcion de 3 parametros
def frase(nombre, apellido, adjetivo):
    return f"{nombre} {apellido} es un {adjetivo}"

#Utilizando keyword arguments
frase_resultante = frase(adjetivo="Es programador", nombre="Jose", apellido="Manuel" )
print(frase_resultante)


print("------------------------------------------------")
print("")



#Creando la misma funcion con un parametro opcional y un valor por efecto
def frase3(nombre, apellido, adjetivo = "Atento"):
    return f"{nombre} {apellido} es muy {adjetivo}"

frase_resultante3 = frase3("Jose", "Manuel", "inteligente")
print(frase_resultante3)