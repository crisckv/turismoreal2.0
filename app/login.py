import flask
import bcrypt
from flask import render_template, session, request, redirect, url_for, flash
from config import getConnection

logins = flask.Blueprint('logins', __name__)

#encriptamiento de contraseñas
semilla = bcrypt.gensalt()


#login inicio de sesion
@logins.route('/login')
def login():
    return render_template('login.html')


@logins.route('/entrar', methods =['POST']) 
def entrar():
    if request.method == 'POST':
        conection = getConnection()
        cursor = conection.cursor()
        cursor2 = conection.cursor()
        cursorAdmin = conection.cursor()
        cursorAdmin2 = conection.cursor()
        cursorFun = conection.cursor()
        cursorFun2 = conection.cursor()
        btEmail = request.form['btEmail']
        btPassword = request.form['btPassword']
        sqlFetchDate = ("select correo from cliente where correo = ('"+btEmail+"')")
        sqlFetchDate2 = ("select contraseña from cliente where correo = ('"+btEmail+"')")
        sqlAdmin = ("select usuario from administrador where usuario =('"+btEmail+"')")
        sqlAdmin2 =("select contrasena from administrador where contrasena = ('"+btPassword+"')")
        sqlFun = ("select correo from recepcionista where correo =('"+btEmail+"')")
        sqlFun2 =("select clave from recepcionista where clave = ('"+btPassword+"')")
        cursor.execute(sqlFetchDate)
        cursor2.execute(sqlFetchDate2)
        cursorAdmin.execute(sqlAdmin)
        cursorAdmin2.execute(sqlAdmin2)
        cursorFun.execute(sqlFun)
        cursorFun2.execute(sqlFun2)
        rowadmin = cursorAdmin.fetchone()
        rowadmin2 = cursorAdmin2.fetchone()
        rowfun = cursorFun.fetchone()
        rowfun2 = cursorFun2.fetchone()
        row = cursor.fetchone()
        print(rowfun)
        print(rowfun2)
        if rowadmin != None:
            if rowadmin2 != None:
                session['admin'] = request.form['btEmail']
                return redirect(url_for('admin.fnAdmin', sessionAdmin = session['admin']))
            else:
                shtml = '<script>alert("credenciales incorrectas")</script>'
                print(shtml)
            return shtml + render_template('/login.html')
        if rowfun != None:
            if rowfun2 != None:
                session['funcionario'] = request.form['btEmail']
                return redirect(url_for('funcionario.fnFuncionario', sessionFuncionario = session['funcionario']))
            else:
                shtml = '<script>alert("credenciales incorrectas")</script>'
                print(shtml)
            return shtml + render_template('/login.html')
        if row != None:
            row2 = cursor2.fetchone()
            str = ''.join(row2)
            row3 = str.encode("utf-8")
            print (str)
            newbt = btPassword.encode("utf-8")
            print(newbt)
            isSamePassword = bcrypt.checkpw(newbt,row3)
            if isSamePassword == True:
                print(isSamePassword)
                request.method == 'POST'
                session['email'] = request.form['btEmail']
                return redirect(url_for('user.fnUsuario', fnLog = session['email']))
            else:
                shtml = '<script>alert("credenciales incorrectas")</script>'
                print(shtml)
            return shtml + render_template('/login.html')
        else:
                shtml = '<script>alert("credenciales incorrectas")</script>'
                print(shtml)
        return shtml + render_template('/login.html')
    return render_template('/login.html')


@logins.route('/insertarUsuario', methods=['GET', 'POST'])
def insertarUsuario():
    conection = getConnection()
    cursor = conection.cursor()
    cursor2 = conection.cursor()
    rut = request.form['eRut']
    correo = request.form['eEmail']
    sqlFetchDate = ("select rut from cliente where rut = ("+rut+")")
    sqlFetchDate2 = ("select correo from cliente where correo = ('"+correo+"')")
    cursor.execute(sqlFetchDate)
    cursor2.execute(sqlFetchDate2)
    row = cursor.fetchone()
    row2 = cursor2.fetchone()
    shtml = '<script>alert("usuario ya cuenta con un rut registrado")</script>'
    shtml2 = '<script>alert("usuario ya cuenta con un correo registrado")</script>'
    if  row != None:
        return shtml + render_template('login.html') 
    if  row2 != None:
        return shtml2 + render_template('login.html') 
    else:
       request.method == 'POST'
       conection = getConnection()
       cursor = conection.cursor()
       rut = request.form['eRut']
       correo = request.form['eEmail']
       password = request.form['ePassword']
       passwordEncode = password.encode("utf-8")
       passwordEncriptado = bcrypt.hashpw(passwordEncode, semilla)
       passwordString = passwordEncriptado.decode('UTF-8')
       print("insertando")
       print("password codificado:" ,passwordEncode)
       print("password encriptado:", passwordEncriptado)
       print("password encriptado:", passwordString)
    cursor.execute("insert into cliente(rut,correo,contraseña) values("+rut+",'"+correo+"','"+passwordString+"')")
    conection.commit()
    flash('Contact Added successfully')
    shtml = '<script>alert("usuario registrado correctamente")</script>'
    shtml2 = '<script>alert("favor de iniciar sesion")</script>'
    return shtml +  shtml2 + render_template('index.html') 
    




