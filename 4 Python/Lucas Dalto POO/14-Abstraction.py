class  Auto():
    def __init__(self):
        self._estado = "Apagado"
        
        
    def encender(self):
        self._estado = "Encendido"
        print("El auto esta encendido")
        
    def conducir(self):
        if self._estado == "Apagado":
            self.encender()
        print("Conduciendo el auto")
            
            
Mi_Auto = Auto()
Mi_Auto.conducir()
