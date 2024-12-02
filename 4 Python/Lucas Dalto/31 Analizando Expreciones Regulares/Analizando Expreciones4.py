import re

email = "jqchaves1928@gmail.com"

pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

result = re.match(pattern, email)

if result:
    print("La dirección de correo electrónico es válida")
else:
    print("La dirección de correo electrónico no es válida")



# ^ indica el inicio de la cadena.
# [a-zA-Z0-9._%+-]+ se refiere a una o más letras (mayúsculas o minúsculas), dígitos o los caracteres especiales ._%+-
# @ es el caracter literal @
# [a-zA-Z0-9.-]+ se refiere a una o más letras (mayúsculas o minúsculas), dígitos o el caracter especial - seguido por el caracter literal .
# [a-zA-Z]{2,} se refiere a dos o más letras (mayúsculas o minúsculas) para el dominio (por ejemplo, com, edu, gov, etc.).
# $ indica el final de la cadena.