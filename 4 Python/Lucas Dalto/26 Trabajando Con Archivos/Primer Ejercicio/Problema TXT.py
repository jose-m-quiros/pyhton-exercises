#2 Listas, una con nombres y otra con apellidos.
Nombres = ["Jose", "Pedro", "Juan", "Alberto", "Roberto", "Emanuel"]
Apellidos = ["Mantequilla", "Alvares", "Quintero", "Landi", "Said", "Gazmey",]


#Registrar esta informacion en un TXT de forma optima

with open("26 Trabajando Con Archivos\\Primer Ejercicio\\Nombres y Apellidos.txt", "w") as Archivo:
    Archivo.writelines("Los Datos Son: \n \n")
    [Archivo.writelines(f"Nombre: {n}\nApellidos: {a}  \n\n---------------------\n\n") for n,a in zip(Nombres, Apellidos)]
