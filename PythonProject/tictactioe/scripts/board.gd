extends Node2D

# Textures for when a tile is an X, O, or empty
@export var x_texture: Texture2D
@export var o_texture: Texture2D
@export var empty_texture: Texture2D

# Dictionary to map tic tac toe coordinates to Sprites
var sprites := {} # "0,0" -> Sprite2D
@onready var play_again_button = $PlayAgainButton
@onready var play_again_button_pos = $PlayAgainButton.position
@onready var turn_sprite = $TurnSprite
@onready var turn_text = $TurnText
@onready var winner_sprite = $WinnerSprite
@onready var winner_text = $WinText
@onready var tie_text = $TieText

# Called when the node enters the scene tree for the first time.
# Initializes signal connections from ApiClient, sprites Dictionary mapping
# of tic tac toe coordinates to tile sprites, and the board. Also connects
# Tile clicks with tile_clicked function.
func _ready() -> void:
	play_again_button.visible = false
	# When ApiClient signals the board info is updated, update board visually.
	ApiClient.board_updated.connect(update_board)
	ApiClient.game_over.connect(game_over_scene)
	# Find tile sprites, put them correctly into sprites Dictionary.
	for child in get_children():
		if child is Sprite2D and child.name.begins_with("S_"):
			var parts = child.name.split("_")
			var key = parts[1] + "," + parts[2]
			sprites[key] = child
	# Ensure board initialization.
	ApiClient.makeBoard()
	# Find click-detecting tile objects and connect when they are clicked
	# with tile_pressed function.
	for tile in get_children():
		if tile.has_signal("tile_clicked"):
			tile.tile_clicked.connect(tile_pressed)

# Tells ApiClient to send a makeMove request with information about what tile 
# was pressed.
func tile_pressed(row, col):
	ApiClient.makeMove(row, col);

# Looks through board_dict, a mapping of tic tac toe corrdinates to which player
# is there (or Empty if it's empty there), updates each texture to the correct
# one based on its linear traversal.
func update_board(board_dict: Dictionary, current_player: String):
	for key in board_dict:
		# Same as sprite = sprites[key] except that if the key doesn't exist 
		# in sprites it becomes null instead of throwing an error 
		var sprite = sprites.get(key)
		# Godot equivalent of a switch statement, assigns correct texture based
		# on contents of board_dict[key]
		match board_dict[key]:
			"X":
				sprite.texture = x_texture
			"O":
				sprite.texture = o_texture
			"Empty":
				sprite.texture = empty_texture
	update_turn(current_player)

func update_turn(current_player: String):
	match current_player:
		"X":
			turn_sprite.texture = x_texture
		"O":
			turn_sprite.texture = o_texture

func game_over_scene(winner: String):
	turn_text.text = ""
	turn_sprite.texture = empty_texture
	play_again_button.visible = true
	if winner == "X":
		winner_sprite.texture = x_texture
		winner_text.text = "wins!"
	if winner == "O":
		winner_sprite.texture = o_texture
		winner_text.text = "wins!"
	if winner == "none":
		tie_text.text = "It's a tie!"
	for tile in get_children():
		if tile.has_signal("tile_clicked"):
			tile.tile_clicked.disconnect(tile_pressed)


func _on_exit_button_pressed() -> void:
	get_tree().quit()


func _on_play_again_button_pressed() -> void:
	winner_sprite.texture = empty_texture
	turn_text.text = "Turn:"
	winner_text.text = ""
	tie_text.text = ""
	ApiClient.makeBoard()
	# Find click-detecting tile objects and connect when they are clicked
	# with tile_pressed function.
	for tile in get_children():
		if tile.has_signal("tile_clicked"):
			tile.tile_clicked.connect(tile_pressed)
	play_again_button.visible = false
