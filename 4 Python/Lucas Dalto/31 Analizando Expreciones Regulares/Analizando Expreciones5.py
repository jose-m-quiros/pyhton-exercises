import re

text = "Este es un ejemplo de pagina web: https://www.youtube.com/watch?v=GlP-SitTbG4 y tambien puedes ver el video."

pattern = "https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" 

result = re.findall(pattern, text)

print(result)