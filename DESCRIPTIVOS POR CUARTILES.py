import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
df = pd.read_csv("Sponsors_IdL2 - Sheet1.csv")
A="Equipo"
X= "IG"
Y= "Twitter"
Z= "País"
Z1= ["Sponsor 1","Sponsor 2","Sponsor 3","Sponsor 4","Sponsor 5","Sponsor 6","Sponsor 7","Sponsor 8","Sponsor 9","Sponsor 10","Sponsor 11","Sponsor 12"]
#df["sponsors"] = df["Sponsor 1"].map(str) + "-" + df["Sponsor 2"]+ "-" + df["Sponsor 3"] \
                 #+ "-" + df["Sponsor 4"]+ "-" + df["Sponsor 5"]+ "-" + df["Sponsor 6"]+ "-" + df["Sponsor 7"] \
                 #+ "-" + df["Sponsor 8"]+ "-" + df["Sponsor 9"]+ "-" + df["Sponsor 10"]+ "-" + df["Sponsor 11"]+ "-" + df["Sponsor 12"]



df_grupo1=df[[X,Y,Z]]
df_grupo2=df[[A,X,Y,Z]]
df_grupo3=[[df_grupo2,df[Z1]]]


#Estadísticos descriptivos generales

DG=round(df.describe())
DG1=round(df_grupo1.IG.describe().loc["25%"])
DG2=round(df_grupo1.IG.describe().loc["50%"])
DG3=round(df_grupo1.IG.describe().loc["75%"])
print(DG)
print("25%: ",DG1)
print("50%: ",DG2)
print("75%: ",DG3)

ulti_element=max(df.IG)

DGE1=df_grupo2.IG.isin(range(0,DG1))
DGE2=df_grupo2.IG.isin(range(DG1,DG2))
DGE3=df_grupo2.IG.isin(range(DG2,DG3))
DGE4=df_grupo2.IG.isin(range(DG3,ulti_element))

df_n1= df_grupo2[DGE1]
df_n2= df_grupo2[DGE2]
df_n3= df_grupo2[DGE3]
df_n4= df_grupo2[DGE4]

print("Equipos 1/4")
print(df_n1)
print("Descriptivos")
print(round(df_n1.IG.describe()))
print("Equipos 2/4")
print(df_n2)
print("Descriptivos")
print(round(df_n2.IG.describe()))
print("Equipos 3/4")
print(df_n3)
print("Descriptivos")
print(round(df_n3.IG.describe()))
print("Equipos 4/4")
print(df_n4)
print("Descriptivos")
print(round(df_n4.IG.describe()))

print(df_grupo3.Z1)


#print(df_grupo2[DGE2])
