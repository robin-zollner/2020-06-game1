import arcade
screen_width = 600
screen_height = 600
window_name = "Smiley Face"




def drawSmileyFace(locX, locY, radius):
    x = locX
    y = locY
    radius = radius
    arcade.draw_circle_filled(x, y, radius, arcade.color.BANANA_YELLOW)

    # Drawing Right Eye
    x = locX + 75
    y = locY + 75
    radius = 20
    arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Drawing Left Eye
    x = locX - 75
    y = locY + 75
    radius = 20
    arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

    # Creating Smile
    x = locX
    y = locY - 30
    width = 250
    height = 200
    start_angle = 180
    end_angle = 360
    border_width = 10
    arcade.draw_arc_outline(x,y,width, height,arcade.color.BLACK_BEAN, start_angle, end_angle, border_width)


def main():
    arcade.open_window(screen_width, screen_height, window_name)
    arcade.set_background_color(arcade.color.WHITE)

    arcade.start_render()
    drawSmileyFace(300, 300, 200)
    arcade.finish_render()
    arcade.run()

if __name__ == '__main__':
    main()