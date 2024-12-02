class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.__nombre} y tengo {self.__edad} años.")


# Crear una instancia de la clase Persona
persona = Persona("Juan", 30)

# Llamar al método de la clase para saludar
persona.saludar()

# Intento de acceso directo al atributo __nombre (esto no se recomienda)
print(persona.__nombre)  # Generará un error, el atributo es privado
