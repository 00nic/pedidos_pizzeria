from flask import Flask, render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os
app = Flask(__name__, static_url_path='/static')
load_dotenv()

app.config['MYSQL_DB']  = os.getenv('MYSQL_DB')
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL__CURSORCLASS'] = os.getenv('MYSQL__CURSORCLASS')
app.config['MYSQL__KEY'] = os.getenv('MYSQL__KEY')

mysql = MySQL(app)

<<<<<<< HEAD
@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html')

@app.route('/compra')
def compra():
    return render_template('compra.html')
@app.route('/procesar_pedido', methods=['POST'])
def procesar_pedido():
    nombre = request.form['nombre']
    email = request.form['email']
    telefono = request.form['telefono']
    direccion = request.form['direccion']
    metodo_pago = request.form['metodo_pago']
    
    return 'Pedido recibido correctamente'

@app.route('/carrito')
def carrito():
    return render_template('carrito.html')

@app.route("/base")
def base():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM pizzas")
    data = cur.fetchall()
    return render_template( 'carrito.html', pizzas = data)

@app.route("/eliminar/<string:id>")
def eliminar(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM pizzas WHERE id = {0}".format(id))
    mysql.connection.commit()
    return redirect(url_for("base"))


if __name__ == '__main__':
    app.run(port=5000, debug=True)

=======


>>>>>>> origin/ramaCatalogo2
