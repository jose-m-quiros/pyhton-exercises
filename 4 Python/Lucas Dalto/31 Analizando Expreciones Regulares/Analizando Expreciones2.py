import re

#La cadena en la que se buscaran los patrones
text = "La fecha es 23/06/2021 y el telefono es +1-555-555-5555"


#El patron a buscar
pattern = r"\d{2}/\d{2}/\d{4}"


#El texto con el que se remplazara el patron
replacement = "Fecha Oculta"


#Remplazar todas las apariciones del patron en la cadena de texto
new_text = re.sub(pattern, replacement, text)


print("Texto Modificado:", new_text)