class Gato():
    def sonido(self):
        return "Mius"


class Perro():
    def sonido(self):
        return "Guau"


def hacer_sonido(animal):
    print(animal.sonido())


gato = Gato()

perro = Perro()

# 2 Tipos de polimorfismo

# Aqui cambia el objeto para el metodo.
print(gato.sonido())
print(perro.sonido())

# Polimorfismo de funcion
# Aqui cambia el argumento para la función.
hacer_sonido(gato)
hacer_sonido(perro)


print("__________________________________________")
print("")

print("Another example of polymorphism")
#Another example of polymorphism
def recorrer(elemento):
    for item in elemento:
        print(f"The current element: {item}")


list = [1, 2, 3, 4, 5, 6]
list2 = "Jose Manuel"

recorrer(list)
print("")
recorrer(list2)