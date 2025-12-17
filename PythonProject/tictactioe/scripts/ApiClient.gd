extends Node

# Signals for when a response is received
signal board_updated(board_data: Dictionary)
signal request_failed(error: String)

@onready var http_request = HTTPRequest.new()
@onready var baseURL = "http://127.0.0.1:5000/"

# Called when the node enters the scene tree for the first time.
func _ready():
	# http request initialization
	add_child(http_request)
	http_request.connect("request_completed", self.finished_thing)

# Called when a request is completed, signals information obtained
# from request (or whatever error occurred)
func finished_thing(result, response_code, headers, body):
	# Check for error code
	if response_code != 200:
		emit_signal("request_failed", "HTTP %d" % response_code)
		return
	# Retrieve JSON data
	var string_body = body.get_string_from_utf8()
	var json = JSON.parse_string(string_body)
	# Check JSON data for contents
	if json == null:
		emit_signal("request_failed", "Invalid JSON")
		return
	# If json data pertains to board, signal board update
	if json.has("board"):
		emit_signal("board_updated", json["board"])

# This uses a POST request method that doesn't require/use any JSON information from the request.
# It will copy tictactoestart.json to tictactoe.json, so the game is ready to begin.
func makeBoard():
	# Initialize args for request
	var url = baseURL+"makeBoard/"
	var jsonRC = {}
	var json_string = JSON.stringify(jsonRC)
	var headers = ["Content-Type: application/json"]
	# Make request
	http_request.request(url, headers, HTTPClient.METHOD_POST, json_string)

# This uses a POST request method that requires the following JSON infomation to be passed to it:
# "row": the row a move has been made at
# "col": the column a move has been made at
# It will place an X or O on a tile depending on whose turn it is.
func makeMove(row, col):
	# Initialize args for request
	var url = baseURL+"makeMove/"
	var jsonRC = { "row": row, "col": col}
	var json_string = JSON.stringify(jsonRC)
	var headers = ["Content-Type: application/json"]
	# Make request
	http_request.request(url, headers, HTTPClient.METHOD_POST, json_string)
