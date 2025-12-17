extends Node2D
 #hi mom

@export var x_texture: Texture2D
@export var o_texture: Texture2D
@export var empty_texture: Texture2D

var sprites := {} # "0,0" -> Sprite2D

# Called when the node enters the scene tree for the first time.
# Initializes signal connections from ApiClient, sprites Dictionary mapping
# of tic tac toe coordinates to tile sprites, and the board. Also connects
# Tile clicks with tile_clicked function.
func _ready() -> void:
	# When ApiClient signals the board info is updated, update board visually.
	ApiClient.board_updated.connect(update_board)
	# Find tile sprites, put them correctly into sprites Dictionary.
	for child in get_children():
		if child is Sprite2D and child.name.begins_with("S_"):
			var parts = child.name.split("_")
			var key = parts[1] + "," + parts[2]
			sprites[key] = child
	# Ensure board initialization.
	ApiClient.makeBoard()
	# Find click-detecting tile objects and connect when they clicked
	# with tile_pressed function.
	for tile in get_children():
		if tile.has_signal("tile_clicked"):
			tile.tile_clicked.connect(tile_pressed)


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass

# 
func tile_pressed(row, col):
	ApiClient.makeMove(row, col);
	
func update_board(board_dict: Dictionary):
	for key in board_dict:
		var sprite = sprites.get(key)
		match board_dict[key]:
			"X":
				sprite.texture = x_texture
			"O":
				sprite.texture = o_texture
			"Empty":
				sprite.texture = empty_texture
		
		
		
