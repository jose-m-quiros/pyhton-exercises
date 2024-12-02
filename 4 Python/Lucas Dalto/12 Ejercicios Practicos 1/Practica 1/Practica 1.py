#Promedio De Duracion Cursos

other_cursos_min = 2.5

other_cursos_max = 7

other_cursos_promedio = 4

Dalto_Python = 1.5

print("-----------------------------------Promedios---------------------------------------")

Diferencia_con_min = 100 - (Dalto_Python / other_cursos_min * 100)
print(f'El curso Del profe Dalto dura un {Diferencia_con_min}% menos que el mas rapido')
print("-----------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------")
print(" ")

print("----------------------------------1 | Normal---------------------------------")
#Varias Formas de hacerlo
Diferencia_con_max = 100 - (Dalto_Python / other_cursos_max * 100)
print(f'El curso Del profe Dalto dura un {Diferencia_con_max}% menos que el mas lento')
print(" ")


print("---------------------2 | Multiplicacion y Division Doble---------------------")

Diferencia_con_max = 100 - (Dalto_Python * 1000 // other_cursos_max / 10)
print(f'El curso Del profe Dalto dura un {Diferencia_con_max}% menos que el mas lento')
print(" ")


print("-------------------------------------3 | INT---------------------------------")
Diferencia_con_El_Max = int(Diferencia_con_max)
print(f'El curso Del profe Dalto dura un {Diferencia_con_El_Max}% menos que el mas lento')

print("-----------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------")
print(" ")

Diferencia_con_promedio = 100 - (Dalto_Python / other_cursos_promedio * 100)
print(f'El curso Del profe Dalto dura un {Diferencia_con_promedio}% menos que el promedio')




print("-----------------------------------------------------------------------------------")
print(" ")
print("-----------------------------------------------------------------------------------")
print(" ")
print("--------------------------------------Crudos---------------------------------------")

#Duracion De Crudos
crudo_promedio = 5
crudo_Dalto = 3.5 

tiempo_crudo = 100 - (other_cursos_promedio * 1000 // crudo_promedio / 10)
print(f'El curso Del profe Dalto elimina un {tiempo_crudo}% de tiempo vacio')

print("-----------------------------------------------------------------------------------")

tiempo_crudo_dalto = 100 - (Dalto_Python * 1000 // crudo_Dalto / 10)
print(f'Este curso elimina el {tiempo_crudo_dalto}% de tiempo vacio')


print("-----------------------------------------------------------------------------------")
print(" ")
print("-----------------------------------------------------------------------------------")
print(" ")
print("---------------------Diferencia De Cursos Si fueran de 10 Horas--------------------")

                                                                            
print(f'Ver 10 horas de este curso equivale a ver {other_cursos_promedio * 1000 // Dalto_Python  / 100} hora de otros cursos')

print("-----------------------------------------------------------------------------------")

print(f'Ver 10 horas de este curso equivale a ver {Dalto_Python * 100 // other_cursos_promedio / 10} hora de otros cursos')










print(" ")
print(" ")