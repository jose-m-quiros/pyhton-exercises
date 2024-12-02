import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df =  pd.read_csv("27 Graficos\\Grafico 2\\Cofla.csv")


#Esto es para poder dibujar la grafica
fig, ax = plt.subplots()
sns.barplot(x="Fuente", y="Ingresos", data=df)


#Obteniendo el total de ingresos con .sum()
total_ingresos = df["Ingresos"].sum()


# Agregar el texto con el total de ingresos en el gráfico
for i, v in enumerate(df['Ingresos']):
    ax.text(i, v + 50, str(v), color='black', ha='center')


plt.title('Ingresos de Cofla')
plt.xlabel('\nFuente')
plt.ylabel('Ingresos (USD)')


# Mostrar el total de ingresos en el gráfico
# Los numeros es para poder acomodar el texto de: total_ingresos donde a uno le guste mas
# Y ha="center" es para el tipo de alineacion
plt.text(2, 3000, f'Total de ingresos: ${total_ingresos} USD', ha='center')


plt.show()