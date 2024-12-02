class Phone():
    marca = "Xiaomi"
    modelo = "Note 8"
    camara = "32MP"

phone1 = Phone()
phone2 = Phone()
phone3 = Phone()
phone4 = Phone()

print(phone2.modelo)  # Salida: Note 8

phone3.camara = "43MP"
print(phone3.camara)  # Salida: 43MP

# Imprimir atributos de otras instancias
print(phone1.marca)  # Salida: Xiaomi
print(phone4.modelo)  # Salida: Note 8 (el atributo es el mismo para todas las instancias)

# Modificar atributo de clase
Phone.marca = "Samsung"

# Imprimir atributos de las instancias después de modificar el atributo de clase
print(phone1.marca)  # Salida: Samsung
print(phone2.marca)  # Salida: Samsung
print(phone3.marca)  # Salida: Samsung
print(phone4.marca)  # Salida: Samsung
