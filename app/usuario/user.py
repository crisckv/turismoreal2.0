import flask
from config import getConnection
from datetime import datetime
from flask import render_template, session, request, flash, redirect,url_for, make_response
import pdfkit

user = flask.Blueprint('user', __name__)


@user.route('/usuario/<fnLog>')
def fnUsuario(fnLog):
    if 'email' in session:
        return render_template('/usuario/servicio.html',fnLog = session['email'] )



@user.route('/misDatos/<fnLog>')
def misDatos(fnLog):
    conection = getConnection()
    cursor = conection.cursor()
    cursor.execute("select * from cliente where correo = '"+fnLog+"'")
    data = cursor.fetchone()
    cursor.close()
    return render_template('/usuario/datos.html', fnLog = session['email'], dato = data)

@user.route('/updateMisDatos/<id>', methods=['POST'])
def updateMisDatos(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = int(request.form['edad'])
        telefono = int(request.form['telefono'])
        rutPrevio = int(id)
        conection = getConnection()
        cursor = conection.cursor()
        statement = "update cliente SET nombre = :1 ,apellido= :2, edad = :3 , telefono = :4  where rut = :5"
        cursor.execute(statement,(nombre,apellido,edad,telefono,rutPrevio))
        conection.commit()
        flash('Cliente Actualizado')
        shtml = '<script>alert("Datos ACtualizados Correctamente")</script>'
        return shtml + render_template('/usuario/Reservar.html')

@user.route('/reservar')
def reservar():
    return render_template('/usuario/reservar.html')

@user.route('/Viña')
def Viña():
    conection = getConnection()
    cursor = conection.cursor()
    cursor.execute("select estado from departamento where id_depto = 1")
    est = cursor.fetchone()
    if est[0] == "Ocupado":
        shtml = '<script>alert("Ente Departamento se encuentra reservado, Intentelo Mas tarde")</script>'
        return shtml + render_template('/usuario/reservar.html')
    if est[0] == "Mantencion":
        shtml = '<script>alert("Ente Departamento se encuentra En Mantencion, Intentelo Mas tarde")</script>'
        return shtml + render_template('/usuario/reservar.html')
    return render_template('/reserva/Viña.html')

@user.route('/Pucon')
def Pucon():
    conection = getConnection()
    cursor = conection.cursor()
    cursor.execute("select estado from departamento where id_depto = 4")
    est = cursor.fetchone()
    if est[0] == "Ocupado":
        shtml = '<script>alert("Ente Departamento se encuentra reservado, Intentelo Mas tarde")</script>'
        return shtml + render_template('/usuario/reservar.html')
    if est[0] == "Mantencion":
        shtml = '<script>alert("Ente Departamento se encuentra En Mantencion, Intentelo Mas tarde")</script>'
        return shtml + render_template('/usuario/reservar.html')
    return render_template('/reserva/Pucon.html')

@user.route('/LaSerena')
def LaSerena():
    conection = getConnection()
    cursor = conection.cursor()
    cursor.execute("select estado from departamento where id_depto = 3")
    est = cursor.fetchone()
    if est[0] == "Ocupado":
        shtml = '<script>alert("Ente Departamento se encuentra reservado, Intentelo Mas tarde")</script>'
        return shtml + render_template('/usuario/reservar.html')
    if est[0] == "Mantencion":
        shtml = '<script>alert("Ente Departamento se encuentra En Mantencion, Intentelo Mas tarde")</script>'
        return shtml + render_template('/usuario/reservar.html')
    return render_template('/reserva/LaSerena.html')

@user.route('/PuertoVaras')
def PuertoVaras():
    conection = getConnection()
    cursor = conection.cursor()
    cursor.execute("select estado from departamento where id_depto = 2")
    est = cursor.fetchone()
    if est[0] == "Ocupado":
        shtml = '<script>alert("Ente Departamento se encuentra reservado, Intentelo Mas tarde")</script>'
        return shtml + render_template('/usuario/reservar.html')
    if est[0] == "Mantencion":
        shtml = '<script>alert("Ente Departamento se encuentra En Mantencion, Intentelo Mas tarde")</script>'
        return shtml + render_template('/usuario/reservar.html')
    return render_template('/reserva/PuertoVaras.html')

@user.route('/ingresarReserva', methods=['POST'])
def ingresarReserva():
    conection = getConnection()
    cursor = conection.cursor()
    #formateo de fecha de entrada
    fecha1 = request.form['Entrada']
    a = datetime.strptime(fecha1, '%Y-%m-%d')
    b = str(datetime.strftime(a,'%d-%m-%y'))
    if a <= datetime.today():
        shtml = '<script>alert("La fecha de ingreso tiene que ser mayor al dia actual")</script>'
        return shtml + render_template('/usuario/Reservar.html')
    #formateo de fecha de Salida
    email = str(session["email"])
    sqlFetchDate = ("select rut from cliente where correo = ('"+email+"')")
    cursor.execute(sqlFetchDate)
    row = cursor.fetchone()
    row2 = str(row[0])
    dato1 = request.form['id']
    noche = request.form['noche']
    dato2 = "0"
    dato3 = "201"
    estado = request.form['Estado']
    cursor.execute("insert into reserva(estado,fecha_ingreso,cliente_rut,departamento_id_depto,transportista_id_tr,recepcionista_id_recep,noche) values ('"+estado+"','"+b+"',"+row2+","+dato1+","+dato2+","+dato3+","+noche+")")
    conection.commit()
    shtml = '<script>alert("Reserva Ingresada Correctamente, Revise sus reservas")</script>'
    return shtml + render_template('/usuario/Reservar.html')

#CANCELAR RESERVA-------------------------------------------------------------
@user.route('/cancelarReserva')
def cancelarRes():
    conection = getConnection()
    conection2 = getConnection()
    cur = conection.cursor()
    cur2 = conection2.cursor()
    correo = str(session['email'])
    cur2.execute("select rut from cliente where correo = ('"+correo+"')")
    data2 = cur2.fetchone()
    data3 = str(data2[0])
    cur2.execute("select rut from cliente where correo = ('"+correo+"')")
    cur.execute("select * from reserva where cliente_rut = ("+data3+")")
    data = cur.fetchall()
    cur.close()
    return render_template('/usuario/cancelar.html', reservas = data)


#ELIMINAR RESERVA-------------------------------------------------------------
@user.route('/deleteReserva/<id>', methods = ['POST','GET'])
def deleteReserva(id):
    conection = getConnection()
    cursor = conection.cursor()
    cursor.execute('delete from servicio where reserva_n_reserva = {0}'.format(id))
    cursor.execute('delete from pago where reserva_n_reserva = {0}'.format(id))
    cursor.execute('delete from reserva where n_reserva = {0}'.format(id))
    conection.commit()
    shtml = '<script>alert("Su Reserva ha sido Eliminada")</script>'
    return shtml + render_template('/usuario/reservar.html')
#FIN DE ELIMINAR RESERVA-------------------------------------------------------------

@user.route('/extras/<id>')
def extras(id):
    return render_template('/reserva/extras.html', id = id)



@user.route('/reservaExtra/<id>', methods=['POST'])
def reservaExtra(id):
    conection = getConnection()
    cursor = conection.cursor()
    cable = request.form['Cable']
    wifi = request.form['WIFI']
    piscina = request.form['Piscina']
    transporte = request.form['Transporte']
    idcable = request.form['idCable']
    idwifi = request.form['idWifi']
    idpiscina = request.form['idPiscina']
    idtransporte = request.form['idTransporte']
    precio = "4000"
    cursor.execute("select servicio from servicio where reserva_n_reserva = ("+id+")")
    data = cursor.fetchone()
    cursor.execute("select noche from reserva where n_reserva = ("+id+")")
    data2 = cursor.fetchone()
    dataconvert = int(data2[0])
    cursor.execute("select departamento_id_depto from reserva where n_reserva = ("+id+")")
    data3 = cursor.fetchone()
    dataconvert2 = int(data3[0])
    a = 0
    if cable == "SI":
        a = a + 4000
    if wifi == "SI":
        a = a + 4000
    if piscina == "SI":
        a = a + 4000
    if transporte == "SI":
        a = a + 4000
    print(a)
    print(cable)
    print(wifi)
    print(piscina)
    print(transporte)
    totalExtra = a
    if dataconvert2 == 1:
        total = 50000*dataconvert+totalExtra
        total2 = str(total)
        cursor.execute("update pago set total = "+total2+" where reserva_n_reserva = ("+id+")")
        conection.commit()
    if dataconvert2 == 2:
        total = 60000*dataconvert+totalExtra
        total2 = str(total)
        cursor.execute("update pago set total = '"+total2+"' where reserva_n_reserva = ("+id+")")
        conection.commit()
    if dataconvert2 == 3:
        total = 70000*dataconvert+totalExtra
        total2 = str(total)
        cursor.execute("update pago set total = '"+total2+"' where reserva_n_reserva = ("+id+")")
        conection.commit()
    if dataconvert2 == 4:
        total = 80000*dataconvert+totalExtra
        total2 = str(total)
        cursor.execute("update pago set total = '"+total2+"' where reserva_n_reserva = ("+id+")")
        conection.commit()
    if data != None:
        cursor.execute("update servicio set servicio = '"+cable+"' where id_servicio = 1 and reserva_n_reserva = ("+id+")")
        cursor.execute("update servicio set servicio = '"+wifi+"' where id_servicio = 2 and reserva_n_reserva = ("+id+")")
        cursor.execute("update servicio set servicio = '"+piscina+"' where id_servicio = 3 and reserva_n_reserva = ("+id+")")
        cursor.execute("update servicio set servicio = '"+transporte+"' where id_servicio = 4 and reserva_n_reserva = ("+id+")")
        conection.commit()
        return redirect(url_for('user.cancelarRes', fnLog = session['email']))
    else:
        cursor.execute("insert into servicio(id_servicio, servicio, precio, reserva_n_reserva) values ("+idcable+", '"+cable+"',"+precio+","+id+")")
        cursor.execute("insert into servicio(id_servicio, servicio, precio, reserva_n_reserva) values ("+idwifi+", '"+wifi+"',"+precio+","+id+")")
        cursor.execute("insert into servicio(id_servicio, servicio, precio, reserva_n_reserva) values ("+idpiscina+", '"+piscina+"',"+precio+","+id+")")
        cursor.execute("insert into servicio(id_servicio, servicio, precio, reserva_n_reserva) values ("+idtransporte+", '"+transporte+"',"+precio+","+id+")")
        conection.commit()
        return redirect(url_for('user.cancelarRes', fnLog = session['email']))
    
    


@user.route('/pagar/<id>')
def pagar(id):
    conection = getConnection()
    cursor = conection.cursor()
    cursor.execute("select total from pago where reserva_n_reserva = ('"+id+"')")
    value1 = cursor.fetchone()
    if value1[0] == None:
        return redirect(url_for('user.cancelarRes', fnLog = session['email']))
    Estado = "Pagado"
    stat= "update reserva set estado = :1 where cliente_rut = :2"
    cursor.execute(stat,(Estado,id))
    cursor.execute("select total from pago where reserva_n_reserva = ('"+id+"')")
    value = cursor.fetchone()
    data3 = int(value[0])
    pago30 = data3*0.3
    pago70 = data3*0.7
    conection.commit()
    return render_template('/reserva/pagar.html', id = id, pago30 = pago30, pago70 = pago70, data3 = data3)



@user.route('/pdf/<reserva>')
def pdf(reserva):
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
    rendered = render_template('/usuario/boleta.html',reserva = reserva, data = value, data2 = value2, data3 = value3, data4 = value4)
    pdf = pdfkit.from_string(rendered, False)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
    return response


@user.route('/pagado/<id>', methods = ["POST"])
def pagado(id):
    ocupado = "Ocupado"
    pagado = "Pagado"
    conection = getConnection()
    cursor = conection.cursor()
    cursor.execute("update reserva set estado = '"+pagado+"' where n_reserva =("+id+")")
    conection.commit()
    cursor.execute("select departamento_id_depto from reserva where n_reserva =("+id+")")
    value = cursor.fetchone()
    data3 = str(value[0])
    cursor.execute("update departamento set estado = '"+ocupado+"' where id_depto =("+data3+")")
    conection.commit()
    return redirect(url_for('user.cancelarRes', fnLog = session['email']))