#librerias (cx_Oracle coneccion con oracle)
from flask import Flask, request
import cx_Oracle
from flask.templating import render_template, render_template_string

try:
#coneccion a la bdd
    def getConnection() :
<<<<<<< HEAD
        conection = cx_Oracle.connect("turismo_real/123456@localhost:1521/xe")
=======
        conection = cx_Oracle.connect("TEST/123456@localhost:1521/xe")
>>>>>>> 1511be2a7e1758209e68db70997a3b1a6b681013
        return conection
except cx_Oracle.Error as error:
        print(error)
