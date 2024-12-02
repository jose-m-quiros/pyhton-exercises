# Duck Typing:

# Tratan el tipo de un objeto basándose en su comportamiento en lugar de su tipo explícito. 
# La idea detrás de duck typing es que "si camina como un pato, nada como un pato y suena como un pato, entonces es un pato".


# Definir una función que acepta cualquier objeto que tenga el método "hacer_sonido"
def hacer_sonido(animal):
    return animal.hacer_sonido()

# Definir dos clases que no están relacionadas por herencia, pero tienen el método "hacer_sonido"
class Gato:
    def hacer_sonido(self):
        return "Miau"

class Pato:
    def hacer_sonido(self):
        return "Cuack"

# Crear instancias de las clases Gato y Pato
gato = Gato()
pato = Pato()

# Llamar a la función hacer_sonido con ambas instancias
print(hacer_sonido(gato))  # Salida: Miau
print(hacer_sonido(pato))  # Salida: Cuack


#El duck typing nos permite utilizar objetos de diferentes clases en la función hacer_sonido() 
# siempre y cuando tengan el comportamiento necesario (en este caso, el método hacer_sonido). 
# Esto hace que el código sea más flexible y genérico.
