from flask import Flask, render_template, request, redirect, url_for, flash , session, render_template_string
import bcrypt
from config import getConnection

app = Flask(__name__)

#Se establece llave secreta
app.secret_key = "mysecretkey"

#encriptamiento de contraseñas
semilla = bcrypt.gensalt()

@app.route('/')
def home():
    if 'email' in session:
        return redirect(url_for('servicio'))
    return render_template('index.html')
  
@app.route('/login')
def login():
    if 'email' in session:
        return redirect(url_for('servicio'))
    return render_template('login.html')

@app.route('/insertar_usuario', methods=['GET', 'POST'])
def insertar_usuario():
    conection = getConnection()
    cursor = conection.cursor()
    cursor2 = conection.cursor()
    rut = request.form['erut']
    correo = request.form['eemail']
    sql_fetch_date = ("SELECT RUT FROM CLIENTE WHERE RUT = ("+rut+")")
    sql_fetch_date2 = ("SELECT correo FROM CLIENTE WHERE correo = ('"+correo+"')")
    cursor.execute(sql_fetch_date)
    cursor2.execute(sql_fetch_date2)
    row = cursor.fetchone()
    row2 = cursor2.fetchone()
    shtml = '<script>alert("usuario ya cuenta con un RUT registrado")</script>'
    shtml2 = '<script>alert("usuario ya cuenta con un Correo registrado")</script>'
    if  row != None:
        return shtml + render_template('login.html') 
    if  row2 != None:
        return shtml2 + render_template('login.html') 
    else:
       request.method == 'POST'
       conection = getConnection()
       cursor = conection.cursor()
       rut = request.form['erut']
       correo = request.form['eemail']
       password = request.form['epassword']
       password_encode = password.encode("utf-8")
       password_encriptado = bcrypt.hashpw(password_encode, semilla)
       passwordstring = password_encriptado.decode('UTF-8')
       print("insertando")
       print("password codificado:" ,password_encode)
       print("password encriptado:", password_encriptado)
       print("password encriptado:", passwordstring)
    cursor.execute("INSERT INTO CLIENTE(rut,correo,password) VALUES("+rut+",'"+correo+"','"+passwordstring+"')")
    conection.commit()
    flash('Contact Added successfully')
    shtml = '<script>alert("usuario registrado correctamente")</script>'
    shtml2 = '<script>alert("favor de iniciar sesion")</script>'
    return shtml +  shtml2 + render_template('login.html') 



@app.route('/entrar', methods =['POST','GET']) 
def entrar():
    conection = getConnection()
    cursor = conection.cursor()
    cursor2 = conection.cursor()
    btemail = request.form['btemail']
    btpassword = request.form['btpassword']
    sql_fetch_date = ("SELECT CORREO FROM CLIENTE WHERE CORREO = ('"+btemail+"')")
    sql_fetch_date2 = ("SELECT PASSWORD FROM CLIENTE WHERE CORREO = ('"+btemail+"')")
    cursor.execute(sql_fetch_date)
    cursor2.execute(sql_fetch_date2)
    row = cursor.fetchone()
    row2 = cursor2.fetchone()
    str = ''.join(row2)
    row3 = str.encode("utf-8")
    print (str)
    newbt = btpassword.encode("utf-8")
    print(newbt)
    issamepassword = bcrypt.checkpw(newbt,row3)
    shtml = '<script>alert("no coincide ningun usuario con estas credenciales")</script>'
    if row != None:
        if issamepassword == True:
            print(issamepassword)
            request.method == 'POST'
            session['email'] = request.form['btemail']
            return redirect(url_for('servicio'))
        else:
            print(issamepassword)
            
    
            
    else:
        return shtml + render_template('login.html')


@app.route('/salir')
def salir():
    # Clear the email stored in the session object
    session.pop('email', default=None)
    return render_template('index.html')


@app.route('/servicio')
def servicio():
    return render_template('usuario/servicio.html')

if __name__ == '__main__':
 app.run(debug=True)


