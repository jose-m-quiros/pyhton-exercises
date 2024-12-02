class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"Cometiste el siguiente error: {err}")
        
try:
    raise MiExcepcion("Revisa tu codigo")

except:
    print("Colaboracion Gracias a CyberStyle Web")

print("")
print("")    

raise MiExcepcion("Revisa tu codigo")