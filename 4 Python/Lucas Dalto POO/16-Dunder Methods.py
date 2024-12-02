class Numero:
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return str(self.valor)

    def __add__(self, otro_numero):
        return Numero(self.valor + otro_numero.valor)

# Crear instancias de la clase Numero
numero1 = Numero(5)
numero2 = Numero(10)

# Usar el método especial __str__ para imprimir el número
print(numero1)  # Salida: 5

# Usar el método especial __add__ para sumar dos números
suma = numero1 + numero2
print(suma)  # Salida: 15
