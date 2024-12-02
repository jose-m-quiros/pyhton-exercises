print("------1------")
# Primera Prueba
ingreso_mensual = 100000

if ingreso_mensual > 10000:
    print("Estas bien en cualquier parte del mundo")
# el else-if SE ESCRIBE elif
elif ingreso_mensual > 1000:
    print("Estas bien en C.R")
else:
    print("Papi busque trabajo porque estamos mal sin plata")
print("-------------------------------------------------")




print("------2------")
# Segunda Prueba
ingreso_mensual2 = 10000

if ingreso_mensual2 > 10000:
    print("Te puedes quedar un buen tiempo en Dubai")
# el else-if SE ESCRIBE elif
elif ingreso_mensual2 > 1000:
    print("Estas bien en C.R")
else:
    print("Papi busque trabajo porque estamos mal sin plata")
print("-------------------------------------------------")




print("------3------")
# Tercera Prueba
ingreso_mensual3 = 1000

if ingreso_mensual3 > 10000:
    print("Estas bien en cualquier parte del mundo")
# el else-if SE ESCRIBE elif
elif ingreso_mensual3 > 1000:
    print("Estas bien en C.R")
else:
    print("Papi busque trabajo porque estamos mal sin plata")
print("-------------------------------------------------")
print("-------------------------------------------------")



print("------4------")
# Esta prueba es con varios else if
ingreso_mensual4 = 1500

if ingreso_mensual4 > 10000:
    print("Esto es una prueba con else if")

# el else-if SE ESCRIBE elif
elif ingreso_mensual4 > 5000:
    print("Estas bien en C.R")

elif ingreso_mensual4 > 4000:
    print("Estas bien en Chile")

elif ingreso_mensual4 > 3000:
    print("Estas bien en Colombia")

elif ingreso_mensual4 > 2000:
    print("Estas bien en Camerun")

elif ingreso_mensual4 > 1000:
    print("Estas bien en Argentina")

else:
    print("Papi busque trabajo porque estamos mal sin plata")

print("-------------------------------------------------")




print("------5------")
# Otro Tipo: if anidados | Es decir que hay un if dentro de otro if
ingreso_mensual4 = 120000
gastos_mensuales = 2000

# ingreso_mensual4 = 72000
# gastos_mensuales = 8000

if ingreso_mensual4 > 10000:
    if gastos_mensuales < 7000:
        print("Como Andamos")
    else:
        print("Porfavor no gastes mucho, reduse tus gastos")

elif ingreso_mensual4 > 5000:
    print("Estas bien en Venezuela")

elif ingreso_mensual4 > 1000:
    print("Estas bien en Pollo Landia")

else:
    print("TRABAJE")

print("-------------------------------------------------")




print("------6------")
#If anidados y else if (elif)
ingreso_mensuales5 = 81000
gastos_mensuales5 = 80000

if ingreso_mensuales5 > 10000:
    if ingreso_mensuales5 - gastos_mensuales5 < 0:
        print("Estas en Deficit")
    elif ingreso_mensuales5 - gastos_mensuales5 > 3000:
        print("Estas Bien")
    else:
        print("Reduce gastos porque te vas a quedar en la calle")

elif ingreso_mensuales5 > 2000:
    print("Estas bien en C.R")
else:
    print("BUSQUE TRABAJO URGENTE")

print("-------------------------------------------------")
