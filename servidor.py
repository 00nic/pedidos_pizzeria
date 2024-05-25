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

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html')

@app.route('/compra')
def compra():
    return render_template('compra.html')

@app.route('/realizarPago')
def realizarPago():
    return render_template('compra.html')

@app.route('/carrito')
def carrito():
    return render_template('carrito.html')

@app.route('/procesar_pedido', methods=['POST'])
def procesar_pedido():
    email = request.form['email']
    telefono = request.form['telefono']
    direccion = request.form['direccion']
    metodo_pago = request.form['metodo_pago']
    """
    if not email or not telefono or not direccion or not metodo_pago:
        return {'error': 'Todos los campos son obligatorios'}, 400
    else:
        return 'Pedido recibido correctamente'"""

if __name__ == '__main__':
    app.run(port=5000, debug=True)