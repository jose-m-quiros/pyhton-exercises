class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def imprimir_grado(self):
        print(f"Grado: {self.grado}")


# Crear una instancia de la clase Estudiante
estudiante1 = Estudiante("Juan", 18, "12th")

# Imprimir los atributos utilizando el método de la clase Persona
estudiante1.imprimir_informacion()

# Imprimir el atributo adicional utilizando el método de la clase Estudiante
estudiante1.imprimir_grado()
