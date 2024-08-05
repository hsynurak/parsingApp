# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_yedek_denem.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1752, 829)
        self.main_page = QtWidgets.QStackedWidget(Widget)
        self.main_page.setGeometry(QtCore.QRect(0, 20, 1501, 741))
        self.main_page.setObjectName("main_page")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.tableWidget = QtWidgets.QTableWidget(self.page_3)
        self.tableWidget.setGeometry(QtCore.QRect(30, 80, 1391, 631))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.filter_combo_box = QtWidgets.QComboBox(self.page_3)
        self.filter_combo_box.setGeometry(QtCore.QRect(30, 10, 201, 32))
        self.filter_combo_box.setObjectName("filter_combo_box")
        self.search_combo_box = QtWidgets.QComboBox(self.page_3)
        self.search_combo_box.setGeometry(QtCore.QRect(250, 10, 201, 32))
        self.search_combo_box.setObjectName("search_combo_box")
        self.download_btn = QtWidgets.QPushButton(self.page_3)
        self.download_btn.setGeometry(QtCore.QRect(1010, 40, 151, 32))
        self.download_btn.setObjectName("download_btn")
        self.back_to_main_page_btn = QtWidgets.QPushButton(self.page_3)
        self.back_to_main_page_btn.setGeometry(QtCore.QRect(1010, 10, 151, 32))
        self.back_to_main_page_btn.setObjectName("back_to_main_page_btn")
        self.show_display_table_btn = QtWidgets.QPushButton(self.page_3)
        self.show_display_table_btn.setGeometry(QtCore.QRect(80, 50, 91, 32))
        self.show_display_table_btn.setObjectName("show_display_table_btn")
        self.delete_btn = QtWidgets.QPushButton(self.page_3)
        self.delete_btn.setGeometry(QtCore.QRect(670, 40, 91, 32))
        self.delete_btn.setObjectName("delete_btn")
        self.searching_value_input = QtWidgets.QLineEdit(self.page_3)
        self.searching_value_input.setGeometry(QtCore.QRect(460, 10, 181, 21))
        self.searching_value_input.setText("")
        self.searching_value_input.setObjectName("searching_value_input")
        self.search_btn = QtWidgets.QPushButton(self.page_3)
        self.search_btn.setGeometry(QtCore.QRect(510, 40, 91, 32))
        self.search_btn.setObjectName("search_btn")
        self.updating_value_input = QtWidgets.QLineEdit(self.page_3)
        self.updating_value_input.setGeometry(QtCore.QRect(810, 10, 161, 21))
        self.updating_value_input.setText("")
        self.updating_value_input.setObjectName("updating_value_input")
        self.update_btn = QtWidgets.QPushButton(self.page_3)
        self.update_btn.setGeometry(QtCore.QRect(840, 40, 91, 32))
        self.update_btn.setObjectName("update_btn")
        self.get_info_btn = QtWidgets.QPushButton(self.page_3)
        self.get_info_btn.setGeometry(QtCore.QRect(1200, 10, 111, 32))
        self.get_info_btn.setObjectName("get_info_btn")
        self.main_page.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.details = QtWidgets.QPushButton(self.page_4)
        self.details.setGeometry(QtCore.QRect(600, 530, 100, 32))
        self.details.setObjectName("details")
        self.label = QtWidgets.QLabel(self.page_4)
        self.label.setGeometry(QtCore.QRect(570, 220, 201, 21))
        self.label.setObjectName("label")
        self.browse_model_btn = QtWidgets.QPushButton(self.page_4)
        self.browse_model_btn.setGeometry(QtCore.QRect(560, 190, 181, 31))
        self.browse_model_btn.setObjectName("browse_model_btn")
        self.upload_model_path = QtWidgets.QLineEdit(self.page_4)
        self.upload_model_path.setGeometry(QtCore.QRect(380, 270, 541, 21))
        self.upload_model_path.setObjectName("upload_model_path")
        self.upload_data_path = QtWidgets.QLineEdit(self.page_4)
        self.upload_data_path.setGeometry(QtCore.QRect(380, 380, 541, 21))
        self.upload_data_path.setObjectName("upload_data_path")
        self.parse_btn = QtWidgets.QPushButton(self.page_4)
        self.parse_btn.setGeometry(QtCore.QRect(560, 440, 181, 31))
        self.parse_btn.setObjectName("parse_btn")
        self.browse_data_btn = QtWidgets.QPushButton(self.page_4)
        self.browse_data_btn.setGeometry(QtCore.QRect(560, 320, 181, 31))
        self.browse_data_btn.setObjectName("browse_data_btn")
        self.parse_success = QtWidgets.QLabel(self.page_4)
        self.parse_success.setGeometry(QtCore.QRect(560, 500, 191, 16))
        self.parse_success.setText("")
        self.parse_success.setObjectName("parse_success")
        self.label_2 = QtWidgets.QLabel(self.page_4)
        self.label_2.setGeometry(QtCore.QRect(560, 350, 201, 21))
        self.label_2.setObjectName("label_2")
        self.main_page.addWidget(self.page_4)

        self.retranslateUi(Widget)
        self.main_page.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.download_btn.setText(_translate("Widget", "Download"))
        self.back_to_main_page_btn.setText(_translate("Widget", "Back"))
        self.show_display_table_btn.setText(_translate("Widget", "Show"))
        self.delete_btn.setText(_translate("Widget", "Delete"))
        self.search_btn.setText(_translate("Widget", "Search"))
        self.update_btn.setText(_translate("Widget", "Update"))
        self.get_info_btn.setText(_translate("Widget", "Info"))
        self.details.setText(_translate("Widget", "Details"))
        self.label.setText(_translate("Widget", "Choose data file(.xls, .xlsx)"))
        self.browse_model_btn.setText(_translate("Widget", "Browse Model File"))
        self.parse_btn.setText(_translate("Widget", "Start Parsing or Create DB"))
        self.browse_data_btn.setText(_translate("Widget", "Browse Data File"))
        self.label_2.setText(_translate("Widget", "Choose data file(.xls, .xlsx)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
