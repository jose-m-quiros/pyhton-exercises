import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df =  pd.read_csv("27 Graficos\\Grafico 3\\Dispersion.csv")


sns.scatterplot(x="Tiempo", y="Dinero", data=df)


plt.show()