# Enlaces estaticos:
#En python esto no es necesario

#conocidos como enlaces tempranos o enlaces estáticos de tiempo de compilación

#Es donde las referencias a funciones o métodos se resuelven en tiempo de compilación en lugar de en tiempo de ejecución.

#En Python, no se utiliza enlaces estáticos de manera directa, ya que Python 
# es un lenguaje de tipado dinámico y utiliza enlaces dinámicos para la resolución 
# de métodos y funciones en tiempo de ejecución. 




class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * self.radio * self.radio


# Función que calcula el área de un objeto de tipo Rectangulo o Circulo utilizando enlaces estáticos
def calcular_area(figure):
    if isinstance(figure, Rectangulo):
        return figure.area()
    elif isinstance(figure, Circulo):
        return figure.area()
    else:
        raise ValueError("Figura no válida")


# Crear instancias de Rectangulo y Circulo
rectangulo = Rectangulo(5, 10)
circulo = Circulo(3)

# Llamar a la función calcular_area con instancias de Rectangulo y Circulo
print(calcular_area(rectangulo))  # Salida: 50 (resultado del área del rectángulo)
print(calcular_area(circulo))    # Salida: 28.26 (resultado del área del círculo)


