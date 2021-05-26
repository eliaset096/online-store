# -*- coding: utf-8 -*-

# Realizamos la importación de las librerías necesarias
import datetime as dt
import warnings;
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from yellowbrick.cluster import KElbowVisualizer
from yellowbrick.cluster import SilhouetteVisualizer
warnings.filterwarnings(action='once')


class ModelClustering(object):
    """
    En esta clase se hace la implentación algunos métodós de aprendizaje
    no supervizado, como RFM, Clustering.
    """

    def __init__(self):
        """
        Inicializa la clase y sus atributos.
        """
        self.df_data = pd.DataFrame()
        self.df_rfm = pd.DataFrame()
        self.df_monthly_new_customer = pd.DataFrame()
        self.df_data_model = pd.DataFrame()
        self.data_transformed_scaled = pd.DataFrame()
        self.kmeans = str("fg")
        self.centroides = str("fg")

    # ------------------Cargue  y descubrimientos de los datos-----------------------------------------------

    def load_discover_data(self):
        """
        Función que realiza el cargue de los datos a un DataFrame.
        :return: No hay retorno.
        """
        dts1 = pd.read_excel('online_retail_II.xlsx', sheet_name='Year 2009-2010')
        dts2 = pd.read_excel('online_retail_II.xlsx', sheet_name='Year 2010-2011')
        data = pd.concat([dts1, dts2])
        data = data.reset_index(drop=True)
        self.df_data = pd.DataFrame(data)

    # --------------Transformación de los datos ---------------------------------------------------

    def transform_data(self):
        """
        Función que realiza la transformación de los datos.
        Se crean las variables TotalSales e InvoiceYearMonth.
        :return:  No hay retorno.
        """
        self.df_data['TotalSales'] = self.df_data['Quantity'] * self.df_data['Price']
        self.df_data.head()

        self.df_data['InvoiceYearMonth'] = pd.to_datetime(self.df_data['InvoiceDate']).map(
            lambda date: str((date.year)) + '-' + dt.datetime(2000, date.month, 29).strftime('%m'))

        self.df_monthly_new_customer = self.df_data.groupby('InvoiceYearMonth')['CustomerID'].nunique().reset_index()
        self.df_monthly_new_customer.set_axis(['InvoiceYearMonth', 'Number of New Customers'], inplace=True, axis=1)
        self.df_monthly_new_customer.head()

    # ------------------Visualización de los datos --------------------------------------

    def show_percentage_of_customers_by_region(self):
        """
        Función que dibuja una gráfico circular para mostrar
        el porcentaje de los clientes de Reino Unido y los que no.
        :return: } No hay retorno.
        """
        x = self.df_data.Country.apply(lambda x: x if x == 'United Kingdom' else 'Not UK').value_counts().rename(
            '#Customers')
        y = (x / self.df_data.shape[0]).rename('%Customers')
        pd.concat([x, y], axis=1)
        labels = 'UK', 'Not UK'
        sizes = [y[0], y[1]]
        explode = (0, 0.1)
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')
        plt.show()

        # Plot
        plt.figure(figsize=(12, 10), dpi=80)
        sns.heatmap(self.df_data.corr(), xticklabels=self.df_data.corr().columns,
                    yticklabels=self.df_data.corr().columns, cmap='RdYlGn',
                    center=0,
                    annot=True)
        # Decorations
        plt.title('Correlogram', fontsize=22)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.show()

    def show_number_of_new_clients_per_month(self):
        """
        Función para mostrar el número de clientes que
        se adicionan a la compañia cada mes.
        :return:  No hay retorno.
        """
        fig = plt.figure()
        axes = fig.add_axes([0, 0, 3, 1])
        axes.bar(self.df_monthly_new_customer['InvoiceYearMonth'],
                 height=self.df_monthly_new_customer['Number of New Customers'],
                 color="Green")
        axes.set_xlabel('Date', size=20)
        axes.set_ylabel('Number', size=20)
        axes.set_title('Monthly New Customer', size=24);
        plt.show()

    # --------------------- Modelado -----------------------------------------------------------

    def crate_deploy_kmeans_model(self):
        """
        Función que prepara los datos poara aplicar el modelo
        KMeans.
        :return: No hay retorno.
        """
        self.df_data_model = self.df_data.copy()
        self.df_rfm = pd.DataFrame()

        today_date = self.df_data_model['InvoiceDate'].max()

        self.df_rfm = self.df_data_model.groupby('CustomerID').agg({
            'InvoiceDate': lambda date: (today_date - date.max()).days,
            # Calculamos el número de días que han pasado desde que se hizo la última compra del cliente
            'Invoice': lambda inv: inv.nunique(),  # Número de compras realizadas por el cliente
            'TotalSales': lambda price: price.sum()})  # Cantidad total de las compras de cada cliente

        self.df_rfm = self.df_rfm.rename(
            columns={'InvoiceDate': 'Recency', 'Invoice': 'Frequency', 'TotalSales': 'Monetary'})

        freq_stats = self.df_rfm['Frequency'].describe()
        freq_threshold_1 = ((freq_stats['75%'] - freq_stats['25%']) * 3)
        limit_q3 = freq_stats['75%'] + freq_threshold_1
        ind = self.df_rfm.loc[self.df_rfm.Frequency > limit_q3].index
        self.df_rfm.drop(index=ind, inplace=True)

        freq_stats = self.df_rfm['Monetary'].describe()
        freq_threshold_2 = ((freq_stats['75%'] - freq_stats['25%']) * 3)
        limit_q3 = freq_stats['75%'] + freq_threshold_2
        ind = self.df_rfm.loc[self.df_rfm.Monetary > limit_q3].index
        self.df_rfm.drop(index=ind, inplace=True)

        scaler = MinMaxScaler(feature_range=(0, 1))
        self.data_transformed_scaled = pd.DataFrame(scaler.fit_transform(self.df_rfm), columns=self.df_rfm.columns)

    def show_table_rfm(self):
        """
        Función muestra la tabla del modelo RFM.
        :return: No hay retorno.
        """
        # Pintamos para ver como se comportan los datos calculados anteriormente
        fig, ax = plt.subplots(ncols=2, nrows=3, figsize=(11, 11))
        sns.distplot(self.df_rfm.Recency, ax=ax[0][0], kde=False)
        sns.distplot(self.df_rfm.Frequency, ax=ax[1][0], kde=False)
        sns.distplot(self.df_rfm.Monetary, ax=ax[2][0], kde=False)

    def show_data_in_rfm(self):
        """
        Función que muestra los datos obtenidos del modelo EFM.
        :return: No hay retorno.
        """
        # Pintamos para ver como se comportan los datos
        fig, ax = plt.subplots(ncols=2, nrows=3, figsize=(11, 11))
        sns.distplot(self.df_rfm.Recency, ax=ax[0][0], kde=False)
        sns.distplot(self.df_rfm.Frequency, ax=ax[1][0], kde=False)
        sns.distplot(self.df_rfm.Monetary, ax=ax[2][0], kde=False)

    def show_data_rfm_scaled(self):
        """
        Función que muestra los datos normalizados en el modelo RFM.
        :return: No hay retorno.
        """
        # Pintamos para ver como se comportan los datos
        fig, ax = plt.subplots(ncols=2, nrows=3, figsize=(11, 11))
        sns.distplot(self.data_transformed_scaled.Recency, ax=ax[0][0], kde=False)
        sns.distplot(self.data_transformed_scaled.Frequency, ax=ax[1][0], kde=False)
        sns.distplot(self.data_transformed_scaled.Monetary, ax=ax[2][0], kde=False)

    def show_define_kmeans_model(self):
        """
        Función que muestra los gráficos de los métdos
        para hallar el k óptimo.
        :return: No hay retorno.
        """
        # Rango del número de clusters
        k_min = 1
        k_max = 10

        model1_clust = KMeans(init='k-means++', n_init=12, max_iter=200, random_state=50)

        for metric in ["distortion", "silhouette", "calinski_harabasz"]:
            if metric == "silhouette" or metric == "calinski_harabasz":
                k_min = max(2, k_min)
            else:
                k_min = k_min

            plt.figure(figsize=(10, 5))
            visualizer = KElbowVisualizer(estimator=model1_clust, k=(k_min, k_max + 1), metric=metric, timings=False,
                                          locate_elbow=False)
            visualizer.fit(self.data_transformed_scaled)
            visualizer.show()

    def show_silhouette_analysis(self):
        """
        Función que muestra los gráficos del método de
        silueta para confirmar el k óptimo.
        :return: No hay retorno.
        """
        for k in [2, 3, 4, 5, 6]:
            model2_clust = KMeans(n_clusters=k, init='k-means++', n_init=12, max_iter=300, random_state=50)

            plt.figure(figsize=(10, 3))
            visualizer = SilhouetteVisualizer(estimator=model2_clust, colors='yellowbrick')
            visualizer.fit(self.data_transformed_scaled)
            visualizer.show()

    def training_kmeans_model(self):
        """
        Función que entrena el modelo kmeans.
        :return: No hay retorno.
        """
        # Final model with k=3
        k = 3
        self.kmeans = KMeans(n_clusters=k, init='k-means++', n_init=12, max_iter=300, random_state=50)
        self.kmeans.fit(self.data_transformed_scaled)

    def show_centroides_model(self):
        """
        Función que muestra los centroides del modelo.
        :return: No hay retorno.
        """
        self.centroides = self.kmeans.cluster_centers_
        print("Centroides")
        print(self.centroides)

    def show_training_kmeans_model_result(self):
        """
        Función que muestra el resultado del modelo kmeans.
        :return: No hay retorno.
        """
        plt.figure(figsize=(5, 5))
        plt.scatter(self.data_transformed_scaled.iloc[:, 0], self.data_transformed_scaled.iloc[:, 1],
                    c=self.kmeans.labels_.reshape((-1, 1)),
                    s=50, cmap='viridis')
        plt.scatter(self.centroides[:, 0], self.centroides[:, 1], marker='o', color='white', edgecolor='k', s=300,
                    alpha=0.8)
        plt.xlabel(self.data_transformed_scaled.columns[0] + ' normalizado.')
        plt.ylabel(self.data_transformed_scaled.columns[1] + ' normalizado.')

        for i, c in enumerate(self.centroides):
            plt.scatter(c[0], c[1], marker='$%d$' % i, alpha=1, s=50, edgecolor='k')

        plt.title('Resultado del agrupamiento')
        plt.show()

    def testing_kmeans_model(self):
        """
        Función que hace la prueba del modelo
        :return: No hay retorno.
        """
        self.df_rfm['Cluster_Segment'] = self.kmeans.labels_
        self.df_rfm.head()
        self.df_rfm[["Cluster_Segment", "Recency", "Frequency", "Monetary"]].groupby("Cluster_Segment").agg(
            ["mean", "median", "count"])

