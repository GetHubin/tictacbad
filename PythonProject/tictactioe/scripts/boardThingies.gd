extends Area2D

# Signals for a boardThingy/tile
signal tile_clicked(row, col)

# row and column data specific to each tile
@export var row: int= -1
@export var col: int= -1



# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass

# When a tile is clicked, signal a tile is clicked with row and column data
func clicked(viewport: Node, event: InputEvent, shape_idx: int) -> void:
	if event is InputEventMouseButton and event.button_index == MOUSE_BUTTON_LEFT and event.pressed:
		emit_signal("tile_clicked", row, col)
