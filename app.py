<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for, flash , session
=======
<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for, flash , session
=======
<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for, flash , session
=======
from flask import Flask, render_template, request, redirect, url_for, flash , session, render_template_string
>>>>>>> 1511be2a7e1758209e68db70997a3b1a6b681013
>>>>>>> d7d2b04ac57d0f73d994057d949996550205ce03
>>>>>>> 270e952fe558b8ea65cace5a8dbec1d3ae183d09
import bcrypt
from config import getConnection

app = Flask(__name__)

#Se establece llave secreta
app.secret_key = "mysecretkey"

#encriptamiento de contraseñas
semilla = bcrypt.gensalt()

@app.route('/')
def home():
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> d7d2b04ac57d0f73d994057d949996550205ce03
>>>>>>> 270e952fe558b8ea65cace5a8dbec1d3ae183d09
    if 'admin' in session:
        return fnAdmin([])
    if 'email' in session:
        return fnUsuario([])
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
    if 'email' in session:
        return redirect(url_for('servicio'))
>>>>>>> 1511be2a7e1758209e68db70997a3b1a6b681013
>>>>>>> d7d2b04ac57d0f73d994057d949996550205ce03
>>>>>>> 270e952fe558b8ea65cace5a8dbec1d3ae183d09
    return render_template('index.html')
  
@app.route('/login')
def login():
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> d7d2b04ac57d0f73d994057d949996550205ce03
>>>>>>> 270e952fe558b8ea65cace5a8dbec1d3ae183d09
    if 'admin' in session:
        return fnAdmin([])
    if 'email' in session:
        return fnUsuario([])
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
    if 'email' in session:
        return redirect(url_for('servicio'))
>>>>>>> 1511be2a7e1758209e68db70997a3b1a6b681013
>>>>>>> d7d2b04ac57d0f73d994057d949996550205ce03
>>>>>>> 270e952fe558b8ea65cace5a8dbec1d3ae183d09
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
<<<<<<< HEAD
    cursor.execute("INSERT INTO CLIENTE(rut,correo,clave) VALUES("+rut+",'"+correo+"','"+passwordstring+"')")
=======
<<<<<<< HEAD
    cursor.execute("INSERT INTO CLIENTE(rut,correo,clave) VALUES("+rut+",'"+correo+"','"+passwordstring+"')")
=======
<<<<<<< HEAD
    cursor.execute("INSERT INTO CLIENTE(rut,correo,clave) VALUES("+rut+",'"+correo+"','"+passwordstring+"')")
=======
    cursor.execute("INSERT INTO CLIENTE(rut,correo,password) VALUES("+rut+",'"+correo+"','"+passwordstring+"')")
>>>>>>> 1511be2a7e1758209e68db70997a3b1a6b681013
>>>>>>> d7d2b04ac57d0f73d994057d949996550205ce03
>>>>>>> 270e952fe558b8ea65cace5a8dbec1d3ae183d09
    conection.commit()
    flash('Contact Added successfully')
    shtml = '<script>alert("usuario registrado correctamente")</script>'
    shtml2 = '<script>alert("favor de iniciar sesion")</script>'
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> d7d2b04ac57d0f73d994057d949996550205ce03
>>>>>>> 270e952fe558b8ea65cace5a8dbec1d3ae183d09
    return shtml +  shtml2 + render_template('index.html') 
    


<<<<<<< HEAD
@app.route('/entrar', methods =['POST']) 
=======
<<<<<<< HEAD
@app.route('/entrar', methods =['POST']) 
=======
<<<<<<< HEAD
@app.route('/entrar', methods =['POST','GET']) 
=======
@app.route('/entrar', methods =['POST']) 
>>>>>>> c4668f7cff593c63ec13a279ac0470de1ea3eb7f
>>>>>>> d7d2b04ac57d0f73d994057d949996550205ce03
>>>>>>> 270e952fe558b8ea65cace5a8dbec1d3ae183d09
def entrar():
    if request.method == 'POST':
        conection = getConnection()
        cursor = conection.cursor()
        cursor2 = conection.cursor()
        cursoradmin = conection.cursor()
        cursoradmin2 = conection.cursor()
        btemail = request.form['btemail']
        btpassword = request.form['btpassword']
        sql_fetch_date = ("SELECT CORREO FROM CLIENTE WHERE CORREO = ('"+btemail+"')")
        sql_fetch_date2 = ("SELECT clave FROM CLIENTE WHERE CORREO = ('"+btemail+"')")
        sql_admin = ("select usuario from admin where usuario =('"+btemail+"')")
        sql_admin2 =("SELECT contraseña FROM admin WHERE contraseña = ('"+btpassword+"')")
        cursor.execute(sql_fetch_date)
        cursor2.execute(sql_fetch_date2)
        cursoradmin.execute(sql_admin)
        cursoradmin2.execute(sql_admin2)
        rowadmin = cursoradmin.fetchone()
        rowadmin2 = cursoradmin2.fetchone()
        row = cursor.fetchone()
        if rowadmin != None:
            if rowadmin2 != None:
                session['admin'] = request.form['btemail']
                return fnAdmin(session['admin'])
            else:
                shtml = '<script>alert("credenciales incorrectas")</script>'
                print(shtml)
            return shtml + render_template('/login.html')
        if row != None:
            row2 = cursor2.fetchone()
            str = ''.join(row2)
            row3 = str.encode("utf-8")
            print (str)
            newbt = btpassword.encode("utf-8")
            print(newbt)
            issamepassword = bcrypt.checkpw(newbt,row3)
            if issamepassword == True:
                print(issamepassword)
                request.method == 'POST'
                session['email'] = request.form['btemail']
                return fnUsuario(session['email'])
            else:
                shtml = '<script>alert("credenciales incorrectas")</script>'
                print(shtml)
            return shtml + render_template('/login.html')
        else:
                shtml = '<script>alert("credenciales incorrectas")</script>'
                print(shtml)
        return shtml + render_template('/login.html')
        
    return render_template('/login.html')


@app.route('/usuario')
def fnUsuario(fnlog):
    if 'admin' in session:
        return fnAdmin([])
    if 'email' in session:
        fnlog = session['email']
        return render_template('/usuario/servicio.html')


@app.route('/admin')
def fnAdmin(sessadmin):
    sessadmin = session['admin']
    return render_template('/admin/admin.html')

@app.route('/salir')
def salir():
    session.pop('admin', default=None)
    session.pop('email', default=None)
    mssge = '<script>alert("Sesion finalizada correctamente")</script>'
    return render_template('index.html') + mssge



#administracion de los departamentos-----------------------------------------------------------------------------------------------------------
@app.route('/departamentos')
def departamentos():
    conection = getConnection()
    cur = conection.cursor()
<<<<<<< HEAD
    cur.execute('SELECT * FROM departamento order by ID asc')
=======
<<<<<<< HEAD
    cur.execute('SELECT * FROM departamento order by ID asc')
=======
<<<<<<< HEAD
    cur.execute('SELECT * FROM departamento')
=======
    cur.execute('SELECT * FROM departamento order by ID asc')
>>>>>>> c4668f7cff593c63ec13a279ac0470de1ea3eb7f
>>>>>>> d7d2b04ac57d0f73d994057d949996550205ce03
>>>>>>> 270e952fe558b8ea65cace5a8dbec1d3ae183d09
    data = cur.fetchall()
    cur.close()
    return render_template('/admin/deptos.html', deptos = data)

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
@app.route('/agregar_depto', methods=['POST'])
def agregar_depto():
    if request.method == 'POST':
        fullname = request.form['departamento']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contacts (fullname, phone, email) VALUES (%s,%s,%s)", (fullname, phone, email))
        mysql.connection.commit()
        flash('Contact Added successfully')
        return redirect(url_for('Index'))






=======
>>>>>>> d7d2b04ac57d0f73d994057d949996550205ce03
>>>>>>> 270e952fe558b8ea65cace5a8dbec1d3ae183d09
@app.route('/agregar_depto', methods=['POST','GET'])
def agregar_depto():
    if request.method == 'POST':
        conection = getConnection()
        conection2 = getConnection()
        cursor = conection.cursor()
        conection2 = conection2.cursor()
        nombredepto = request.form['nombredepto']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        ase = str(session['admin'])
        abb = conection2.execute("select id from admin where usuario = '"+ase+"'")
        rowadminid = abb.fetchone()
        rowadminid2 = str(rowadminid[0])
        cursor.execute("INSERT INTO departamento(nombre, direccion, telefono, admin_id) VALUES ('"+nombredepto+"','"+direccion+"',"+telefono+","+rowadminid2+")")
        conection.commit()
        flash('Contact Added successfully')
        return redirect(url_for('departamentos'))


@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_contact(id):
    conection = getConnection()
    cursor = conection.cursor()
    cursor.execute("SELECT * FROM departamento WHERE ID = '"+id+"'")
    data = cursor.fetchall()
    cursor.close()
    print(data[0])
    return render_template('admin/edit-depto.html', depto = data[0])

@app.route('/update/<id>', methods=['POST'])
def update_depto(id):
    if request.method == 'POST':
        nombredepto = request.form['nombredepto']
        direccion = request.form['direccion']
        telefono = int(request.form['telefono'])
        conection = getConnection()
        conection2 = getConnection()
        conection2 = conection2.cursor()
        id3 = int(id)
        cursor = conection.cursor()
        ase = str(session['admin'])
        abb = conection2.execute("select id from admin where usuario = '"+ase+"'")
        rowadminid = abb.fetchone()
        rowadminid2 = int(rowadminid[0])
        statement = "UPDATE departamento SET nombre = :1 , direccion = :2 , telefono = :3 , admin_id = :4 WHERE id = :5"
        cursor.execute(statement, (nombredepto, direccion, telefono, rowadminid2, id3))
        flash('Contact Updated Successfully')
        conection.commit()
        return redirect(url_for('departamentos'))

@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_depto(id):
    conection = getConnection()
    cursor = conection.cursor()
    cursor.execute('DELETE FROM departamento WHERE id = {0}'.format(id))
    conection.commit()
    flash('Contact Removed Successfully')
    return redirect(url_for('departamentos'))
#FIN administracion de los departamentos-------------------------------------------------------------------------------------------------------------------
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> c4668f7cff593c63ec13a279ac0470de1ea3eb7f
=======
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
>>>>>>> 1511be2a7e1758209e68db70997a3b1a6b681013
>>>>>>> d7d2b04ac57d0f73d994057d949996550205ce03
>>>>>>> 270e952fe558b8ea65cace5a8dbec1d3ae183d09

if __name__ == '__main__':
 app.run(debug=True)


