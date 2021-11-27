#LIBRERIA PARA CONECTAR ORACLE Y PYTHON
import cx_Oracle

#CONNECION A LA BASE DE DATOS
try:
    def getConnection() :
        conection = cx_Oracle.connect("duoc/123456@localhost:1521/xe")
        return conection
except cx_Oracle.Error as error:
        print(error)
