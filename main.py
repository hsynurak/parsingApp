import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sqlite3
import pandas as pd
from ui import Ui_Widget

class MainWindow(QWidget, Ui_Widget):
     def __init__(self):
          super(MainWindow, self).__init__()
          #loadUi('form_yedek_denem.ui', self)
          self.setupUi(self)
          self.file_path_model = ''
          self.file_path_data = ''
          self.table_names=[]
          self.back_to_main_page_btn.clicked.connect(self.show_main)
          self.details.clicked.connect(self.show_details)
          self.browse_model_btn.clicked.connect(self.browsefiles)
          self.browse_data_btn.clicked.connect(self.browsefiles_data)
          #self.define_btn.clicked.connect(self.define_model)
          self.parse_btn.clicked.connect(self.parsing)
          self.show_display_table_btn.clicked.connect(self.load_data)
          self.delete_btn.clicked.connect(self.delete_data)
          self.parse_success.setText('')
          self.download_btn.clicked.connect(self.download_data)
          self.search_btn.clicked.connect(self.search_data)
          self.update_btn.clicked.connect(self.update_data)
          self.get_info_btn.clicked.connect(self.get_info)
          #self.load_data()
            
     #opening details page        
     def show_details(self):
          self.main_page.setCurrentIndex(0)      

     #opening main page
     def show_main(self):
          self.main_page.setCurrentIndex(1)
     
     #main function for parsing
     def parsing(self):
          conn = sqlite3.connect('deneme.db')
          cursor = conn.cursor()
          #taking model and data file paths from user
          model_input = self.file_path_model
          data_input = self.file_path_data
          df_model = pd.read_excel(model_input)
          df_data = pd.read_excel(data_input)
          #to make groups and controlling group types, need to check first 4 columns
          columns_to_check = [0, 1, 2, 3]
          control_row = df_model.iloc[0]
          #a list for table column names from model file
          table_columns_name_list = []
          table_names = []
          #index infos for parsing raw data
          length_list_cs0000 = []
          length_list_cs0100 = []
          length_list_cs0200 = []
          length_list_cs0301 = []
          length_list_cs0400 = []
          length_list_memzuc = [] 
          
          #the function to fill filter_combo_box with table names from db, dinamically
          def fetch_data_from_db():
               cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
               data = cursor.fetchall()
               #conn.close()
               return [item[0] for item in data]
          
          #getting table names from and filling filter_combo_box
          data = fetch_data_from_db()
          self.filter_combo_box.addItems(data)
          
          conn = sqlite3.connect('deneme.db')
          cursor = conn.cursor()
          
          #the function to create db tables with table group name infos
          def create_table_if_not_exists():
               if table_columns_name_list:
                    #first create a table name with all grouo name infos, then create columns type and create table
                    formatted_table_name = f'"{report_parent_grup_name}_{report_grup_name}_{report_name}_{report_sub_name}"'
                    table_names.append(formatted_table_name)
                    formatted_columns_with_types = ', '.join(f'"{col}" TEXT' for col in table_columns_name_list)
                    cursor.execute(f'CREATE TABLE IF NOT EXISTS {formatted_table_name} ({formatted_columns_with_types})')

          for index, row in df_model.iterrows():
               if all(row.iloc[col] == control_row.iloc[col] for col in columns_to_check):
                    #while taking column names, we need to check special characters and turkish characters
                    column_name = row.iloc[4].replace('/', '_').replace(' ', '_').replace(':', '_').lower()
                    column_name = column_name.replace('ı', 'i').replace('ğ', 'g').replace('ü', 'u').replace('ş', 's').replace('ö', 'o').replace('ç', 'c').replace('İ','i').replace('Ğ','g').replace('Ü','u').replace('Ş','s').replace('Ö','o').replace('Ç','c')
                    #if column name is already in the list, show a warning message
                    if column_name in table_columns_name_list:
                         msg = QMessageBox()
                         msg.setIcon(QMessageBox.Information)
                         msg.setWindowTitle("WARNING!")
                         msg.setText("There is repeating column names")
                         msg.setInformativeText("Please check your model file and column names")                         
                         
                    #if column name is not in the list, add it to the table_columns_name_list
                    table_columns_name_list.append(column_name)
                    start_index = int(row.iloc[5] - 1)
                    end_index = int(start_index + row.iloc[6])
                    report_parent_grup_name = row[0]
                    report_grup_name = row[1]
                    report_name = row[2]
                    report_sub_name = row[3]
                    if report_sub_name == 'CS0000':
                         length_list_cs0000.append((start_index, end_index))
                    elif report_sub_name == 'CS0100':
                         length_list_cs0100.append((start_index, end_index))
                    elif report_sub_name == 'CS0200':
                         length_list_cs0200.append((start_index, end_index))
                    elif report_sub_name == 'CS0301':
                         length_list_cs0301.append((start_index, end_index))
                    elif report_sub_name == 'CS0400':
                         length_list_cs0400.append((start_index, end_index))
                    elif report_sub_name == 'MEMZUC':
                         length_list_memzuc.append((start_index, end_index))
                    else:
                         print('Invalid report name')
               else:
                    create_table_if_not_exists()

                    table_columns_name_list = []
                    report_parent_grup_name = row[0]
                    report_grup_name = row[1]
                    report_name = row[2]
                    report_sub_name = row[3]
                    control_row = row
                    
                    column_name = row.iloc[4].replace('/', '_').replace(' ', '_').replace(':', '_').lower()
                    column_name = column_name.replace('ı', 'i').replace('ğ', 'g').replace('ü', 'u').replace('ş', 's').replace('ö', 'o').replace('ç', 'c').replace('İ','i').replace('Ğ','g').replace('Ü','u').replace('Ş','s').replace('Ö','o').replace('Ç','c')
                    table_columns_name_list.append(column_name)
                    start_index = int(row.iloc[5] - 1)
                    end_index = int(start_index + row.iloc[6])
                    if report_sub_name == 'CS0000':
                         length_list_cs0000.append((start_index, end_index))
                    elif report_sub_name == 'CS0100':
                         length_list_cs0100.append((start_index, end_index))
                    elif report_sub_name == 'CS0200':
                         length_list_cs0200.append((start_index, end_index))
                    elif report_sub_name == 'CS0301':
                         length_list_cs0301.append((start_index, end_index))
                    elif report_sub_name == 'CS0400':
                         length_list_cs0400.append((start_index, end_index))
                    elif report_sub_name == 'MEMZUC':
                         length_list_memzuc.append((start_index, end_index))
                    else:
                         print('Invalid report name')

          create_table_if_not_exists()  # Son tabloyu oluşturmak için çağır
          
          for table in table_names:
               cursor.execute(f'DELETE FROM {table}')

          def parsing_raw_data(raw_value, length_list):
               parsed_data = [raw_value[start:end] for start, end in length_list]
               #print(parsed_data)
               return parsed_data

          for index, row in df_data.iterrows():
               str_x = str(row[0])
               if str_x.startswith('CS0000'):
                    parsed_data = parsing_raw_data(str_x, length_list_cs0000)
                    placeholders = ', '.join(['?'] * len(parsed_data))
                    sql_query = f'INSERT INTO RM_KRS_KONUT_CS0000 VALUES ({placeholders})'
                    try:
                         cursor.execute(sql_query, parsed_data)
                         print('Data inserted for CS0000')
                    except sqlite3.Error as e:
                         print(f"An error occurred: {e.args[0]}")
               elif str_x.startswith('CS0100'):
                    parsed_data = parsing_raw_data(str_x, length_list_cs0100)
                    placeholders = ', '.join(['?'] * len(parsed_data))
                    sql_query = f'INSERT INTO RM_KRS_KONUT_CS0100 VALUES ({placeholders})'
                    try:
                         cursor.execute(sql_query, parsed_data)
                         print('Data inserted for CS0100')
                    except sqlite3.Error as e:
                         print(f"An error occurred: {e.args[0]}")
               elif str_x.startswith('CS0200'):
                    parsed_data = parsing_raw_data(str_x, length_list_cs0200)
                    placeholders = ', '.join(['?'] * len(parsed_data))
                    sql_query = f'INSERT INTO RM_KRS_KONUT_CS0200 VALUES ({placeholders})'
                    try:
                         cursor.execute(sql_query, parsed_data)
                         print('Data inserted for CS0200')
                    except sqlite3.Error as e:
                         print(f"An error occurred: {e.args[0]}")
               elif str_x.startswith('CS0301'):
                    parsed_data = parsing_raw_data(str_x, length_list_cs0301)
                    placeholders = ', '.join(['?'] * len(parsed_data))
                    sql_query = f'INSERT INTO RM_KRS_KONUT_CS0301 VALUES ({placeholders})'
                    try:
                         cursor.execute(sql_query, parsed_data)
                         print('Data inserted for CS0301')
                    except sqlite3.Error as e:
                         print(f"An error occurred: {e.args[0]}")
               elif str_x.startswith('CS0400'):
                    parsed_data = parsing_raw_data(str_x, length_list_cs0400)
                    placeholders = ', '.join(['?'] * len(parsed_data))
                    sql_query = f'INSERT INTO RM_KRS_KONUT_CS0400 VALUES ({placeholders})'
                    try:
                         cursor.execute(sql_query, parsed_data)
                         print('Data inserted for CS0400')
                    except sqlite3.Error as e:
                         print(f"An error occurred: {e.args[0]}")
               elif len(str_x) == 176:
                    parsed_data = parsing_raw_data(str_x, length_list_memzuc)
                    placeholders = ', '.join(['?'] * len(parsed_data))
                    sql_query = f'INSERT INTO RM_MEMZUC_MEMZUC_MEMZUC VALUES ({placeholders})'
                    try:
                         cursor.execute(sql_query, parsed_data)
                         print('Data inserted for MEMZUC')
                    except sqlite3.Error as e:
                         print(f"An error occurred: {e.args[0]}")
                    
                    
               else:
                    print('Undefined data type')
                    
          self.parse_success.setText('Data parsing is successful')

          conn.commit()
          conn.close()

     def load_data(self):
          conn = sqlite3.connect('deneme.db')
          cursor = conn.cursor()
          
          self.search_combo_box.clear()
          self.tableWidget.clear()
          self.tableWidget.setRowCount(0)
          self.tableWidget.setColumnCount(0)
          filter_value = ''
          filter_value = self.filter_combo_box.currentText()
          
          if not filter_value or filter_value == '':
               msg = QMessageBox()
               msg.setIcon(QMessageBox.Information)     
               msg.setWindowTitle("UYARI")
               msg.setText("Lütfen bir tablo seç")
               #msg.setInformativeText("Yedek aldığınızdan emin olun")
               msg.setDetailedText("Tablo seçme kısmı boş ise, model ve data dosyalarınız kontrol ediniz. Parsing işleminin sağlıklı gerçekleştiğinden emin olun")
               msg.setStandardButtons(QMessageBox.Ok)
               msg.exec_()
               return
          

          if filter_value == "All":
               column_names = []
               all_datas = []
               for table in self.table_names:
                    cursor.execute(f'SELECT * FROM {table}')
                    rows = cursor.fetchall()
                    if rows:
                         table_columns = [description[0] for description in cursor.description]
                         if not column_names:
                              column_names = table_columns
                              self.tableWidget.setColumnCount(len(column_names))
                              self.tableWidget.setHorizontalHeaderLabels(column_names)
                         all_datas.extend(rows)
               for row_data in all_datas:
                    row = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row)
                    for column, data in enumerate(row_data):
                         self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))
          else:
               cursor.execute(f'SELECT * FROM {filter_value}')
               rows = cursor.fetchall()
               if rows:
                    column_names = [description[0] for description in cursor.description]
                    self.tableWidget.setColumnCount(len(column_names))
                    self.tableWidget.setHorizontalHeaderLabels(column_names)
                    for row_data in rows:
                         row = self.tableWidget.rowCount()
                         self.tableWidget.insertRow(row)
                         for column, data in enumerate(row_data):
                              self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))
                              
          def fetch_tables_from_db():
               conn = sqlite3.connect('deneme.db')
               cursor = conn.cursor()
               cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
               tables = cursor.fetchall()
               conn.close()
               return [item[0] for item in tables]
          
          def fetch_columns_from_db():
               conn = sqlite3.connect('deneme.db')
               cursor = conn.cursor()
               cursor.execute(f"PRAGMA table_info({filter_value})")
               columns_info = cursor.fetchall()
               conn.close()
               return [item[1] for item in columns_info]
          
          columns = fetch_columns_from_db()
          self.search_combo_box.addItems(columns)

     def browsefiles(self):
          file_filter = "Excel files (*.xls *.xlsx)"
          fname=QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', file_filter)
          if fname[0]:
               self.file_path_model = fname[0]
               self.upload_model_path.setText(self.file_path_model)
               print(f"Selected file: {self.file_path_model}")
      
     def browsefiles_data(self):
          file_filter = "Excel files (*.xls *.xlsx)"
          fname=QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', file_filter)
          if fname[0]:
               self.file_path_data = fname[0]
               self.upload_data_path.setText(self.file_path_data)
               print(f"Selected file: {self.file_path_data}")           
   
     def on_item_clicked(self, item):
          row = item.row()
          self.tableWidget.selectRow(row)
     
     def delete_data(self):
          row = self.tableWidget.currentRow()
          if row < 0:
               msg = QMessageBox()
               msg.setIcon(QMessageBox.Warning)
               msg.setWindowTitle("UYARI")
               msg.setText("Silme yapılamadı!!!")
               msg.setInformativeText("Lütfen silmek için tablo ve satır seçtiğinizden emin olun.")
               msg.setStandardButtons(QMessageBox.Ok)
               msg.setDefaultButton(QMessageBox.Ok)
               msg.exec_()
          else:
               msg = QMessageBox()
               msg.setIcon(QMessageBox.Information)
               msg.setWindowTitle("UYARI")
               msg.setText("Silmek üzeresin")
               msg.setInformativeText("Yedek aldığınızdan emin olun")
               msg.setDetailedText("Silinen dosyaların geri dönüşümü yoktur")
               msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
               msg.setDefaultButton(QMessageBox.Cancel)
               response = msg.exec_()
               if response == QMessageBox.Ok:
                    #filter_value = self.filter_combo_box.currentText()
                    if row >= 0:
                         item = self.tableWidget.item(row, 2)
                         if item:
                              uye_kodu = item.text()
                              conn = sqlite3.connect('deneme.db')
                              cursor = conn.cursor()
                              cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
                              tables = cursor.fetchall()
                              tables_names = [table[0] for table in tables]
                              for table in tables_names:
                                   cursor.execute(f"PRAGMA table_info({table})")
                                   columns = cursor.fetchall()
                                   column_names = [column[1] for column in columns]
                                   if 'uye_kodu' in column_names:
                                        cursor.execute(f"DELETE FROM {table} WHERE uye_kodu = ?", (uye_kodu, ))
                              conn.commit()
                              conn.close()
                              self.tableWidget.removeRow(row)
                    
                    print('Delete button clicked')               
               else:
                    print('Cancel clicked')

     def download_data(self):
          target_table_name = self.filter_combo_box.currentText()
          options = QFileDialog.Options()
          options |= QFileDialog.DontUseNativeDialog

          
          if not target_table_name:
               msg = QMessageBox()
               msg.setIcon(QMessageBox.Warning)
               msg.setWindowTitle("UYARI")
               msg.setText("İndirme yapılamadı!!!")
               msg.setInformativeText("Lütfen indirmek için tablo seçtiğinizden emin olun.")
               msg.setStandardButtons(QMessageBox.Ok)
               msg.setDefaultButton(QMessageBox.Ok)
               msg.exec_()
          else:
               file_path, _ = QFileDialog.getSaveFileName(self, "Excel Dosyasını Kaydet", "", "Excel Files (*.xlsx);;All Files (*)", options=options)
               if not file_path:
                    # Kullanıcı bir dosya seçmezse işlemi iptal et
                    QMessageBox.warning(self, "İptal", "Dosya kaydetme işlemi iptal edildi.")
                    return

               # Kullanıcı dosya uzantısı belirtmemişse '.xlsx' ekleyin
               if not file_path.endswith('.xlsx'):
                    file_path += '.xlsx'

               conn = sqlite3.connect('deneme.db')
               cursor = conn.cursor()
               try:
                    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
                    table_names = cursor.fetchall()

                    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
                         for table_name in table_names:
                              table_name = table_name[0]
                              query = f"SELECT * FROM {table_name}"
                              cursor.execute(query)
                              data = cursor.fetchall()
                              
                              if not data:
                                   print(f"No data found in table {table_name}")
                                   continue
                              df = pd.DataFrame(data)
                              column_names = [description[0] for description in cursor.description]

                              if df.empty:
                                   print(f"No data found in table {table_name}")
                                   continue
                              
                              df.columns = column_names
                              sheet_name = f"{table_name}"
                              df.to_excel(writer, sheet_name=sheet_name, index=False)
               finally:
                    conn.close()
              
     def search_data(self):
          conn = sqlite3.connect('deneme.db')
          cursor = conn.cursor()

          target_table_name = self.filter_combo_box.currentText()
          target_column_name = self.search_combo_box.currentText()
          target_value = self.searching_value_input.text()

          if not target_table_name or not target_column_name or not target_value:
               msg = QMessageBox()
               msg.setIcon(QMessageBox.Information)     
               msg.setWindowTitle("UYARI")
               msg.setText("Lütfen değerleri eksiksiz giriniz")
               #msg.setInformativeText("Yedek aldığınızdan emin olun")
               msg.setDetailedText("Tablo seçme kısmı boş ise, model ve data dosyalarınız kontrol ediniz. Parsing işleminin sağlıklı gerçekleştiğinden emin olun")
               msg.setStandardButtons(QMessageBox.Ok)
               msg.exec_()
               return
          else:
               self.tableWidget.clear()
               self.tableWidget.setRowCount(0)
               self.tableWidget.setColumnCount(0)
               cursor.execute(f'SELECT * FROM {target_table_name} WHERE {target_column_name} = ?', (target_value, ))
               rows = cursor.fetchall()
               conn.close()
               
               if rows:
                    self.tableWidget.setRowCount(len(rows))
                    self.tableWidget.setColumnCount(len(rows[0]))
                    for row_index, row_data in enumerate(rows):
                         for col_index, data in enumerate(row_data):
                              self.tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(data)))
               
               print('Search button clicked')          
                       
     def update_data(self):
          target_table_name = self.filter_combo_box.currentText()
          target_column_name = self.search_combo_box.currentText()
          new_value = self.updating_value_input.text()
          target_row = self.tableWidget.currentRow()
          target_column = self.tableWidget.currentColumn()
          if not target_table_name or not new_value:
               msg = QMessageBox()
               msg.setIcon(QMessageBox.Warning)
               msg.setWindowTitle("UYARI")
               msg.setText("Güncelleme yapılamadı!!!")
               msg.setInformativeText("Lütfen güncellemek için bilgilerin eksiksiz olduğundan emin olun.")
               msg.setStandardButtons(QMessageBox.Ok)
               msg.setDefaultButton(QMessageBox.Ok)
               msg.exec_()
          else: 
               conn = sqlite3.connect('deneme.db')
               cursor = conn.cursor()
               msg = QMessageBox()
               msg.setIcon(QMessageBox.Information)
               msg.setWindowTitle("UYARI")
               msg.setText("Güncellemek üzeresin")
               msg.setInformativeText("Yedek aldığınızdan emin olun")
               msg.setDetailedText("Güncellenen dosyaların geri dönüşümü yoktur")
               msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
               msg.setDefaultButton(QMessageBox.Cancel)
               response = msg.exec_()
               if response == QMessageBox.Ok:
                    if target_table_name.startswith('RM_KRS'):
                         old_value = self.tableWidget.item(target_row, target_column).text()
                         target_column_name = self.tableWidget.horizontalHeaderItem(target_column).text()
                         uye_kodu = self.tableWidget.item(target_row, 2).text()
                         update_query = f'UPDATE {target_table_name} SET "{target_column_name}" = ? WHERE uye_kodu = ?'
                         cursor.execute(update_query, (new_value, uye_kodu))
                    else:
                         new_value = self.updating_value_input.text()
                         target_row = self.tableWidget.currentRow()
                         target_column = self.tableWidget.currentColumn()
                         old_value = self.tableWidget.item(target_row, target_column).text()
                         target_column_name = self.tableWidget.horizontalHeaderItem(target_column).text()
                         uye_kodu = self.tableWidget.item(target_row, 1).text()
                         update_query = f'UPDATE {target_table_name} SET "{target_column_name}" = ? WHERE uye_kodu = ?'
                         cursor.execute(update_query, (new_value, uye_kodu))

                    conn.commit()
                    conn.close()

          # Update the database
          #update_query = f"UPDATE {target_table_name} SET {target_column_name} = ? WHERE {target_column_name} = ?"
          #cursor.execute(update_query, (new_value, old_value))
          #conn.commit()
          #conn.close()
          

               print('Update button clicked')
      
     def get_info(self):

          msg = QMessageBox()
          msg.setIcon(QMessageBox.Information)
          msg.setText("Info")
          msg.setInformativeText("Hüseyin Urak | Temmuz 2024 ")
          msg.setDetailedText("Öncelikle ham verinizi tanımlayan model dosyanızı, ardından ham verinizin bulunduğu dosyayı yükleyiniz. Model dosyasında ilk dört sütun sırasıyla 'Rapor Üst Grup Adı', 'Rapor Grup Adı', 'Rapor Adı', 'Rapor Alt Adı' olmalıdır. Beşinci sütun veri tabanında oluşturulacak sütun adını belirtir. Altıncı sütun sütunun başlangıç indeksini, yedinci sütun sütunun uzunluğunu belirtir. Model dosyanızın sütun adlarındaki özel karakterlerin yerine alt tire (_) kullanınız. Türkçe karakterler ile yazılan metinler İngilizce karakterlere çevrilir. Değişken isimleri 'Snake Case' düzeninde yapılmıştır. Sütun adlarında tekrar olmamasına özen gösteriniz. Tekrar olması durumunda hata ile karşılaşırsınız. Ham verinizin sütun uzunlukları model dosyanızdaki sütun uzunluklarına uygun olmalıdır. Daha detaylı bilgi için Linkedin @huseyinurak")
          msg.setWindowTitle("Info")
          msg.setStandardButtons(QMessageBox.Ok)
          msg.setFixedHeight(600)
          msg.setFixedWidth(600)
          msg.exec_()

app = QApplication(sys.argv) 
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1440)
widget.setFixedHeight(770)
widget.show()
sys.exit(app.exec_())
