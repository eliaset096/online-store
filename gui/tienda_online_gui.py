# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tienda_online_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from model.clean_data import CleanData
from model.model_clustering import ModelClustering


class Ui_Tienda_Online(object):
    def setupUi(self, Tienda_Online):
        Tienda_Online.setObjectName("Tienda_Online")
        Tienda_Online.resize(1264, 842)
        Tienda_Online.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(Tienda_Online)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(680, 10, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(690, 59, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(910, 10, 321, 101))
        self.graphicsView.setObjectName("graphicsView")
        self.tb_main = QtWidgets.QTabWidget(self.centralwidget)
        self.tb_main.setGeometry(QtCore.QRect(10, 100, 1251, 651))
        self.tb_main.setObjectName("tb_main")
        self.tb_data = QtWidgets.QWidget()
        self.tb_data.setObjectName("tb_data")
        self.label_3 = QtWidgets.QLabel(self.tb_data)
        self.label_3.setGeometry(QtCore.QRect(560, 10, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tw_data = QtWidgets.QTableWidget(self.tb_data)
        self.tw_data.setGeometry(QtCore.QRect(30, 40, 1201, 571))
        self.tw_data.setObjectName("tw_data")
        self.tw_data.setColumnCount(10)
        self.tw_data.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw_data.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_data.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_data.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_data.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_data.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_data.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_data.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_data.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_data.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_data.setHorizontalHeaderItem(9, item)
        self.tb_main.addTab(self.tb_data, "")
        self.tb_report = QtWidgets.QWidget()
        self.tb_report.setObjectName("tb_report")
        self.layoutWidget = QtWidgets.QWidget(self.tb_report)
        self.layoutWidget.setGeometry(QtCore.QRect(690, 0, 551, 631))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gv_graphic_report = QtWidgets.QGraphicsView(self.layoutWidget)
        self.gv_graphic_report.setObjectName("gv_graphic_report")
        self.verticalLayout.addWidget(self.gv_graphic_report)
        self.tbrow_recomendations = QtWidgets.QTextBrowser(self.layoutWidget)
        self.tbrow_recomendations.setObjectName("tbrow_recomendations")
        self.verticalLayout.addWidget(self.tbrow_recomendations)
        self.layoutWidget1 = QtWidgets.QWidget(self.tb_report)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 681, 631))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cb_customer_id = QtWidgets.QComboBox(self.layoutWidget1)
        self.cb_customer_id.setObjectName("cb_customer_id")
        self.cb_customer_id.addItem("")
        self.verticalLayout_2.addWidget(self.cb_customer_id)
        self.gv_graphic_main = QtWidgets.QGraphicsView(self.layoutWidget1)
        self.gv_graphic_main.setObjectName("gv_graphic_main")
        self.verticalLayout_2.addWidget(self.gv_graphic_main)
        self.tb_main.addTab(self.tb_report, "")
        self.bt_money_spent_customer = QtWidgets.QPushButton(self.centralwidget)
        self.bt_money_spent_customer.setGeometry(QtCore.QRect(12, 760, 191, 28))
        self.bt_money_spent_customer.setObjectName("bt_money_spent_customer")
        self.tb_new_customers_next = QtWidgets.QPushButton(self.centralwidget)
        self.tb_new_customers_next.setGeometry(QtCore.QRect(220, 760, 181, 28))
        self.tb_new_customers_next.setObjectName("tb_new_customers_next")
        self.tb_customers_for_exit = QtWidgets.QPushButton(self.centralwidget)
        self.tb_customers_for_exit.setGeometry(QtCore.QRect(420, 760, 101, 28))
        self.tb_customers_for_exit.setObjectName("tb_customers_for_exit")
        self.bt_appropriate_items_customer = QtWidgets.QPushButton(self.centralwidget)
        self.bt_appropriate_items_customer.setGeometry(QtCore.QRect(540, 760, 171, 28))
        self.bt_appropriate_items_customer.setObjectName("bt_appropriate_items_customer")
        self.bt_customer_purshas_history = QtWidgets.QPushButton(self.centralwidget)
        self.bt_customer_purshas_history.setGeometry(QtCore.QRect(730, 760, 201, 28))
        self.bt_customer_purshas_history.setObjectName("bt_customer_purshas_history")
        self.bt_return_back = QtWidgets.QPushButton(self.centralwidget)
        self.bt_return_back.setGeometry(QtCore.QRect(1070, 760, 93, 28))
        self.bt_return_back.setObjectName("bt_return_back")
        Tienda_Online.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Tienda_Online)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1264, 26))
        self.menubar.setObjectName("menubar")
        Tienda_Online.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Tienda_Online)
        self.statusbar.setObjectName("statusbar")
        Tienda_Online.setStatusBar(self.statusbar)

        self.retranslateUi(Tienda_Online)
        self.tb_main.setCurrentIndex(0)

        # ------------------------------------
        self.tw_data.setColumnWidth(0, 100)
        self.tw_data.setColumnWidth(1, 160)
        self.tw_data.setColumnWidth(2, 270)
        self.tw_data.setColumnWidth(3, 160)
        self.tw_data.setColumnWidth(4, 160)
        self.tw_data.setColumnWidth(5, 160)
        self.tw_data.setColumnWidth(6, 160)
        self.tw_data.setColumnWidth(7, 160)
        self.tw_data.setColumnWidth(8, 160)
        self.tw_data.setColumnWidth(9, 160)

        # ------------------------------------
        clustering = ModelClustering()
        clean_data = CleanData()

        clustering.load_discover_data()
        data = clustering.df_data
        clean_data.clean_data_manager(data)
        clustering.transform_data()

        clustering.show_percentage_of_customers_by_region()
        clustering.show_number_of_new_clients_per_month()

        clustering.crate_deploy_kmeans_model()

        clustering.show_table_rfm()
        clustering.show_data_in_rfm()
        clustering.show_data_rfm_scaled()
        clustering.show_define_kmeans_model()
        clustering.show_silhouette_analysis()

        clustering.training_kmeans_model()
        clustering.show_centroides_model()
        clustering.show_training_kmeans_model_result()
        clustering.testing_kmeans_model()

        self.show_data_in_tablewidget(data)

        #self.gv_graphic_main.setBackgroundBrush(QImage(clustering.show_percentage_of_customers_by_region()))
        #self.gv_graphic_main.setCacheMode(QtWidgets.QGraphicsView.CacheBackground)
        #self.gv_graphic_main.setFrameShape(QFrame(QImage(clustering.show_percentage_of_customers_by_region())))
        # self.gv_graphic_main.setScene(clustering.show_percentage_of_customers_by_region())
        # self.gv_graphic_main.  (clustering.show_percentage_of_customers_by_region())


        # -----------------------------------

        # self.gv_graphic_report.

        # ------------------------------------------

        QtCore.QMetaObject.connectSlotsByName(Tienda_Online)

    def retranslateUi(self, Tienda_Online):
        _translate = QtCore.QCoreApplication.translate
        Tienda_Online.setWindowTitle(_translate("Tienda_Online", "Tienda Online - Portafolio de Analítica"))
        self.label.setText(_translate("Tienda_Online", "Tienda Online "))
        self.label_2.setText(_translate("Tienda_Online", "Portafolio de Analítica"))
        self.label_3.setText(_translate("Tienda_Online", "Conjunto de Datos"))
        item = self.tw_data.horizontalHeaderItem(0)
        item.setText(_translate("Tienda_Online", "Invoice"))
        item = self.tw_data.horizontalHeaderItem(1)
        item.setText(_translate("Tienda_Online", "StockCode"))
        item = self.tw_data.horizontalHeaderItem(2)
        item.setText(_translate("Tienda_Online", "Description"))
        item = self.tw_data.horizontalHeaderItem(3)
        item.setText(_translate("Tienda_Online", "Quantity"))
        item = self.tw_data.horizontalHeaderItem(4)
        item.setText(_translate("Tienda_Online", "InvoiceDate"))
        item = self.tw_data.horizontalHeaderItem(5)
        item.setText(_translate("Tienda_Online", "Price"))
        item = self.tw_data.horizontalHeaderItem(6)
        item.setText(_translate("Tienda_Online", "CustomerID"))
        item = self.tw_data.horizontalHeaderItem(7)
        item.setText(_translate("Tienda_Online", "Country"))
        item = self.tw_data.horizontalHeaderItem(8)
        item.setText(_translate("Tienda_Online", "TotalSales"))
        item = self.tw_data.horizontalHeaderItem(9)
        item.setText(_translate("Tienda_Online", "InvoiceYearMonth"))
        self.tb_main.setTabText(self.tb_main.indexOf(self.tb_data),
                                _translate("Tienda_Online", "            Datos            "))
        self.cb_customer_id.setCurrentText(_translate("Tienda_Online", "Seleccione un CustomerID"))
        self.cb_customer_id.setItemText(0, _translate("Tienda_Online", "Seleccione un CustomerID"))
        self.tb_main.setTabText(self.tb_main.indexOf(self.tb_report),
                                _translate("Tienda_Online", "            Informe             "))
        self.bt_money_spent_customer.setText(_translate("Tienda_Online", "Ver Dinero Gastado Cliente Mes"))
        self.tb_new_customers_next.setText(_translate("Tienda_Online", "Clientes Nuevos Próximo Mes"))
        self.tb_customers_for_exit.setText(_translate("Tienda_Online", "Clientes por Irse"))
        self.bt_appropriate_items_customer.setText(_translate("Tienda_Online", "Artículos Apropiados Cliente"))
        self.bt_customer_purshas_history.setText(_translate("Tienda_Online", "Clientes Según Historial Compras"))
        self.bt_return_back.setText(_translate("Tienda_Online", "Regresar"))

    def show_data_in_tablewidget(self, data):
        # data = clustering.load_data_from_dataset(self)
        row = 0
        self.tw_data.setRowCount(len(data))
        for i in data.index:
            self.tw_data.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data["Invoice"][i])))
            self.tw_data.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data["StockCode"][i])))
            self.tw_data.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data["Description"][i])))
            self.tw_data.setItem(row, 3, QtWidgets.QTableWidgetItem(str(data["Quantity"][i])))
            self.tw_data.setItem(row, 4, QtWidgets.QTableWidgetItem(str(data["InvoiceDate"][i])))
            self.tw_data.setItem(row, 5, QtWidgets.QTableWidgetItem(str((data["Price"][i]))))
            self.tw_data.setItem(row, 6, QtWidgets.QTableWidgetItem(str(data["CustomerID"][i])))
            self.tw_data.setItem(row, 7, QtWidgets.QTableWidgetItem(str(data["Country"][i])))

            self.tw_data.setItem(row, 8, QtWidgets.QTableWidgetItem(str(data["TotalSales"][i])))
            self.tw_data.setItem(row, 9, QtWidgets.QTableWidgetItem(str(data["InvoiceYearMonth"][i])))

            row += 1


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Tienda_Online = QtWidgets.QMainWindow()
    ui = Ui_Tienda_Online()
    ui.setupUi(Tienda_Online)
    Tienda_Online.show()
    sys.exit(app.exec_())
