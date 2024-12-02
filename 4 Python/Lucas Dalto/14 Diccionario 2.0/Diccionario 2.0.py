#Creando un diccionario con dict()
#Se puede hacer de cualquiera de las dos formas pero como estamos trabajando con 2.0 
#Entonces es mejor trabajar con diccionario 2.0 (diccionario0)

diccionario0 = dict(
    Nombre = "Jose", 
    Apellido = "Quiros"
)

#Este esta modo viejito
diccionario = {
    'Nombre' : "Jose",
    'Apellido' : "Quiros"
}

print(diccionario0)
print(diccionario)
print("------------------------------------------------")


#Las listas no pueden ser claves 
diccionario2 = {frozenset(["dalto", "oso"]) : "pollo"}
print(diccionario2)
print("------------------------------------------------")


#Creando diccionarios con fromkeys() valor por defecto
diccionario3 = dict.fromkeys(["Nombre", "Apellidos"])
print(diccionario3)
print("------------------------------------------------")




#Creando diccionarios con fromkeys() cambiando el valor por defecto a "Esto es x2"
diccionario4 = dict.fromkeys(["Nombre", "Apellidos"], "Esto es x2")
print(diccionario4)
print("------------------------------------------------")


