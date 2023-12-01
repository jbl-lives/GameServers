from flask import Flask, request, jsonify
import mysql.connector

# initialize the flask application
app = Flask(__name__)

# Create database connection
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="jabu@1994",
    database="tutorials",
    port=3306
)

mycursor = conn.cursor()

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'