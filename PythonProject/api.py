import json
import os

from flask import Flask, jsonify, request

from tictactoe import Tictactoe

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "tictactioe", "data")
START_PATH = os.path.join(DATA_DIR, "tictactoestart.json")
GAME_PATH = os.path.join(DATA_DIR, "tictactoe.json")

# This is a server that processes requests for a tic tac toe game. You can make a board
# or make a move.
app = Flask(__name__)
game = Tictactoe()

# POST request that doesn't need any JSON info to be passed into it. Copies the content
# of a specific json file representing the start of a tic tac toe game onto another json
# file representing the current state of the game. Returns json information indicating
# the board has been reset.
@app.route("/makeBoard/", methods=["POST"])
def make_board():
    game.start_board()
    # Get start info from json file.
    with open(START_PATH, "r") as inp:
        data = inp.read()

    with open(GAME_PATH, "w") as outp:
        outp.write(data)
    json_data = json.loads(data)
    # Create models
    game.update_board(json_data)
    # Return update status.
    return {"status": "board_updated", "board": json_data["board"], "current_player": json_data["current_player"]}

# POST method that requires the following JSON infomation to be passed to it:
# "row": the row a move has been made at
# "col": the column a move has been made at
# It will place an X or O on the tile at depending on whose turn it is by updating
# the game state json file. Returns ok status, updated board data, and new current
# player.
@app.route("/makeMove/", methods=['POST'])
def make_move():
    # Retrieving data from request, storing in variables.
    data = request.get_json()
    row = str(data['row'])
    col = str(data['col'])
    key = row+","+col
    # Get current game state info from json file, store in variable.
    with open(GAME_PATH, "r") as inp:
        json_data = json.load(inp)
    # Check if tile can be played on.
    if game.is_valid_move(int(row), int(col)):
        # Place correct player in correct position.
        current_player = json_data['current_player']
        json_data['board'][key] = current_player
        game.update_board(json_data)
    else:
        # Return update status, current board state in json, and current player information.
        return jsonify({"status": "no_changes", "board": json_data["board"], "current_player": json_data["current_player"]})
    # Switch players once placement has been completed.
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    json_data['current_player'] = current_player
    # Update current game state json file.
    with open(GAME_PATH, "w") as outp:
        json.dump(json_data, outp, indent=2)

    if game.check_game_end(row, col) == True:
        return jsonify({
            "winner": game.get_winner(),
            "status": "board_updated",
            "board": json_data["board"],
            "current_player": json_data["current_player"]
            })
    else:
        # Return update status, current board state in json, and current player information.
        return jsonify({"status": "board_updated", "board": json_data["board"], "current_player": json_data["current_player"]})

if __name__ == "__main__":
    app.run()