extends Node2D
 #hi mom

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	ApiClient.makeBoard()
	for tile in get_children():
		if tile.has_signal("tile_clicked"):
			tile.tile_clicked.connect(tile_pressed)


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass

func tile_pressed(row, col):
	print("hi mom")
	print(row, " ", col)
	ApiClient.makeMove(row, col);
