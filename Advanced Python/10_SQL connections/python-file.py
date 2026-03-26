####SQL connections in python
'''
#syntax
import module_name
var = module_name.connect('file-name.db')
var1 = var.cursor()
var.execute('SQL query')
var.commit()
var.close()
'''

import sqlite3
'''
var = sqlite3.connect('sql-file.db')
var1 = var.cursor()
#var.execute('CREATE TABLE STUDENT2 (NAME VARCHAR(20) NOT NULL, SUBJECT VARCHAR(20) NOT NULL, MARKS NUMBER(3) NOT NULL)')
var.execute("INSERT INTO STUDENT VALUES('SAM', 'ENGLISH', 90)")
var.commit()
var.close()

##creaate atable flipcart with columns woth product id and procut name, insert products fetch out entire data  from flipcart
#save the chanfes and close the file
'''

##flipcart
flipcart = sqlite3.connect('flipcart-file.db')
flip = flipcart.cursor()
#flipcart.execute('CREATE TABLE FLIPCART (PRODUCT_ID NUMBER(10) PRIMARY KEY, PRODUCT_NAME VARCHAR(20) NOT NULL)')
#flipcart.execute("INSERT INTO FLIPCART VALUES(1, 'ASUS')")
#flipcart.execute("INSERT INTO FLIPCART VALUES(2, 'REDMI NOTE 9 PRO')")
flipcart.execute('SELECT * FROM FLIPCART')
flipcart.commit()
flipcart.close()



# rows = flip.fetchall()
# for row in rows:
#     print(row)
# flipcart.close()
