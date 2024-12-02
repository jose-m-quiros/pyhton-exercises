# Enlaces dinamicos:

#conocidos como enlaces tardíos o enlaces polimórficos

#permiten que el comportamiento de un programa se determine en tiempo de ejecución, 
# lo que brinda flexibilidad y adaptabilidad al código, y es fundamental para lograr 
# el polimorfismo en la programación orientada a objetos.


class Animal:
    def hacer_sonido(self):
        return "Sonido genérico de animal."


class Gato(Animal):
    def hacer_sonido(self):
        return "Miau, miau."


class Perro(Animal):
    def hacer_sonido(self):
        return "Guau, guau."


# Función que toma un objeto y llama al método hacer_sonido()
def sonido_animal(animal):
    return animal.hacer_sonido()


# Crear instancias de las clases Gato y Perro
gato = Gato()
perro = Perro()

# Llamar a la función sonido_animal() con instancias de Gato y Perro
print(sonido_animal(gato))  # Salida: Miau, miau.
print(sonido_animal(perro))  # Salida: Guau, guau.


#Sin embargo, esta función no necesita preocuparse por el tipo específico del 
# objeto que se le pasa, ya que los enlaces dinámicos permiten que el método 
# hacer_sonido() apropiado se determine en tiempo de ejecución según el tipo real del objeto.