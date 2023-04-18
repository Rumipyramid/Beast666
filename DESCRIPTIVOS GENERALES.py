import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats
df = pd.read_csv("Sponsors_IdL2 - Sheet1.csv")
X= "IG"
Y= "Twitter"
Z= "País"
#Z1=

#Estadísticos descriptivos generales
DG1=round(df.describe())
DG2=round(df.describe(include=['object']))


#Contar valores repetidos
DG3=df['País'].value_counts().to_frame()


print("DESCRIPTIVOS GENERALES")
print(DG1)
print("VALORES REPETIDOS")
print(DG2)
print("RECUENTO DE CASOS")
print(DG3)

#Aislar columnas
df_group_one = df[[X,Y,Z]]
df_group_one.head(30)

df_group_one2 = df_group_one.groupby([Z],as_index=False).mean()
df_group_one

print("MEDIAS AGRUPADAS")
print(round(df_group_one2))

#Agrupar por variables categóricas

#grouped_pivot = df.pivot(index='Continente',columns='País')
#grouped_pivot

#Mapa de calor de variables agrupadas
#plt.pcolor(grouped_pivot)
#plt.colorbar()
#3plt.show()

#Correlaciones
print("CORRELACIONES")
corr = df_group_one2.corr()
print(corr)

#Coeficiente Pearson
print("COEFICIENTE DE PEARSON")
pearson_coef, p_value = stats.pearsonr(df[X], df[Y])
print("El coeficiente de correlación de Pearson es", pearson_coef, " con un valor P de P =", p_value)

DG1prime=DG1.iloc[:,0]
print(DG1prime)
corte25= DG1[DG1prime]=="25%"
filtro=df[(df["IG"]==corte25) & (df["País"]=="Brasil")]
#print(filtro.value_counts(filtro["IG"]))
print(filtro)



plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True)
plt.show()
