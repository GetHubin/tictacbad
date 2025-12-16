import arcade
from os import path

from arcade.examples.astar_pathfinding import SPRITE_SCALING
from arcade.examples.perf_test.stress_test_collision_arcade import SPRITE_SCALING_PLAYER

DIR = path.dirname(path.abspath(__file__))

SPRITE_SCALING_PEEPS = .75
SPRITE_SCALING_LASER = .75

P1_MAX_HEALTH = 300
P2_MAX_HEALTH = 300

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Shooter"

PLAYER_SPEED = 5
LASER_SPEED = 10

winner = None

class MyGame(arcade.Window):

    def __init__(self):
        """ Initializer """
        #call parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # variables hold sprite list
        self.player1_list = None
        self.player2_list = None
        self.laser1_list = None
        self.laser2_list = None
        self.wall_list = None

        # set player info
        self.player1_sprite = None
        self.player2_sprite = None

        self.p1_health = None
        self.p2_health = None

        #background
        self.background = None

        #done show mouse
        self.set_mouse_visible(False)

    def setup(self):
        """ Set up the game and initialize the variables """

        self.background = arcade.load_texture(f"{DIR}\\assets\\main_screen.png")

        #sprite list
        self.player1_list = arcade.SpriteList()
        self.player2_list = arcade.SpriteList()
        self.laser1_list = arcade.SpriteList()
        self.laser2_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        #set up players
        self.p1_health = P1_MAX_HEALTH
        self.p2_health = P2_MAX_HEALTH

        #sprite images
        self.player1_sprite = arcade.Sprite(f"{DIR}\\assets\\purpleship.png", SPRITE_SCALING_PLAYER)
        self.player1_sprite.center_x = SCREEN_WIDTH / 2
        self.player1_sprite.center_y = 35
        self.player1_list.append(self.player1_sprite)

        self.player2_sprite = arcade.Sprite(f"{DIR}\\assets\\greenship.png", SPRITE_SCALING_PLAYER)
        self.player2_sprite.center_x = SCREEN_WIDTH / 2
        self.player2_sprite.center_y = SCREEN_HEIGHT-35
        self.player2_list.append(self.player2_sprite)

        #set color
        arcade.set_background_color(arcade.color.BLACK)

        #physics ewww
        self.physics_engine1 = arcade.PhysicsEngineSimple(self.player1_sprite, self.wall_list)
        self.physics_engine2 = arcade.PhysicsEngineSimple(self.player2_sprite, self.wall_list)

    def on_draw(self):
        """render the screen"""

        self.clear()  # Clear the screen at the start of the draw

        if self.background:
            arcade.draw_texture_rect(
                texture=self.background,
                center_x=SCREEN_WIDTH / 2,
                center_y=SCREEN_HEIGHT / 2,
                width=SCREEN_WIDTH,
                height=SCREEN_HEIGHT
            )

        # Draw all sprite lists
        self.player1_list.draw()
        self.player2_list.draw()
        self.laser1_list.draw()
        self.laser2_list.draw()

        #draw back image
        #arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)


    def on_key_press(self):
        """handle key presses"""
        pass
    def on_key_release(self):
        """handle key releases"""
        pass

#    def update(self):
#        """handle key presses"""

def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()


