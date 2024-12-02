from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @abstractmethod
    def saludar(self):
        pass

class Estudiante(Persona):
    def saludar(self):
        print(f"Hola, soy {self.nombre} y soy un estudiante.")

class Profesor(Persona):
    def saludar(self):
        print(f"Hola, soy {self.nombre} y soy un profesor.")

# No se puede crear una instancia de la clase abstracta Persona
# persona = Persona("Juan", 25)

estudiante = Estudiante("Carlos", 20)
profesor = Profesor("Ana", 35)

estudiante.saludar()  # Salida: Hola, soy Carlos y soy un estudiante.
profesor.saludar()    # Salida: Hola, soy Ana y soy un profesor.


print(".....................")

#Segundo Ejemplo
from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def conducir(self):
        pass

class Auto(Vehiculo):
    def conducir(self):
        print(f"Conduciendo el auto {self.marca} {self.modelo}")

class Camion(Vehiculo):
    def conducir(self):
        print(f"Conduciendo el camión {self.marca} {self.modelo}")

# No se puede crear una instancia de la clase abstracta Vehiculo
# vehiculo = Vehiculo("Marca", "Modelo")

auto = Auto("Toyota", "Corolla")
camion = Camion("Volvo", "VNL")

auto.conducir()   # Salida: Conduciendo el auto Toyota Corolla
camion.conducir() # Salida: Conduciendo el camión Volvo VNL
