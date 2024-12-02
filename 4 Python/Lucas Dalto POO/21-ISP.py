# Interface segregation principle

from abc import ABC, abstractmethod

class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass

class Humano(Comedor, Trabajador, Durmiente):
    def comer(self):
        return "Comiendo con cubiertos"

    def trabajar(self):
        return "Trabajando en la oficina"

    def dormir(self):
        return "Durmiendo en la cama"

class Robot(Trabajador, Durmiente):
    def trabajar(self):
        return "Realizando tareas de automatización"

    def dormir(self):
        return "Apagando y recargando batería"


# Crear instancias de humano y robot
persona = Humano()
robot = Robot()

# Llamar a los métodos trabajar() de las instancias
print(persona.trabajar())
print(robot.trabajar())
