import json

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/makeBoard/", methods=["POST"])
def make_board():
    with open("PythonProject/tictactoestart.json", "r") as inp:
        data = inp.read()

    with open("PythonProject/tictactioe/data/tictactoe.json", "w") as outp:
        outp.write(data)

    return {"status": "board reset"}

@app.route("/makeMove/", methods=['POST'])
def make_move():
    data = request.get_json()
    row = str(data['row'])
    col = str(data['col'])
    key = row+","+col

    with open("PythonProject/tictactioe/data/tictactoe.json", "r") as inp:
        json_data = json.load(inp)
    
    current_player = json_data['current_player']
    json_data['board'][key] = current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    json_data['current_player'] = current_player

    with open("PythonProject/tictactioe/data/tictactoe.json", "w") as outp:
        json.dump(json_data, outp, indent=2)
    return jsonify({"status": "ok", "board": json_data["board"], "current_player": json_data["current_player"]})

def check_game_over():
    pass

if __name__ == "__main__":
    app.run()