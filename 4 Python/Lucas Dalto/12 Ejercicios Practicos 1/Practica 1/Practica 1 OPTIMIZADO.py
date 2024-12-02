#Promedio De Duracion Cursos

other_cursos_min = 2.5

other_cursos_max = 7

other_cursos_promedio = 4

Dalto_Python = 1.5

print("-----------------------------------Promedios---------------------------------------")

Diferencia_con_min = 100 - (Dalto_Python / other_cursos_min * 100)
print(f'El curso Del profe Dalto dura un {Diferencia_con_min}% menos que el mas rapido')
print("-----------------------------------------------------------------------------------")
print(" ")

# 
print("-----------------------------------Con Round()-------------------------------------")

Diferencia_con_max = round(100 - (Dalto_Python / other_cursos_max * 100), 2)
print(f'El curso Del profe Dalto dura un {Diferencia_con_max}% menos que el mas lento')
print("-----------------------------------------------------------------------------------")
print(" ")


print("-------------------------------------Promedio-------------------------------------")
Diferencia_con_promedio = 100 - (Dalto_Python / other_cursos_promedio * 100)
print(f'El curso Del profe Dalto dura un {Diferencia_con_promedio}% menos que el promedio')
print("-----------------------------------------------------------------------------------")
print(" ")



print("--------------------------------------Crudos---------------------------------------")
#Duracion De Crudos
crudo_promedio = 5
crudo_Dalto = 3.5 

tiempo_crudo = 100 - (other_cursos_promedio / crudo_promedio * 100)
print(f'El curso Del profe Dalto elimina un {tiempo_crudo}% de tiempo vacio')
print("-----------------------------------------------------------------------------------")
 
tiempo_crudo_dalto = round(100 - (Dalto_Python / crudo_Dalto * 100), 2)
print(f'Este curso elimina el {tiempo_crudo_dalto}% de tiempo vacio')

print("-----------------------------------------------------------------------------------")

print(" ")
print("---------------------Diferencia De Cursos Si fueran de 10 Horas--------------------")

other_promedio = round((other_cursos_promedio / Dalto_Python * 10), 2)                                                                            
print(f'Ver 10 horas de este curso equivale a ver {other_promedio} hora de otros cursos')

print("-----------------------------------------------------------------------------------")
other_promedio_dalto = round((Dalto_Python / other_cursos_promedio * 10), 2) 
print(f'Ver 10 horas de este curso equivale a ver {other_promedio_dalto} hora de otros cursos')