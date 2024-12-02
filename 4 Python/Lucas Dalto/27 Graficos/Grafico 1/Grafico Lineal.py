import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df =  pd.read_csv("27 Graficos\\Grafico 1\\Goles.csv")
print(df)

#Esto es para poder dibujar la grafica
sns.lineplot(x="Fecha", y="Goles", data=df)


#Buscando la fecha con mas goles de la tabla para mostrarla en la grafica
max_idx = df['Goles'].argmax()
max_goles = df.loc[max_idx, 'Goles']
max_fecha = df.loc[max_idx, 'Fecha']
plt.plot(max_fecha, max_goles, marker='o', markersize=5, color='red')


#Buscando el punto medio de la tabla
# Encontrar el punto en la mitad de los datos
mid_idx = len(df) // 2
mid_goles = df.sort_values('Goles').iloc[mid_idx]['Goles']
mid_fecha = df.sort_values('Goles').iloc[mid_idx]['Fecha']

# Plot de la gráfica
sns.lineplot(x="Fecha", y="Goles", data=df.sort_values('Goles'))

# Marcar el punto en la mitad con un círculo
plt.plot(mid_fecha, mid_goles, marker='o', markersize=5, color='red')



#Buscando la fecha con menos goles de la tabla
min_idx = df['Goles'].argmin()
min_goles = df.loc[min_idx, 'Goles']
min_fecha = df.loc[min_idx, 'Fecha']
plt.plot(min_fecha, min_goles, marker='o', markersize=5, color='red')


plt.plot()

plt.show()