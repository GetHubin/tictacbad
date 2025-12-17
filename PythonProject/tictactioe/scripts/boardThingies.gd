extends Area2D
#hi mom
signal tile_clicked(row, col)
@export var row: int= -1
@export var col: int= -1
#hi mom


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass

# When a tile is clicked, signal a tile is clicked with row and column data
func clicked(viewport: Node, event: InputEvent, shape_idx: int) -> void:
	if event is InputEventMouseButton and event.button_index == MOUSE_BUTTON_LEFT and event.pressed:
		emit_signal("tile_clicked", row, col)
