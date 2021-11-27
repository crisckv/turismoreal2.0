import flask 
import pdfkit
from config import getConnection
from flask import render_template, session, request, redirect,url_for, make_response

admin = flask.Blueprint('admin', __name__)


@admin.route('/admin/<sessionAdmin>')
def fnAdmin(sessionAdmin):
    sessionAdmin = session['admin']
    conection = getConnection()
    cursor = conection.cursor()
    cursor.execute('SELECT * FROM Departamento')
    data = cursor.fetchall()
    cursor.close()
    return render_template('/admin/admin.html', sessionAdmin = session['admin'], habitaciones = data)

@admin.route('/editar_hab/<id>', methods = ['POST', 'GET'])
def editar_hab(id):
    conection = getConnection()
    cursor = conection.cursor()
    cursor.execute("select * from departamento where id_depto = '"+id+"'")
    data = cursor.fetchall()
    cursor.close()
    return render_template('admin/editar_hab.html', depa = data[0])
   
@admin.route('/updateDepa/<id>', methods=['POST'])
def updateDepa(id):
    if request.method == 'POST':
        conection = getConnection()
        cursor = conection.cursor()
        mantencion = request.form['mantencion']
        statement = "update departamento set estado= :1 WHERE id_depto =:2"
        cursor.execute(statement,(mantencion,id))
        conection.commit()
        
        return redirect(url_for('home'))

#administracion de los departamentos-----------------------------------------------------------------------------------------------------------

@admin.route('/departamentos')
def departamentos():
    conection = getConnection()
    cur = conection.cursor()
    cur.execute('select * from departamento order by id_depto asc')
    data = cur.fetchall()
    cur.close()
    return render_template('/admin/deptos.html', deptos = data)

@admin.route('/agregar_depto', methods=['POST','GET'])
def agregar_depto():
    if request.method == 'POST':
        conection = getConnection()
        conection2 = getConnection()
        cursor = conection.cursor()
        conection2 = conection2.cursor()
        nombredepto = request.form['nombredepto']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        valor = request.form['valor']
        ase = str(session['admin'])
        abb = conection2.execute("select id_admin from administrador where usuario = '"+ase+"'")
        rowadminid = abb.fetchone()
        rowadminid2 = str(rowadminid[0])
        cursor.execute("INSERT INTO departamento(nombre, direccion, telefono,valorizacion , administrador_id_admin) VALUES ('"+nombredepto+"','"+direccion+"',"+telefono+","+valor+","+rowadminid2+")")
        conection.commit()
        return redirect(url_for('departamentos'))


@admin.route('/edit/<id>', methods = ['POST', 'GET'])
def get_contact(id):
    conection = getConnection()
    cursor = conection.cursor()
    cursor.execute("SELECT * FROM departamento WHERE id_depto = '"+id+"'")
    data = cursor.fetchall()
    cursor.close()
    return render_template('admin/edit-depto.html', depto = data[0])

@admin.route('/update/<id>', methods=['POST'])
def update_depto(id):
    if request.method == 'POST':
        nombredepto = request.form['nombredepto']
        direccion = request.form['direccion']
        telefono = int(request.form['telefono'])
        valor = int(request.form['valor'])
        conection = getConnection()
        conection2 = getConnection()
        conection2 = conection2.cursor()
        id3 = int(id)
        cursor = conection.cursor()
        ase = str(session['admin'])
        abb = conection2.execute("select id_admin from administrador where usuario = '"+ase+"'")
        rowadminid = abb.fetchone()
        rowadminid2 = int(rowadminid[0])
        statement = "UPDATE departamento SET nombre = :1 , direccion = :2 , telefono = :3 , valorizacion = :4 , administrador_id_admin = :5 WHERE id_depto = :6"
        cursor.execute(statement, (nombredepto, direccion, telefono ,valor, rowadminid2, id3))
        conection.commit()
        return redirect(url_for('departamentos'))

@admin.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_depto(id):
    conection = getConnection()
    cursor = conection.cursor()
    cursor.execute('DELETE FROM departamento WHERE id_depto = {0}'.format(id))
    conection.commit()
    return redirect(url_for('departamentos'))


#administracion de los clientes-----------------------------------------------------------------------------------------------------------

@admin.route('/clientes')
def clientes():
    conection = getConnection()
    cur = conection.cursor()
    cur.execute('SELECT * FROM cliente order by rut asc')
    data = cur.fetchall()
    cur.close()
    return render_template('/admin/clientes.html', clientes = data)


@admin.route('/editar/<id>', methods = ['POST', 'GET'])
def get_cliente(id):
    conection = getConnection()
    cursor = conection.cursor()
    cursor.execute("select * from cliente where rut = '"+id+"'")
    data = cursor.fetchall()
    cursor.close()
    return render_template('admin/edit-clientes.html', cliente = data[0])



@admin.route('/update_cli/<id>', methods=['POST'])
def update_cliente(id):
    if request.method == 'POST':
        rut = int(request.form['rut'])
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = int(request.form['edad'])
        telefono = int(request.form['telefono'])
        correo = request.form['correo']
        rutprevio = int(id)
        conection = getConnection()
        cursor = conection.cursor()
        statement = "update cliente SET rut = :1, nombre = :2 ,apellido= :3, edad = :4 , telefono = :5 , correo = :6 where rut = :7"
        cursor.execute(statement,(rut,nombre,apellido,edad,telefono,correo,rutprevio))
        conection.commit()
        return redirect(url_for('clientes'))


@admin.route('/delete_cli/<string:id>', methods = ['POST','GET'])
def delete_cli(id):
    conection = getConnection()
    cursor = conection.cursor()
    cursor.execute('delete FROM cliente where rut = {0}'.format(id))
    conection.commit()
    return redirect(url_for('clientes'))

@admin.route('/pdf_template')
def pdf_template():
    rendered = render_template('/admin/reporte.html')
    pdf = pdfkit.from_string(rendered, False)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=output.pdf'

    return response
