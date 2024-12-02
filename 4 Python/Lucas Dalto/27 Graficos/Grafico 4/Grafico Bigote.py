import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df =  pd.read_csv("27 Graficos\\Grafico 4\\Bigote.csv")


sns.boxplot(x="Categoria", y="Valor", data=df)


plt.show()