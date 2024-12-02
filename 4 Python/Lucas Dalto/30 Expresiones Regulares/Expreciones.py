import re

texto = """Que como te va con el curso 1. Pollo Asado.
Esto es ya casi el final del curso entonces aprovechalo ya que se viene la 23.
Este es la tercer linea de este curso pero es un disque parrafo con 1 3 21 Asado.
Este es la cuarta abbbbb abbb abb ab linea de este curso pero es un disque parrafo con 1 3 21 333 1000 33233 Asado.
Esto es ababababababababa ya que se viene la 23.
"""

print(".........Resultado 1.........")
#Este re.search("Lo que hace es encontrar el primer elemento que tenga esa considencia")
resultado = re.search("", texto)
print(resultado)

print("---------------------")

print(".........Resultado 2.........")
#Este lo que hace es re.findall("Mostrar todos los resultados con esa concidencia")
resultado2 = re.findall("curso", texto)
print(resultado2)

print("---------------------")

print(".........Resultado 3.........")
#\d -> busca digitos numericos del 0-9
resultado3 = re.findall(r"\d",texto)
print(resultado3)

print("---------------------")

print(".........Resultado 4.........")
#\D -> busca TODO MENOS digitos numericos del 0-9
resultado4 = re.findall(r"\D",texto)
print(resultado4)

print("---------------------")

print(".........Resultado 5.........")
#\w -> busca caracteres alfanumericos [a-z A-Z 0-9 _]
resultado5 = re.findall(r"\w",texto)
print(resultado5)

print("---------------------")

print(".........Resultado 6.........")
#\W -> busca TODO MENOS caracteres alfanumericos [a-z A-Z 0-9 _]
resultado6 = re.findall(r"\W",texto)
print(resultado6)

print("---------------------")

print(".........Resultado 7.........")
#\s -> busca espacios en blanco -> espacios, tabs, saltos de linea
resultado7 = re.findall(r"\s",texto)
print(resultado7)

print("---------------------")

print(".........Resultado 8.........")
#\S -> busca TODO MENOS espacios en blanco -> espacios, tabs, saltos de linea
resultado8 = re.findall(r"\S",texto)
print(resultado8)

print("---------------------")

print(".........Resultado 9.........")
#. -> busca saltos de linea
resultado9 = re.findall(r"\n",texto)
print(resultado9)

print("---------------------")

print(".........Resultado 10.........")
#. -> busca TODO MENOS saltos de linea
resultado10 = re.findall(r".",texto)
print(resultado10)

print("---------------------")

print(".........Resultado 11.........")
#\ -> cancela caracteres especiales
#Cancelando la funcion del punto y buscando puntos
resultado11 = re.findall(r"\.",texto)
print(resultado11)

print("---------------------")

#De aqui en adelande se estan usando \(barra invertida) varias para ser mas especifico con lo que se esta buscando | "re.findall(r"\d\s\.")"
print(".........Resultado 12.........")
#Armando una cadena que busque un numero, seguido de un punto y un espacio
resultado12 = re.findall(r"\d\.\s",texto)
print(resultado12)

print("---------------------")

print(".........Resultado 13 & 13_2.........")
#^ -> Busca el comienzo de una linea
resultado13 = re.findall(r"^Que",texto)
#flags=re.M = activa la multilinea
resultado13_2 = re.findall(r"^Pollo",texto, flags=re.M)#No lo va a encontar ya que no se encuentra al principio de la linea
print(resultado13)
print(resultado13_2)

print(".........Resultado 14.........")
#$ -> Busca el final de una linea
resultado14 = re.findall(r"Asado.$",texto)
print(resultado14)

print(".........Resultado 15.........")
#{n} -> Busca n cantidad de veces el valor de la izquierda
resultado15 = re.findall(r"\d",texto)
resultado15_2 = re.findall(r"\d{2}\s",texto)
print(resultado15)
print(resultado15_2)

print(".........Resultado 16.........")
#{n, m} -> al menos n, como maximo m
resultado16 = re.findall(r"\d{2,4}",texto)

#Lo que estamos buscando es una concidencia de la letra ab y que si b tiene entre 2 y 4 b juntas se pueda mostar
resultado16_2 = re.findall(r"ab{2,4}",texto)


#PERO si enceramos (ab) va a buscar las 2 letras por igual
#Lo que pasa es que nos esta devolviendo un ab cada ves que encuentra el ab x 2 | Si encontras 2 veces el ab juntos devuelveme solo un ab
# resultado16_3 = re.findall(r"(ab){3,2}",texto)
resultado16_3 = re.findall(r"(ab){2}",texto)

#Si le ponemos corchetes, nos va a devolver todos los que encuentren | Los corchetes sirven en este caso para decir que se va aplicar tanto a y b
resultado16_4 = re.findall(r"[ab]{2}",texto)

print(resultado16)
print(resultado16_2)
print(resultado16_3)
print(resultado16_4)

print(".........Resultado 17.........")
# | -> Busca  una cosa o la otra
#Lo va a mostar con forme lo encuentre en la cadena de texto
resultado17 = re.findall(r"\d{2,4}|Hola",texto)
print(resultado17)