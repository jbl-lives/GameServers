from flask import Flask, request, jsonify
import mysql.connector

# initialize the flask application
app = Flask(__name__)

# Create database connection
conn = mysql.connector.connect(
    host="viaduct.proxy.rlwy.net",
    user="root",
    password="1-HHcAd341DH5BcbFAeEAAFBheh5d4gE",
    database="railway",
    port=23987
)

mycursor = conn.cursor()

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'