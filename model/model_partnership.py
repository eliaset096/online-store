import warnings

from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

warnings.filterwarnings(action='once')


class ModelAssociation(object):

    def __init__(self, data):
        """
        Inicializa la clase y sus atributos.
        """

        self._df_data = data
        self._df_apriori_rules = None


    def get_df_apriori_rules(self):
        return self._df_apriori_rules

    def prepare_data(self):
        """
        Funcion que se encarga de preparar el DataFrame para aplicar el algoritmo Apriori removiendo de la
        columna 'Description' los espacios vacios; eliminando cualquier dato Nan de la columna 'Invoice', asi
        como cambiando su tipo de dato a 'str'.
        :return: No hay retorno.
        """

        self._df_data['Description'] = self._df_data['Description'].str.strip()
        self._df_data.dropna(axis=0, subset=['Invoice'], inplace=True)
        self._df_data['Invoice'] = self._df_data['Invoice'].astype('str')
        self._df_data[~self._df_data['Invoice'].str.contains('C')]



    def change_format_dataFrame(self, country):
        """
        Función que se encarga de agrupar el dataset por la transacciónes de un pais determinado como fila y
        las descripciones de los diferentes productos que vende la tienda como columnas.
        :param country: Pais al cual se le quiere aplicar el agrupar sus transacciones.
        :return: El nuevo dataFrame con las transacciones agrupadas
        """

        df_basket = (self._df_data[self._df_data['Country'] == country]
                     .groupby(['Invoice', 'Description'])['Quantity']
                     .sum().unstack().reset_index().fillna(0)
                     .set_index('Invoice'))

        return df_basket



    def binary_values(self, df_basket):
        """
        Funcion que se encarga de iniciar el proceso de volver en binario los valores del dataFrame ingresado
        por parametro. Elimina la columna 'Postage' ya que más adelante dara errores.
        :param df_basket: El dataFrame al cual se le quieren cambiar sus valores por binario.
        :return: El nuevo dataFrame con los valores en binarios.
        """

        df_basket_Sets = df_basket.applymap(self._encode_units)
        df_basket_Sets.drop('POSTAGE', inplace=True, axis=1)

        return df_basket_Sets



    def _encode_units(self, x):
        """
        Funcion que se encarga de volver los valores del dataFrame
        :param x: Valor el cual se quiere cambiar ya sea por un cero o un uno.
        :return: Cero si el valor X es cero o menor. Uno si el valor X es uno o mayor.
        """

        if x <= 0:
            return 0
        if x >= 1:
            return 1



    def create_itemset(self, df_basket_Sets):
        """
        Funcion que se encarga de crear los itemsets y de calcular su correspondiente metrica support.
        :param df_basket_Sets: DataFrame con los diferentes items de cada transaccion.
        :return: El nuevo dataFrame con los itemsets creados y su correspondiente metrica support calculada.
        """

        frequent_itemsets = apriori(df_basket_Sets, min_support=0.07, use_colnames=True)

        return frequent_itemsets



    def create_association_rules(self, frequent_itemsets):
        """
        Funcion que se encarga de calcular las reglas de asociacion, con sus correspondientes metricas support,
        confidence y lift
        :param frequent_itemsets: DataFrame del cual se va a calcular las reglas de asociacion.
        :return: No hay retorno.
        """

        df_apriori_rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)