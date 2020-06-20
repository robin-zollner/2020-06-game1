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

# Creating Smile
x = 300
y = 270
width = 250
height = 200
start_angle = 180
end_angle = 360
border_width = 10
arcade.draw_arc_outline(x,y,width, height,arcade.color.BLACK_BEAN, start_angle, end_angle, border_width)


arcade.finish_render()
arcade.run()
