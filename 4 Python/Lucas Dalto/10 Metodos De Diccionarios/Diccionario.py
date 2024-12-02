diccionario = {
    "Nombre": "Jose",
    "Apellido": "Quiros",
    "Fecha Nacimiento": 2006
}

print("-----------------------Keys-----------------------")
#Keys()-> Devuelve las claves | Tambien nos sirve para iterar -> Mas Adelante | Nos devuelve un objeto dict_item
claves = diccionario.keys()
print(claves)
print("--------------------------------------------------")


print("------------------------Get-----------------------")
#Get() -> Devuelve el valor de una clave | Si no encuentra nada el programa continua
gets = diccionario.get("Nombre")
print(gets)

print("--------------------------------------------------")


print("-----------------------Clear----------------------")
#Clear() -> Elimina todos los elementos del diccionario
# diccionario.clear()
# print(diccionario)

print("--------------------------------------------------")



print("------------------------Pop-----------------------")
#Pop() -> Elimina un elemento del diccionario
diccionario.pop("Apellido")
print(diccionario)

print("--------------------------------------------------")



print("-----------------------Items----------------------")
#Items() -> Para iterar el dict
diccionario_iterable = diccionario.items()
print(diccionario_iterable)