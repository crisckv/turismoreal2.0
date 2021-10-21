#librerias (cx_Oracle coneccion con oracle)
from flask import Flask, request
import cx_Oracle
from flask.templating import render_template, render_template_string

try:
#coneccion a la bdd
    def getConnection() :
        conection = cx_Oracle.connect("TEST/123456@localhost:1521/xe")
        return conection
except cx_Oracle.Error as error:
        print(error)
