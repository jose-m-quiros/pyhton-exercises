#Liskov's substitution principle

class Figura:
    def calcular_area(self):
        pass

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

def imprimir_area(figura):
    print(f"Área: {figura.calcular_area()}")

# Crear instancias de las clases Rectangulo y Cuadrado
rectangulo = Rectangulo(5, 10)
cuadrado = Cuadrado(7)

# Imprimir áreas utilizando el principio de LSP
imprimir_area(rectangulo)
imprimir_area(cuadrado)
