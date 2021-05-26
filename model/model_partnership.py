# -*- coding: utf-8 -*-

# Realizamos la importación de las librerías necesarias
import numpy as np
import pandas as pd
import matplotlib as mpl
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import cut_tree

import warnings; warnings.filterwarnings(action='once')

#!pip install yellowbrick --upgrade
from yellowbrick.cluster import KElbowVisualizer    
from yellowbrick.cluster import SilhouetteVisualizer



"""Llamamos el dataset desde su link correspondiente para importar el excel. Dado que los datos estan separados a la mitad en dos hojas distintas, asignamos cada hoja a un data frame."""

# importamos los datos
dts1 = pd.read_excel('https://archive.ics.uci.edu/ml/machine-learning-databases/00502/online_retail_II.xlsx' ,sheet_name='Year 2009-2010')
dts2 = pd.read_excel('https://archive.ics.uci.edu/ml/machine-learning-databases/00502/online_retail_II.xlsx' ,sheet_name='Year 2010-2011')

"""Conectamos ambos dataframe en uno mismo para tener toda la información alli."""

# Unimos los datos obtenidos de las dos hojas de excel
data = pd.concat([dts1,dts2])

"""Dado que el dataframe se obtuvo de dos hojas de cálculo, debemos restablecer sus índices y borrar los índices anteriores."""

# Reseteamos los índices
data = data.reset_index(drop=True)

"""# Exploración de datos y pre-procesamiento

En esta sección realizamos la exploración rápida de los datos.
"""

## Número de filas y columnas
data.shape

# Observamos los primeros cinco registros del dataframe
data.head()

"""# Limpieza

En esta sección nos enfocamos en la limpieza y la correción de posibles problemas en los datos

*Formato de las 
Variables no 
Coincide con el 
Tipo de Variable*
"""

# Observamos infomación general en el dataframe
data.info

# Observamos los tipos de las variables 
data.dtypes

# Observamos el número de cada tipo de variable
data.dtypes.value_counts()

# Observamos una descripción estadística rápida de los datos.
data.describe()

# Convertimos las variables a su formato correcto

data.Invoice = data.Invoice.astype("category")
data.StockCode = data.StockCode.astype("category")
data.Description = data.Description.astype("category")
data.Country = data.Country.astype("category")

data.dtypes

"""*Observaciones Duplicadas*"""

# Revisamos si hay registros duplicados
data.duplicated()

# revisamos si hay registros duplicados
data.duplicated().value_counts()

#Eliminamos los valores duplicados
indx = data[data.duplicated(keep='first')].index
data.drop(index = indx, inplace= True)

data.duplicated().value_counts()

"""Transacciones sin CustomerID (sin el identificador del cliente)"""

#Eliminamos las transacciones que no contengan CustomerID
data.dropna(axis=0, subset=['Customer ID'], inplace= True)

"""Transacciones canceladas"""

#Algunas de las transacciones contienen la letra C al comienzo de sus atributos Invoice, esto significa que fueron 
#canceladas. Por lo tanto y, dado que para nuestra propuesta de solución no las necesitamos, las eliminaremos.

indx = data.Invoice[data.Invoice.str.contains('C') == True].index
data.drop(index= indx, inplace= True)

"""Transacciones con precios menores o iguales a cero"""

#Eliminamos las transacciones que contengan en su atributo price, una cantidad igual o menor a cero.
indx = data.loc[data.Price <= 0].index
data.drop(index= indx, inplace= True)

"""* **texto en negrita**Valores Nulos (null)*

"""

# Revisamos si hay datos nulos
data.isnull()

data.isnull()

data.isnull().sum()

# Revisamos los datos que no son nulos
data.notnull()

# Eliminamos los registros con datos null
data.dropna()

"""*Errores de Digitación*"""

# Renombramos el nombre de la variable "Customer ID" por "CustomerID"
data = data.rename({'Customer ID':'CustomerID'}, axis="columns")

"""# Transformación de los datos"""

# Agregamos la variable de venta total, a través del producto de precio*cantidad de productos
data['TotalSales'] = data['Quantity'] * data['Price']

data.head()

#Agregamos una nueva columna en donde nos indiqe solamente el año y mes de la compra
data['InvoiceYearMonth']=pd.to_datetime(data['InvoiceDate']).map(lambda date: str((date.year))+'-'+dt.datetime(2000,date.month,29).strftime('%m'))
data.head()

data.shape

df_MonthlyNewCustomer = data.groupby('InvoiceYearMonth')['CustomerID'].nunique().reset_index()
df_MonthlyNewCustomer.set_axis(['InvoiceYearMonth','Number of New Customers'],inplace=True,axis=1)
df_MonthlyNewCustomer.head()

x = data.Country.apply(lambda x: x if x == 'United Kingdom' else 'Not UK').value_counts().rename('#Customers')
y = (x/data.shape[0]).rename('%Customers')
pd.concat([x, y], axis= 1)

"""# Visualización

Realizamos la visualización de los datos
"""

#Porcentage de Clientes que residen dentro de UK y fuera de UK
labels = 'UK', 'Not UK'
sizes = [y[0], y[1]]
explode = (0, 0.1)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')

plt.show()

# Plot
plt.figure(figsize=(12,10), dpi= 80)
sns.heatmap(data.corr(), xticklabels=data.corr().columns, yticklabels=data.corr().columns, cmap='RdYlGn', center=0, annot=True)

# Decorations
plt.title('Correlogram', fontsize=22)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

#Número de nuevos clientes por mes

fig = plt.figure()
axes = fig.add_axes([0, 0, 3, 1])
axes.bar(df_MonthlyNewCustomer['InvoiceYearMonth'],height=df_MonthlyNewCustomer['Number of New Customers'],color="Green")
axes.set_xlabel('Date',size=20)
axes.set_ylabel('Number',size=20)
axes.set_title('Monthly New Customer',size=24);
plt.show()

"""# **Asociación**

Preguntas

*   ¿Qué productos tienden a comprarse juntos en las transancciones?
"""

#Importamos las librerias necesarias para el desarrollo del modelo
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

#Creamos un nuevo dataset para este modelo
df_apriori = data.copy()

df_apriori.info()

#El modelo que se tiene planeado hacer, servirá para cualquier país. Pero para desarrollarlo, se usará Germany.
df_apriori.Country.value_counts()

#Aquí cambiamos los tipos de variables de las Columnas Description e Invoice. Además se eliminan valores Nan en Invoice.
df_apriori['Description'] = df_apriori['Description'].str.strip()
df_apriori.dropna(axis=0, subset=['Invoice'], inplace=True)
df_apriori['Invoice'] = df_apriori['Invoice'].astype('str')
df_apriori = df_apriori[~df_apriori['Invoice'].str.contains('C')]

#Acomodamos el dataset agrupandolo por la factura (Invoice) como fila y como columna las descripciones de los diferentes productos que
#vende la tienda. Esto, con el fin de visualizar de mejor manera qué productos y en qué cantidad se vendieron en las diferentes transacciones
df_basket = (df_apriori[df_apriori['Country'] =="Germany"]
          .groupby(['Invoice', 'Description'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('Invoice'))

#Observamos cómo quedaron los datos
df_basket

#Este método lo que hace es volver los valores de cada columna en binario (0 y 1) para el desarrollo del modelo.
def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

#Aplicamos dicha función al dataset con el que estamos desarrollando el modelo. Y nos da como resultado otro dataset.
df_basket_Sets = df_basket.applymap(encode_units)
df_basket_Sets.drop('POSTAGE', inplace=True, axis=1)

#Miramos cómo queda el nuevo dataset.
df_basket_Sets

#Aquí aplicamos el algoritmo apriori, el cual nos calcula los soportes dividiendo la frecuencia con la que aparecen los productos en las
#diferentes transacciones, por la cantidad total de transacciones que se hicieron.

#El soporte mínimo que se utiliza para clasificar a dicho producto como aceptable para tenerlo en cuenta en el desarrollo del modelo,
#depende mucho de la empresa. Como no se tienen más datos acerca de lo busca la empresa, se utilizará un soporte mínimo de 0.05.
frequent_itemsets = apriori(df_basket_Sets, min_support=0.05, use_colnames=True)

frequent_itemsets

"""Aquí se buscan las reglas de asociación de cada uno de los itemsets frecuentes que se encontraron anteriormente.
Para ello se tiene en cuenta un parametro llamado confianza, el cual se calcula como el soporte del itemset formado por todos los items 
que participan en la regla, dividido por el soporte del itemset formado por los items del antecedente. A continuación una imagen que ilustra mejor dicho escenario:

![image.png](data:image/png;base64,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)

Donde {A} (antecedente) => {B} (consecuente)

Además del soporte y la confianza, existe una tercera métrica cuantificar la calidad de las reglas y la probabilidad de que reflejen relaciones reales. Esta métrica es el estadístico lift, el cual compara la frecuencia observada de una regla con la frecuencia esperada simplemente por azar (si la regla no existe realmente).

Cuanto más se aleje el valor de lift de 1, más evidencias de que la regla no se debe a un artefacto aleatorio, es decir, mayor la evidencia de que la regla representa un patrón real.
"""

df_apriori_rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

df_apriori_rules.head()