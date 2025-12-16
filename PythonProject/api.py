import json

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/makeBoard/", methods=["POST"])
def make_board():
    with open("tictactoestart.json", "r") as inp:
        data = inp.read()

    with open("tictactoe.json", "w") as outp:
        outp.write(data)

    return {"status": "board reset"}

@app.route("/makeMove/", methods=['POST'])
def make_move():
    data = request.get_json()
    row = str(data['row'])
    col = str(data['col'])
    inp = open("tictactoe.json", "r")
    json_data = json.load(inp)
    current_player = json_data['current_player']
    json_data[row+","+col] = current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    json_data['current_player'] = current_player
    outp = open("tictactoe.json", "w")
    return jsonify({"status": "ok"})

def check_game_over():
    pass

if __name__ == "__main__":
    app.run()