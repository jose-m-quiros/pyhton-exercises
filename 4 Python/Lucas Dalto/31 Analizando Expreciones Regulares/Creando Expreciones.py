import re

#Detectando un numero CABA y ocultandolo
texto = "Hola Dalto mi numero es +506 63 86 86 08"

pattern = r'\+\d{3}\s\d{2}\s\d{2}\s\d{2}\s\d{2}'

remplazo = re.sub(pattern, "(Numero Ocultado) ", texto)

print(remplazo)