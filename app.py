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


# Function to insert values into the database using values gathered from the user's input
@app.route('/insert_games', methods=['POST'])
def insert_games():
    try:
        g_name = request.form.get('gameName')
        g_price = int(request.form.get('gamePrice'))
        g_date = request.form.get('gameDate')
        g_rating = request.form.get('gameRating')

        sql = "INSERT INTO games (game_name, game_price, game_date, game_rating) VALUES (%s, %s, %s, %s)"
        val = (g_name, g_price, g_date, g_rating)

        mycursor.execute(sql, val)
        conn.commit()
        return jsonify({'message': 'Game data inserted successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Function to retrieve a single data set of game based on the user input
@app.route('/get_game', methods=['GET', 'POST'])
def get_game():
    try:
        if request.method == 'GET':
            g_name = request.args.get('gameName')
        elif request.method == 'POST':
            g_name = request.form.get('gameName')
        else:
            return jsonify({'message': 'Method not allowed'}), 405

        sql = "SELECT * FROM games WHERE game_name = %s"
        mycursor.execute(sql, (g_name,))

        game_data = mycursor.fetchone()

        if game_data:
            return jsonify([
                str(game_data[1]),  # game_name
                str(game_data[2]),  # price
                str(game_data[3]),  # rating
                str(game_data[4])  # release_date
            ]), 200
        else:
            return jsonify(*[
                'Game not found'
            ]), 404


    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/get_all_games', methods=['GET'])
def get_all_games():
    try:
        sql = "SELECT * FROM games"
        mycursor.execute(sql)

        games_data = mycursor.fetchall()

        games_list = []

        for game_data in games_data:
            game = {
                'game_name': str(game_data[1]),
                'price': str(game_data[2]),
                'rating': str(game_data[3]),
                'release_date': str(game_data[4])
            }
            games_list.append(game)

        return jsonify({'games': games_list}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
