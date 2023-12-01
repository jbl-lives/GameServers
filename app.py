from flask import Flask
import mysql.connector


app = Flask(__name__)

conn = mysql.connector.connect(
    host="192.168.31.100",
    user="root",
    password="jabu@1994",
    database="tutorials"
)

@app.route('/')
def hello_world():
    return 'Hello, Zuma!'