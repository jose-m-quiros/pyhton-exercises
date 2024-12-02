class Animal:
    def comer(self):
        print("El animal está comiendo.")


class Mamifero(Animal):
    def amamantar(self):
        print("El mamífero está amamantando.")


class Ave(Animal):
    def volar(self):
        print("El ave está volando.")


class Murcielago(Mamifero, Ave):
    pass


# Crear una instancia de Murcielago y probar los métodos
murcielago1 = Murcielago()

# Llamada directa a los métodos de las clases base
murcielago1.comer()    # El animal está comiendo.
murcielago1.amamantar()    # El mamífero está amamantando.
murcielago1.volar()    # El ave está volando.

print("MRO (Method Resolution Order) de Murcielago:", Murcielago.mro())

# Cambiar el orden de herencia a (Ave, Mamifero) y observar los cambios en el MRO y el comportamiento
class MurcielagoAvePrimero(Ave, Mamifero):
    def comportamiento(self):
        print("El murciélago tiene un comportamiento particular, pero Ave está primero.")


murcielago2 = MurcielagoAvePrimero()

murcielago2.comer()    # El animal está comiendo.
murcielago2.amamantar()    # El ave está amamantando. (Se toma el método de la clase Ave, porque es la primera en el orden de herencia)
murcielago2.volar()    # El ave está volando.

print("MRO (Method Resolution Order) de MurcielagoAvePrimero:", MurcielagoAvePrimero.mro())
