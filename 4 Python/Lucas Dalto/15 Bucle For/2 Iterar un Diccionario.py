diccionario = dict(
    Nombre = "Jose", 
    Apellido = "Quiros",
    Edad = 16
)


#Recorriendo Un Diccionario para obtener las claves
for key in diccionario:
    print(key)
    
print("--------------------------------")



#Recorriendo Un Diccionario con items() para obtener la clave y el valor 
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"Clave: {key} | Valor: {value}")