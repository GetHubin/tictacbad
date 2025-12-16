import arcade
import arcade.gui
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

def snowman():
    arcade.draw_circle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT * 1 / 4, SCREEN_HEIGHT / 6, arcade.color.WHITE)
    arcade.draw_circle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 7, SCREEN_HEIGHT / 7, arcade.color.WHITE)
    arcade.draw_circle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 5, SCREEN_HEIGHT / 8, arcade.color.WHITE)
    arcade.draw_circle_filled(SCREEN_WIDTH / 2 + 20, SCREEN_HEIGHT * 3 / 5 + 15, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(SCREEN_WIDTH / 2 - 20, SCREEN_HEIGHT * 3 / 5 + 15, 5, arcade.color.BLACK)
    arcade.draw_triangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 5, SCREEN_WIDTH / 2 - 3,
                                SCREEN_HEIGHT * 3 / 5 - 12, SCREEN_WIDTH / 2 + 35, SCREEN_HEIGHT * 3 / 5 - 6,
                                arcade.color.ORANGE)

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Picture")
arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)
arcade.start_render()
snowman()


arcade.finish_render()
arcade.run()
