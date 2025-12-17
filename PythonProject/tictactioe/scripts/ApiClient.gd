extends Node

signal board_updated(board_data: Dictionary)
signal request_failed(error: String)

@onready var http_request = HTTPRequest.new()
@onready var baseURL = "http://127.0.0.1:5000/"

func _ready():
	add_child(http_request)
	http_request.connect("request_completed", self.finished_thing)
	
func finished_thing(result, response_code, headers, body):
	if response_code != 200:
		emit_signal("request_failed", "HTTP %d" % response_code)
		return
		
	var string_body = body.get_string_from_utf8()
	var json = JSON.parse_string(string_body)
	if json == null:
		emit_signal("request_failed", "Invalid JSON")
		return
	
	if json.has("board"):
		emit_signal("board_updated", json["board"])

func makeBoard():
	var url = baseURL+"makeBoard/"
	var jsonRC = {}
	var json_string = JSON.stringify(jsonRC)
	var headers = ["Content-Type: application/json"]
	http_request.request(url, headers, HTTPClient.METHOD_POST, json_string)

func makeMove(row, col):
	var url = baseURL+"makeMove/"
	var jsonRC = { "row": row, "col": col}
	var json_string = JSON.stringify(jsonRC)
	var headers = ["Content-Type: application/json"]
	var err = http_request.request(url, headers, HTTPClient.METHOD_POST, json_string)
	if err != OK:
		print("httprequest failed to start ",err)
