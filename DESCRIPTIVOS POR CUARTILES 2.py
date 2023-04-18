import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
from collections import Counter
from wordcloud import WordCloud

df = pd.read_csv("Sponsors_IdL2 - Sheet1.csv")

Z1= ["Sponsor 1","Sponsor 2","Sponsor 3","Sponsor 4", \
     "Sponsor 5","Sponsor 6","Sponsor 7","Sponsor 8","Sponsor 9", \
     "Sponsor 10","Sponsor 11","Sponsor 12"]

df['combinedS'] = [[e for e in row if e==e] for row in df[Z1].values.tolist()]

df = df.drop(columns=["Sponsor 1","Sponsor 2","Sponsor 3","Sponsor 4", \
     "Sponsor 5","Sponsor 6","Sponsor 7","Sponsor 8","Sponsor 9", \
     "Sponsor 10","Sponsor 11","Sponsor 12","Diferencia IG/T","Continente","Unnamed: 0"])

counter = Counter(sum(df['combinedS'], []))
for element, count in counter.items():
    print(element, count)

x = [k for k, v in counter.items() if v > 2]
y = [v for k, v in counter.items() if v > 2]

plt.bar(x, y)
plt.xlabel('Sponsors')
plt.ylabel('Recuento')
plt.title('Recuento de elementos repetidos')
plt.show()

nube_palabras = WordCloud(background_color='white').generate_from_frequencies(counter)
plt.imshow(nube_palabras, interpolation='bilinear')
plt.axis("off")
plt.show()


DG1=round(df.IG.describe().loc["25%"])
DG2=round(df.IG.describe().loc["50%"])
DG3=round(df.IG.describe().loc["75%"])
print("25%: ",DG1)
print("50%: ",DG2)
print("75%: ",DG3)

ulti_element=max(df.IG)

DGE1=df.IG.isin(range(0,DG1))
DGE2=df.IG.isin(range(DG1,DG2))
DGE3=df.IG.isin(range(DG2,DG3))
DGE4=df.IG.isin(range(DG3,ulti_element))

df_n1= df[DGE1]
df_n2= df[DGE2]
df_n3= df[DGE3]
df_n4= df[DGE4]

#==========================================================================
print("TIER 1")
print (df_n1.iloc[:,0:4].sort_values("IG", ascending=False))

counter = Counter(sum(df_n1['combinedS'], []))
for element, count in counter.items():
    print(element, count)


df_n1.iloc[:,0:4].sort_values("IG", ascending=False).to_html('tabla.html', index=False)

#x = [k for k, v in counter.items() if v > 1]
#y = [v for k, v in counter.items() if v > 1]

#plt.bar(x, y)
#plt.xlabel('Sponsors')
#plt.ylabel('Recuento')
#plt.title('Recuento de elementos repetidos')
#plt.show()

x = [k for k, v in counter.items() if v > 1]
y = [v for k, v in counter.items() if v > 1]

plt.bar(x, y)
plt.xlabel('Sponsors')
plt.ylabel('Recuento')
plt.title('Recuento de elementos repetidos')
plt.show()

nube_palabras = WordCloud(background_color='white').generate_from_frequencies(counter)
plt.imshow(nube_palabras, interpolation='bilinear')
plt.axis("off")
plt.show()

#==========================================================================
print("TIER 2")
print (df_n2.iloc[:,0:4].sort_values("IG", ascending=False))

counter = Counter(sum(df_n2['combinedS'], []))
for element, count in counter.items():
    print(element, count)

df_n2.iloc[:,0:4].sort_values("IG", ascending=False).to_html('tabla2.html', index=False)

x = [k for k, v in counter.items() if v > 1]
y = [v for k, v in counter.items() if v > 1]

plt.bar(x, y)
plt.xlabel('Sponsors')
plt.ylabel('Recuento')
plt.title('Recuento de elementos repetidos')
plt.show()

nube_palabras = WordCloud(background_color='white').generate_from_frequencies(counter)
plt.imshow(nube_palabras, interpolation='bilinear')
plt.axis("off")
plt.show()

#==========================================================================
print("TIER 3")
print (df_n3.iloc[:,0:4].sort_values("IG", ascending=False))

counter = Counter(sum(df_n3['combinedS'], []))
for element, count in counter.items():
    print(element, count)

df_n3.iloc[:,0:4].sort_values("IG", ascending=False).to_html('tabla3.html', index=False)

x = [k for k, v in counter.items() if v > 1]
y = [v for k, v in counter.items() if v > 1]

plt.bar(x, y)
plt.xlabel('Sponsors')
plt.ylabel('Recuento')
plt.title('Recuento de elementos repetidos')
plt.show()

nube_palabras = WordCloud(background_color='white').generate_from_frequencies(counter)
plt.imshow(nube_palabras, interpolation='bilinear')
plt.axis("off")
plt.show()

#==========================================================================
print("TIER 4")
print (df_n4.iloc[:,0:4].sort_values("IG", ascending=False))

counter = Counter(sum(df_n4['combinedS'], []))
for element, count in counter.items():
    print(element, count)

df_n4.iloc[:,0:4].sort_values("IG", ascending=False).to_html('tabla4.html', index=False)

x = [k for k, v in counter.items() if v > 1]
y = [v for k, v in counter.items() if v > 1]

plt.bar(x, y)
plt.xlabel('Sponsors')
plt.ylabel('Recuento')
plt.title('Recuento de elementos repetidos')
plt.show()

nube_palabras = WordCloud(background_color='white').generate_from_frequencies(counter)
plt.imshow(nube_palabras, interpolation='bilinear')
plt.axis("off")
plt.show()
