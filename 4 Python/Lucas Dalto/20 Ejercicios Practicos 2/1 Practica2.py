# falto el profe y los pibes van a armar la clase.

# pedir el nombre y la edad de los compañeros que vinieron hoy a clase.

# def obtener_compañeros(cantidad_de_compañeros):
    
#     Creando lista con los compañeros
#     compañeros = []
    
#     Ejecutando un for para pedir informacion de cada compañero
#     for i in range(cantidad_de_compañeros):
#             nombre = input("Nombre del compañero: ")
#             edad = int(input("Edad del compañero: "))
#             compañero = (nombre, edad)
            
#             Agregando la informacion a la lista
#             compañeros.append(compañero)
   
#     Ordenandolos de menor a mayor segun su edad.
#     compañeros.sort(key = lambda x: x[1])
    
#     Compañeros[x] devuelva una tupla con (nombre, edad) y despues accedemos al nombre.
#     Para definir al asistente y al profesor 
#     asistente = compañeros[0][0]
#     profesor = compañeros[-1][0]
    
#     Retornando una tupla.
#     return asistente, profesor

# Desempaquetando lo que retorna la funcion
# asistente, profesor = obtener_compañeros(5)


# print(f"El profesor es: {profesor} y su asistente es {asistente}")






#Avanzado

def obtener_compañeros(cant_de_compas):
    compañeros = []
    for i in range(1, cant_de_compas + 1):
        print(f"\nEstudiante {i}:")
        nombre = input("Nombre del compañero: ")
        edad = int(input("Edad de compañero: "))
        compañero = (nombre, edad)
        compañeros.append(compañero)

    compañeros.sort(key=lambda x: x[1], reverse=True)
    profesores = [compañeros[0][0]]
    for i in range(1, len(compañeros)):
        if compañeros[i][1] == compañeros[0][1]:
            profesores.append(compañeros[i][0])
        else:
            break

    asistentes = []
    for compa in compañeros:
        if compa[1] == compañeros[-1][1] and compa[0] not in profesores:
            asistentes.append(compa[0])

    if len(profesores) == 1:
        profesor_str = f"El profesor es {profesores[0]}"
    else:
        profesor_str = f"Los profesores son {', '.join(profesores)}"

    if len(asistentes) == 1:
        print(f"{profesor_str} y su valiente asistente es {asistentes[0]}.")
    elif len(asistentes) > 1:
        asistentes_str = ", ".join(asistentes)
        print(f"{profesor_str} y sus valientes asistentes son {asistentes_str}.")
    else:
        print(profesor_str)

obtener_compañeros(5)
