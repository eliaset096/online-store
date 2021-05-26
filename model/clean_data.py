class CleanData(object):
    """
     Esta clase contiene funciones que se encargan de
    realizar la limpieza de los dostas del DataFrame con los datos
    """

    # -----------------Correciones de a los datos----------------------------------------------------

    def clean_data_manager(self, df_data):
        """
        Función principal donde se invocan las funciones
        auxilares.

        :param df_data: Es el DataFrame con los datos.

        :return: No hay retorno.

        """
        self.__rename_variables(df_data)
        self.__remove_duplicated(df_data)
        self.__remove_nan_customerID(df_data)
        self.__remove_cancelled_transations(df_data)
        self.__remove_negative_price(df_data)
        self.__rename_customerID_variable(df_data)

    def __rename_variables(self, df_data):
        """
        Función que corrije los nombres de las columnas del DataFrame.

        :param df_data: Es el DataFrame con los datos.

        :return: No hay retorno.

        """
        df_data.Invoice = df_data.Invoice.astype("category")
        df_data.Invoice = df_data.Invoice.astype("category")
        df_data.StockCode = df_data.StockCode.astype("category")
        df_data.Description = df_data.Description.astype("category")
        df_data.Country = df_data.Country.astype("category")

    def __remove_duplicated(self, df_data):
        """
        Función que elimina los registros duplicados del DataFrame.

        :param df_data: Es el DataFrame con los datos.

        :return: No hay retorno.

        """
        df_data.duplicated()
        df_data.duplicated().value_counts()
        ind = df_data[df_data.duplicated(keep='first')].index
        df_data.drop(index=ind, inplace=True)
        df_data.duplicated().value_counts()

    def __remove_nan_customerID(self, df_data):
        """
        Función que elimina los CustomerID nulos del DataFrame.

        :param df_data: Es el DataFrame con los datos.

        :return: No hay retorno.

        """
        df_data.dropna(axis=0, subset=['Customer ID'], inplace=True)

    def __remove_cancelled_transations(self, df_data):
        """
        Función que elimina las transacciones canceladas en el DataFrame.

        :param df_data: Es el DataFrame con los datos.

        :return: No hay retorno.

        """
        ind = df_data.Invoice[df_data.Invoice.str.contains('C') == True].index
        df_data.drop(index=ind, inplace=True)

    def __remove_negative_price(self, df_data):
        """
        Función que elimina los valores negativos en el Price.

        :param df_data: Es el DataFrame con los datos.

        :return: No hay retorno.

        """
        ind = df_data.loc[df_data.Price <= 0].index
        df_data.drop(index=ind, inplace=True)

    def __rename_customerID_variable(self, df_data):
        """
        Función que corrige el error de digitación en la columna CustomerID.

        :param df_data: Es el DataFrame con los datos.

        :return: No hay retorno.
        """
        df_data = df_data.rename({'Customer ID': 'CustomerID'}, axis="columns", inplace=True)
