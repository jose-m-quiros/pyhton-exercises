#Todas las funciones que estan dentro de una clase se llaman metodos

#Clase
class Persona:
    #Funcion
    def __init__(self, nombre):
        self.nombre = nombre
    #Funcion
    def saludar(self):
        print(f"Hola, soy {self.nombre}. ¡Mucho gusto!")
        
        
    


#Example        
class Phone:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    def llamar(self):
        print(f"Estas llamando desde su {self.marca}")
        
    def cortar(self):
        print(f"Estas cortando desde su {self.marca}")
        

# Crear varias instancias de la clase Phone con diferentes atributos
phone1 = Phone("Xiaomi", "Note 8", "32MP")

# Imprimir atributos de las instancias
print(phone1.marca)  # Salida: Xiaomi

phone1.llamar()
phone1.cortar()



print("################################")

class Perro:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    def ladrar(self):
        print(f"{self.nombre}, un {self.raza}, está ladrando. ¡Guau, guau!")

    def dormir(self):
        print(f"{self.nombre}, un {self.raza}, está durmiendo. Zzzz...")

# Crear una instancia de la clase Perro
mi_perro = Perro("Max", "Golden Retriever", 2)

# Imprimir atributos de la instancia
print(mi_perro.nombre)  # Salida: Max
print(mi_perro.raza)    # Salida: Golden Retriever

# Llamar a los métodos
mi_perro.ladrar()
mi_perro.dormir()
