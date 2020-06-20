import arcade
screen_width = 600
screen_height = 600


arcade.open_window(screen_width, screen_height, "Drawing Example")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

# drawing face

# Drawing circle
x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x, y, radius, arcade.color.BANANA_YELLOW)

# Drawing Right Eye
x = 375
y = 375
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Drawing Left Eye
x = 225
y = 375
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

x = 100
y = 100
arcade.draw_arc_outline()


arcade.finish_render()
arcade.run()
