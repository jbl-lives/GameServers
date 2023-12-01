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

@app.route('/get_all_games', methods=['GET'])
def get_all_games():
    try:
        sql = "SELECT * FROM games"
        mycursor.execute(sql)

        games_data = mycursor.fetchall()

        games_list = []

        for game_data in games_data:
            game = {
                'game_name': game_data[1],
                'price': str(game_data[2]),
                'rating': str(game_data[3]),
                'release_date': str(game_data[4])
            }
            games_list.append(game)

        return jsonify({'games': games_list}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500