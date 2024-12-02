#Ejemplo sin setters
class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre


# Crear una instancia de la clase Persona
persona = Persona("Juan, No modificado sin setter ")

persona.__nombre = "Jose" # No se puede modificar

# Obtener el valor del nombre utilizando el getter (property)
print(persona.nombre)  # Salida: Juan


print("---------")

#Example 2 con setter
class Persona2:
    def __init__(self, nombre_inicial2):
        self.__nombre2 = nombre_inicial2

    @property
    def obtener_nombre2(self):
        return self.__nombre2

    @obtener_nombre2.setter
    def establecer_nombre2(self, nuevo_nombre2):
        self.__nombre2 = nuevo_nombre2


# Crear una instancia de la clase Persona2
persona2 = Persona2("Juan")

# Modificar el valor del nombre utilizando el setter (property)
persona2.establecer_nombre2 = "Jose, segundo ejemplo modificado."

# Obtener el valor del nombre utilizando el getter (property)
print(persona2.obtener_nombre2)  # Salida: Jose

print("---------")


#Ejemplo 3 con delete
class Persona3:
    def __init__(self, nombre_inicial3):
        self.__nombre3 = nombre_inicial3

    @property
    def nombre3(self):
        return self.__nombre3

    @nombre3.setter
    def nombre3(self, nuevo_nombre3):
        self.__nombre3 = nuevo_nombre3

    @nombre3.deleter
    def nombre3(self):
        del self.__nombre3


# Crear una instancia de la clase Persona3
persona3 = Persona3("Juan")

# Modificar el valor del nombre utilizando el setter (property)
persona3.nombre3 = "Jose del tercer ejemplo de eliminar"

# Obtener el valor del nombre utilizando el getter (property)
print(persona3.nombre3)  # Salida: Jose

# Eliminar el nombre utilizando el deleter
del persona3.nombre3

# Intentar obtener el valor del nombre después de eliminarlo (generará un error)
# print(persona3.nombre3)  # Generará un error, el atributo ya no existe
