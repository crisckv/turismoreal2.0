import flask
from config import getConnection
from datetime import datetime
from flask import render_template, session, request, flash, redirect,url_for

funcionario = flask.Blueprint('funcionario', __name__)


#CHECK IN FUNCIONARIO----------------------------------------------------------------


@funcionario.route('/funcionario/<sessionFuncionario>', methods = ['POST','GET'])
def fnFuncionario(sessionFuncionario):
    sessionFuncionario = session['funcionario']
    if request.method == 'POST':
        Rut = request.form['consultaRut']
        return redirect(url_for('funcionario.CheckIn' , Rut = Rut))
    return render_template('/funcionario/funhome.html', sessionFuncionario = session['funcionario'])

@funcionario.route('/deleteReservaFunc/<id>', methods = ['POST','GET'])
def deleteReservaFunc(id):
    conection = getConnection()
    cursor = conection.cursor()
    cursor.execute('delete from pago where reserva_n_reserva = {0}'.format(id))
    cursor.execute('delete from reserva where n_reserva = {0}'.format(id))
    conection.commit()
    return redirect(url_for('funcionario.fnFuncionario', sessionFuncionario = session['funcionario']))

@funcionario.route('/CheckIn/<Rut>')
def CheckIn(Rut):
  conection = getConnection()
  cursor = conection.cursor()
  cursor.execute("select * from reserva where cliente_rut = ("+Rut+")")
  data = cursor.fetchall()
  cursor.close()
  return render_template('/funcionario/check_in.html', reservas = data) 
  

@funcionario.route('/update_check/<id>')
def update_check(id):
    if request.method == 'GET':
        ahora = datetime.today()
        conection = getConnection()
        cursor = conection.cursor()
        Estado = "En Uso"
        Departamento = "Ocupado"
        cursor.execute("select departamento_id_depto from reserva where n_reserva = ("+id+")")
        n = cursor.fetchone()
        m = str(n[0])
        statement = "update reserva set estado = :1 , check_in = :2  where n_reserva = :3"
        cursor.execute(statement,(Estado,ahora,id))
        stat= "update departamento set estado = :1 where id_depto = :2"
        cursor.execute(stat,(Departamento,m))
        conection.commit()
        return redirect(url_for('home'))


@funcionario.route('/checkout/<id>')
def checkout(id):
    conection = getConnection()
    cursor = conection.cursor()
    cursor.execute("select * from reserva where n_reserva = '"+id+"'")
    data = cursor.fetchone()
    cursor.close()
    return render_template('/funcionario/check_out.html', dato = data)

@funcionario.route('/terminar/<id>', methods=['POST'])
def terminar(id):
    if request.method == 'POST':
        multa = request.form['multa']
        ahora = datetime.today()
        Estado = "Terminado"
        Departamento = "Disponible"
        conection = getConnection()
        cursor = conection.cursor()
        statement = "update reserva set check_out = :1 , multa= :2 ,estado = :3 where n_reserva = :4"
        cursor.execute(statement,(ahora,multa,Estado,id))
        cursor.execute("select departamento_id_depto from reserva where n_reserva = ("+id+")")
        n = cursor.fetchone()
        m = str(n[0])
        stat= "update departamento set estado = :1 where id_depto = :2"
        cursor.execute(stat,(Departamento,m))
        conection.commit()
        return redirect(url_for('home'))

