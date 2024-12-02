# Dependency Inversion Principle

from abc import ABC, abstractmethod

# Clase abstracta de dispositivos


class Dispositivo(ABC):
    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

# Clase abstracta de interruptores


class Interruptor(ABC):
    @abstractmethod
    def activar(self, dispositivo):
        pass

# Clase concreta de un dispositivo: una bombilla


class Bombilla(Dispositivo):
    def encender(self):
        return "Bombilla encendida"

    def apagar(self):
        return "Bombilla apagada"

# Clase concreta de un interruptor manual


class InterruptorManual(Interruptor):
    def activar(self, dispositivo):
        return f"Interruptor manual activado: {dispositivo.encender()}"

# Clase concreta de un interruptor de voz


class InterruptorVoz(Interruptor):
    def activar(self, dispositivo):
        return f"Interruptor de voz activado: {dispositivo.encender()}"

# Función que activa un interruptor


def activar_interruptor(interruptor, dispositivo):
    return interruptor.activar(dispositivo)


# Crear instancias de dispositivos y interruptores
bombilla = Bombilla()
interruptor_manual = InterruptorManual()
interruptor_voz = InterruptorVoz()

# Activar interruptores con dispositivos utilizando el Principio de Inversión de Dependencia
print(activar_interruptor(interruptor_manual, bombilla))
print(activar_interruptor(interruptor_voz, bombilla))


print("--------------------------------")

# Segundo ejemplo

from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass

class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        # Lógica para verificar palabras en el diccionario
        # Por ejemplo, aquí simplemente retornamos la palabra sin cambios
        return palabra

class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador

    def corregir_texto(self, texto):
        palabras = texto.split()
        palabras_corregidas = []

        for palabra in palabras:
            palabra_corregida = self.verificador.verificar_palabra(palabra)
            palabras_corregidas.append(palabra_corregida)

        return ' '.join(palabras_corregidas)


class ServicioWeb(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        # Lógica para verificar palabras a través de un servicio web
        # Por ejemplo, aquí simplemente retornamos la palabra en mayúsculas
        return palabra.upper()


# Crear instancias de las clases
diccionario = Diccionario()
corrector_con_diccionario = CorrectorOrtografico(diccionario)

servicio_web = ServicioWeb()
corrector_con_servicio_web = CorrectorOrtografico(servicio_web)

# Ejemplo de uso
texto_para_corregir = "Hola mundoo, cómo estas?"
texto_corregido_diccionario = corrector_con_diccionario.corregir_texto(texto_para_corregir)
texto_corregido_servicio_web = corrector_con_servicio_web.corregir_texto(texto_para_corregir)

print("Texto corregido usando diccionario:", texto_corregido_diccionario)
print("Texto corregido usando servicio web:", texto_corregido_servicio_web)
