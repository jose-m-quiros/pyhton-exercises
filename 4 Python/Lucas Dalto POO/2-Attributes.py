#First Example
class Phone:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

# Crear varias instancias de la clase Phone con diferentes atributos
phone1 = Phone("Xiaomi", "Note 8", "32MP")
phone2 = Phone("Samsung", "Galaxy S20", "64MP")
phone3 = Phone("Apple", "iPhone 15", "52MP")

# Imprimir atributos de las instancias
print(phone1.marca)  # Salida: Xiaomi
print(phone2.modelo)  # Salida: Galaxy S20
print(phone3.camara)  # Salida: 12MP

print("#################################")

#Second Example
class Animal:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

# Crear varias instancias de la clase Animal con diferentes atributos
animal1 = Animal("Leo", "León", 5)
animal2 = Animal("Max", "Perro", 3)
animal3 = Animal("Whiskers", "Gato", 2)

# Imprimir atributos de las instancias
print(f"{animal1.nombre}, es un {animal1.especie}, y tiene {animal1.edad} años.")
print(f"{animal2.nombre}, es un {animal2.especie}, y tiene {animal2.edad} años.")
print(f"{animal3.nombre}, es un {animal3.especie}, y tiene {animal3.edad} años.")
