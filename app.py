from flask import Flask
from flask import render_template,request,redirect,url_for
from flaskext.mysql import MySQL
from datetime import datetime #Nos permitirá darle el nombre a la foto
from flask import send_from_directory
import os
app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
# app.config['MYSQL_DATABASE_PORT']='3306'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='root'
app.config['MYSQL_DATABASE_BD']='sistema'
CARPETA= os.path.join('uploads')
app.config['CARPETA']=CARPETA
mysql.init_app(app)

#sentencia para crear la tabla en mysql
# CREATE TABLE `sistema`.`empleados` (
#   `id` INT NOT NULL AUTO_INCREMENT,
#   `nombre` VARCHAR(45) NULL,
#   `correo` VARCHAR(45) NULL,
#   `foto` VARCHAR(255) NULL,
#   PRIMARY KEY (`id`));

@app.route('/')
def index():

    sql = "SELECT * FROM `sistema`.`empleados`;"   
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    
    empleados=cursor.fetchall()
    conn.commit()

    return render_template('empleados/index.html',empleados=empleados)



@app.route('/create')
def create():
    return render_template('empleados/create.html')


@app.route('/store', methods=['POST'])
def storage():
    # sql = "INSERT INTO `sistema`.`empleados` (`id`, `nombre`, `correo`, ` foto`) VALUES (NULL, 'Juan Pablo', 'juanpablo@gmail.com', 'juanpablo.jpg');"
    _nombre=request.form['txtNombre']
    _correo=request.form['txtCorreo']
    _foto=request.files['txtFoto']

    now= datetime.now()
    tiempo= now.strftime("%Y%H%M%S")

    nuevoNombreFoto="vacio" #lo pongo para que me persista en la bd

    if _foto.filename!='':
        nuevoNombreFoto=tiempo+_foto.filename
        _foto.save("uploads/"+nuevoNombreFoto)
    
    
    sql = "INSERT INTO `sistema`.`empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, %s, %s, %s);" 

    datos=(_nombre,_correo,nuevoNombreFoto)

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return redirect('/')


@app.route('/destroy/<int:id>')
def destroy(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM `sistema`.`empleados` WHERE id=%s", (id))
    conn.commit()
    return redirect('/')

@app.route('/edit/<int:id>')
def edit(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `sistema`.`empleados` WHERE id=%s", (id))
    empleados=cursor.fetchall()
    conn.commit()
    return render_template('empleados/edit.html', empleados=empleados)


@app.route('/update', methods=['POST'])
def update():
    _nombre=request.form['txtNombre']
    _correo=request.form['txtCorreo']
    _foto=request.files['txtFoto']
    id=request.form['txtID']
    sql = "UPDATE `sistema`.`empleados` SET `nombre`=%s, `correo`=%s WHERE id=%s;"
    datos=(_nombre,_correo,id)

    conn = mysql.connect()
    cursor = conn.cursor()

    now= datetime.now()
    tiempo= now.strftime("%Y%H%M%S")

    nuevoNombreFoto="vacio" #lo pongo para que me persista en la bd
    if _foto.filename!='':
        nuevoNombreFoto=tiempo+_foto.filename
        _foto.save("uploads/"+nuevoNombreFoto)
        cursor.execute("SELECT foto FROM `sistema`.`empleados` WHERE id=%s", id)
        fila= cursor.fetchall()
        os.remove(os.path.join(app.config['CARPETA'], fila[0][0]))
        cursor.execute("UPDATE `sistema`.`empleados` SET foto=%s WHERE id=%s;", (nuevoNombreFoto, id))
        conn.commit()

    cursor.execute(sql,datos)
    conn.commit()
    return redirect('/')

@app.route('/destroy/<int:id>')
def func():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM `sistema`.`empleados` WHERE id=%s;", (id))
    conn.commit()
    return redirect('/')


@app.route('/uploads/<nombreFoto>')
def uploads(nombreFoto):
    return send_from_directory(app.config['CARPETA'], nombreFoto)

if __name__=='__main__':
    app.run(debug=True)