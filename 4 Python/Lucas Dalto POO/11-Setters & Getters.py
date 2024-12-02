class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre


# Crear una instancia de la clase Persona
persona = Persona("Juan")

# Obtener el valor del atributo __nombre utilizando el getter
print(persona.get_nombre())  # Salida: Juan

# Intentar acceder al atributo __nombre directamente (esto no se recomienda y generará un error)
# print(persona.__nombre)  # Generará un error, el atributo es privado

# Establecer un nuevo valor para el atributo __nombre utilizando el método setter
persona.set_nombre("Pedro")

# Obtener el nuevo valor del atributo __nombre utilizando el getter
print(persona.get_nombre())  # Salida: Pedro

# Intentar llamar al método privado directamente (esto no se recomienda y generará un error)
# persona.__privado()  # Generará un error, el método es privado
