import json

from flask import Flask, jsonify, request

# This is a server that processes requests for a tic tac toe game. You can make a board
# or make a move.
app = Flask(__name__)

# POST request that doesn't need any JSON info to be passed into it. Copies the content
# of a specific json file representing the start of a tic tac toe game onto another json
# file representing the current state of the game. Returns json information indicating
# the board has been reset.
@app.route("/makeBoard/", methods=["POST"])
def make_board():
    # Get start info from json file.
    with open("PythonProject/tictactioe/data/tictactoestart.json", "r") as inp:
        data = inp.read()
    # Write start info to game state json file.
    with open("PythonProject/tictactioe/data/tictactoe.json", "w") as outp:
        outp.write(data)
    # Return status.
    return {"status": "board reset"}

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
    with open("PythonProject/tictactioe/data/tictactoe.json", "r") as inp:
        json_data = json.load(inp)
    # Place correct player in correct position
    current_player = json_data['current_player']
    json_data['board'][key] = current_player
    # Switch players once placement has been completed.
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    json_data['current_player'] = current_player
    # Update current game state json file.
    with open("PythonProject/tictactioe/data/tictactoe.json", "w") as outp:
        json.dump(json_data, outp, indent=2)
    # Return ok status, current board state in json, and current player information.
    return jsonify({"status": "ok", "board": json_data["board"], "current_player": json_data["current_player"]})

def check_game_over():
    pass

if __name__ == "__main__":
    app.run()