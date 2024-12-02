import re

text = "The quick brown fox jumps over the lazy dog"

x = re.search("^The.*dog$", text)

if x:
    print("Yes")
else:
    print("No")
    
    
    
# La variable text contiene la cadena de texto que se va a buscar.
# ^The significa que la cadena debe comenzar con "The".
# .* significa que hay cero o más caracteres de cualquier tipo entre "The" y "dog".
# $ significa que la cadena debe terminar con "dog".
# La función re.search() busca la cadena text para encontrar una coincidencia con el patrón especificado.
# Si la función re.search() encuentra una coincidencia, se imprime "Yes", de lo contrario se imprime "No".