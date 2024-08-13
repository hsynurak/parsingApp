PARSING APP
=============

08.08.2024 --- 2024 Summer Internship Project --- Hüseyin Urak

*    The application has two Python files. "main.py" and "ui.py".

*    Design (UI) created with QT-Creator application. (For ui file from created by QT-Creator mail me ==> huseyinurak@gmail.com)
     After created design file with drag-drop type, transformed to py type.
     The python file has one class object which includes two functions. 
     First function is create the buttons, labels, comboBox and other things. Second function is changing text of buttons and others.

*    main.py includes only one class object. In this class there are 17 functions. Some of this functions are includes some of them.

*         In main.py firstly import the necessary tools and ui file. 

*         At the "MainWindow" class there are two parameters, QWidget and Ui_Widget. Part of these parameters can use in the MainWindow with (.self) call.

*         First function is "def__init__(self):". 

*         With "super(MainWindow, self).__init__()" we can use property and methods of Qwidget and Ui_Widget.

*         "self.setupUi(self)" setups the UI components for the MainWindow.

*         "self.file_path_model", "self.file_path_data" and "self.table_names" defined here to use for more than one functions.

*         self.back_to_main_page_btn.clicked.connect(self.show_main)
          self.details.clicked.connect(self.show_details)
          self.browse_model_btn.clicked.connect(self.browsefiles)
          self.browse_data_btn.clicked.connect(self.browsefiles_data)
          self.parse_btn.clicked.connect(self.parsing)
          self.show_display_table_btn.clicked.connect(self.load_data)
          self.delete_btn.clicked.connect(self.delete_data)
          self.download_btn.clicked.connect(self.download_data)
          self.search_btn.clicked.connect(self.search_data)
          self.update_btn.clicked.connect(self.update_data)
          self.get_info_btn.clicked.connect(self.get_info) these are connects the buttons to their methods. 

*         self.parse_success.setText('')
          Changes the label text.

*         "show_main()" and "show_details()" functions changes the page when clicked to page changing buttons.

*         "parsing()" function is the main function of project. 
               It include three sub functions, "create_table_if_not_exists()", "fetch_data_from_db()" and "parsing_raw_data()"

               At the definiton part, 
                    ***First thing of the parsing function connecting with db. 
                    ***The data and model paths taked as data_input and model_input. To read the files at this file-path, use the "read_excel"   method from pd(Pandas).
                    *** While reading model file, top four column of the model file is about the group informations.(Parent Group Name, Group Name, Name, Sun Name). 
                    *** In this function we check this four column for each loop return. Because if there is an changed information, it will make another table on sql.
                         To check the rows, putted their indexes to "columns_to_check" list.
                         The cheking starts at the first row. Thats why the first rows index taking to "contol_row".
                    *** In the controlling section, to taking the column names there is "table_columns_name_list" and to taking the finished table names there is "table_names" list.
                    *** To parse row datas with sepificed index at the model file. We will need this indexes at the parsing.
               
               The first function of the parsing() function is "create_table_if_not_exists()".
                    *** We will use it to creating tables.
                    *** Checking, is there any column name in the "column_name_list" for the table.
                    *** If there is no problem, creating table name and adding to "table_names" list with "append()"
                    *** When create a table, we need column names and types. For this column names with type we have "formatted_column_with_types".
                    *** After this steps execute SQL code and create table.

               The second function of the parsing() function is "fetch_data_from_db()".
                    *** We will use it to table name datas dinamically to combo box that includes table names.
                    *** With "sqlite_master" take the pieces names which has type as "table". And put them to "data" variable with "fetchall()".

               The third function of the parsing() function is "parsing_raw_data()".
                    *** We will use it after creating table with informations from model file.
                    *** It has start and end indexes informations from model file. We will see how tok takes this informations after this descriptions.
                    *** Raw datas parsing this start, end indexes and putting to "parsed_data" list.

               After the functions are defined, loop start to read model file row by row.
                    *** If current row("row") and "control_row" have same values for the columns in the "columns_to_check", element at fourth column of the model taking as "column_name". While taking, replacing the some values with "_" and letters with English letters.
                    *** After creating "column_name", if it is already exists in the "table_column_name_list" a warning message will be shown. If it is a new column_name, it will append to "table_column_name_list".
                    *** To use at parsing_raw_data() function we need star_index and end_index from model file. Fifth column of the model file includes start index of each piece and sixth column of the model file includes length of this piece. 
                    *** With this values we can find "start_index" and "end_index" values.
                    *** To continue checking is there any change from columns_to_check, update the group informations values with current row values.
                    *** After updating this values, putting start_index and end_index values to correct length_list list.

               When reading model file finish, we have tables and start-end index values.

               To prevent any duplication problem, at the tables with a loop we delete each table with execute().

               With table names and fetch_data_from_db() function, combo box named as "filter_combo_box" filled with table names.
               
               Last part of the parsing() function is reading "df_data" that includes raw datas and apply the functions to this data.
                    *** Firstly transformed the data values to str as "str_x"
                    *** If data is one of the define type, it start the apply functions. Else it gives warning. 
                    *** For the defined datas, "parsing_raw_data" function is called with parameters as "str_x"(raw data) and "length_list_????"(start-end indexes) to "parsed_data" variable.
                    *** After calling function, parsed_data inserted to table.
               
               When parsing finished, comes a label about parsing success.

*         load_data() function working like a refresh page function.
               
               When clicked its button, it clears combo boxes and display table to prevent duplication.

               When table should display a table, a table must be choosen from combo box. This choosing has a variable named "filter_value".

               If "filter_value" is empty or not selected, a warning pop up will be shown.

               Else, all datas in the "filter_value" table is taken and adding to the display table.

               When this loading is finished "fetch_columns_from_db()" functions calling. This function will take column names from db. 

               End of the function, function calling to "columns" variable, and "columns" adding to "search_combo_box".

          
*         browsefiles() and browsefiles_data() functions using to taking model and data files.
               
               To make a filter for which type of files can adding, there is file_filter variable. 

               Opening a pop-up file choosing window with QFileDialog, getOpenFileName and file_filter as fname variable.

               If zeroth index of fname is not empty, file_path_data variables changing with fname variable and gives this path information into the text box

               