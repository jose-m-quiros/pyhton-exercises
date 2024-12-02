# Definir un decorador
def mi_decorador(func):
    def wrapper():
        print("Antes de la función")
        func()
        print("Después de la función")
    return wrapper

#Forma optima de hacerlo
# Aplicar el decorador a una función
@mi_decorador
def saludar():
    print("¡Hola!")

# Llamar a la función decorada
saludar()




#Forma no optima de hacerlo
# # Aplicar el decorador a una función
# def saludar():
#     print("¡Hola!")

# # Llamar a la función decorada
# saludar_modificado = mi_decorador(saludar)
# saludar_modificado()
