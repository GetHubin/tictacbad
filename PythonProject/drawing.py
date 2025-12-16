import arcade
from random import randrange
from typing import cast
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_BOTTOM = 0
SCREEN_LEFT = 0

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "learning python")
arcade.set_background_color(arcade.color.BLACK)
arcade.start_render()

#ground
arcade.draw_lrbt_rectangle_filled(SCREEN_LEFT, SCREEN_WIDTH, SCREEN_HEIGHT/2, SCREEN_HEIGHT, arcade.color.YELLOW_GREEN)


#dead sun
arcade.draw_circle_filled(50, SCREEN_BOTTOM+50,90, arcade.color.BRONZE)
arcade.draw_line(35, 150, 25, 200,arcade.color.BRONZE, 20)
arcade.draw_line(70, 150, 75, 200,arcade.color.BRONZE, 20)
arcade.draw_line(100, 140, 125, 180,arcade.color.BRONZE, 20)
arcade.draw_line(125, 115, 165, 150,arcade.color.BRONZE, 20)
arcade.draw_line(145, 80, 190, 110,arcade.color.BRONZE, 20)
arcade.draw_line(155, 50, 205, 55,arcade.color.BRONZE, 20)
arcade.draw_line(145, 20, 200, 10,arcade.color.BRONZE, 20)

#tree's
def drawtree(xpos, ypos):
    arcade.draw_lrbt_rectangle_filled(xpos, xpos+16, ypos, ypos+65, arcade.color.GOLD)
    arcade.draw_lrbt_rectangle_outline(xpos, xpos + 16, ypos, ypos + 65, arcade.color.BLACK)
    arcade.draw_circle_filled(xpos+8, ypos, 25, arcade.color.PINK_PEARL)
    arcade.draw_circle_outline(xpos + 8, ypos, 25, arcade.color.BLACK)

for i in range(25, SCREEN_WIDTH-25, 75):
    miny = int(SCREEN_HEIGHT / 2)
    drawtree(randrange(i-25, i+25), randrange(miny, SCREEN_HEIGHT-70))
'''
for i in range(10):
    miny = int(SCREEN_HEIGHT/2)
    drawtree(randrange(10,SCREEN_WIDTH-10), randrange(miny)+int(SCREEN_HEIGHT/2-70))
'''


#done
arcade.finish_render()
arcade.run()

