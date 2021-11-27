import flask
from flask_mail import Mail, Message
from flask import render_template, session, redirect, url_for
from app.login import logins
from app.usuario.user import user
from app.funcionario.funcionary import funcionario
from app.administrador.admin import admin
from config import getConnection

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#RUTA PRINCIPAL
@app.route('/')
def home():
    if 'admin' in session:
        return redirect(url_for('admin.fnAdmin', sessionAdmin = session['admin']))
    if 'email' in session:
        return redirect(url_for('user.fnUsuario', fnLog = session['email']))
    if 'funcionario' in session:
        return redirect(url_for('funcionario.fnFuncionario', sessionFuncionario = session['funcionario']))
    return render_template('index.html')

@app.route('/salir')
def salir():
    session.pop('admin', default=None)
    session.pop('email', default=None)
    session.pop('funcionario', default=None)
    return redirect(url_for('home'))


#INICIADOR DE APP


#LLAVE SECRETA
app.secret_key = "mySecretKey"

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'turismoreal2021duoc@gmail.com'
app.config['MAIL_PASSWORD'] = 'portafolioduoc'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/Send/<reserva>')
def Send(reserva):
    conection = getConnection()
    cursor = conection.cursor()
    cursor.execute("select cliente_rut from reserva where n_reserva = ("+reserva+")")
    value0 = cursor.fetchone()
    strim0 = str(value0[0])
    cursor.execute("select * from reserva where n_reserva = ("+reserva+")")
    value = cursor.fetchone()
    strim = str(value[8])
    cursor.execute("select * from cliente where rut = ('"+strim0+"')")
    value2 = cursor.fetchone()
    cursor.execute("select * from departamento where id_depto = ("+strim+")")
    value3 = cursor.fetchone()
    cursor.execute("select * from pago where reserva_n_reserva = ("+reserva+")")
    value4 = cursor.fetchone()
    data2 = value2
    msg = Message('Boleta Turismo Real', sender='turismoreal2021duoc@gmail.com', recipients=[data2[3]])
    msg.body = render_template('/usuario/boletaCorreo.html',reserva = reserva, data = value, data2 = value2, data3 = value3, data4 = value4)
    mail.send(msg)
    shtml = '<script>alert("Correo Enviado Correctamente")</script>'
    return shtml + render_template('/funcionario/funhome.html', sessionFuncionario = session['funcionario'])


#BLUEPRINTS (RUTAS DE LAS FUNCIONES)
app.register_blueprint(logins)
app.register_blueprint(user)
app.register_blueprint(admin)
app.register_blueprint(funcionario)






#CORRER APLICACION
app.run()