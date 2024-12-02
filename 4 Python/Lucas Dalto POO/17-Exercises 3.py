class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
        
    def __repr__(self):
        return f"{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})"

    def __add__(self, otro_pj):
        new_name = self.nombre + "-" + otro_pj.nombre
        new_fuerza = round(((self.fuerza + otro_pj.fuerza) / 2) ** 1.34)
        new_velocidad = round(((self.velocidad + otro_pj.velocidad) / 2) ** 1.34)
        return Personaje(new_name, new_fuerza, new_velocidad)

goku = Personaje("Goku", 110, 100)
vegeta = Personaje("Vegeta", 100, 110)
majinbu = Personaje("Majinbu", 90, 210)

gogeta = goku + vegeta
majinta = gogeta + majinbu

print(gogeta)
print(majinta)
