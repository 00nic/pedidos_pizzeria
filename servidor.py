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
