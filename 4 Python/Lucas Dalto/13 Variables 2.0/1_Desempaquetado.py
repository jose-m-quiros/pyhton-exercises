#Creado los Datos
datos_tupla = ("Jose", "Quiros", 16)
datos_lista = ["Jose", "Quiros", 16]
datos_set = {"Jose", "Quiros"}  # No permite desempaquetar NUMEROS


#Desempaquetado
nombre1, apellido1, edad1 = datos_tupla
nombre2, apellido2, edad2 = datos_lista
nombre, apellido = datos_set


#Imprimiendo resultado
print(f'Mi Nombre es {nombre1} {apellido2} y tengo {edad1}')