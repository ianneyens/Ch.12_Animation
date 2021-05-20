"""
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

"""
import arcade
SW = 700
SH = 700
suns = 1


class Sun:
    def __init__(self, x, y, dx, dy, rad, c):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.c = c

    def draw_sun(self):
        arcade.draw_circle_filled(self.x, self.y, self.rad, self.c)

    def update_sun(self):
        self.y += self.dy
        self.x += self.dx


class MyGame(arcade.Window):
    def __init__(self, SW, SH, title):
        super().__init__(SW, SH, title)
        arcade.set_background_color(arcade.color.SKY_BLUE)

        self.sun_list = []

        for i in range(suns):
            self.rad = 50
            self.dx = .5
            self.dy = .7
            self.x = 300
            self.y = 250
            self.c = arcade.color.SUNGLOW
            make_sun = Sun(self.x, self.y, self.dx, self.dy, self.rad, self.c)
            self.sun_list.append(make_sun)

    def on_draw(self):
        arcade.start_render()

        for sun in self.sun_list:
            sun.draw_sun()

        arcade.draw_rectangle_filled(250, 305, 500, 7, arcade.color.SADDLE_BROWN)
        arcade.draw_circle_filled(50, 450, 25, arcade.color.WHITE)  # Cloud 1
        arcade.draw_circle_filled(70, 460, 25, arcade.color.WHITE)
        arcade.draw_circle_filled(80, 450, 25, arcade.color.WHITE)
        arcade.draw_circle_filled(175, 470, 25, arcade.color.WHITE)  # Cloud 2
        arcade.draw_circle_filled(190, 450, 25, arcade.color.WHITE)
        arcade.draw_circle_filled(210, 470, 25, arcade.color.WHITE)
        arcade.draw_circle_filled(375, 400, 25, arcade.color.WHITE)  # Cloud 3
        arcade.draw_circle_filled(350, 420, 25, arcade.color.WHITE)
        arcade.draw_rectangle_filled(350, 150, 700, 300, arcade.color.GREEN)  # Grass
        arcade.draw_rectangle_filled(250, 250, 300, 200, arcade.color.WHITE)  # House
        arcade.draw_triangle_filled(250, 470, 50, 340, 450, 340, arcade.color.RED)  # Roof
        arcade.draw_rectangle_filled(250, 212, 65, 125, arcade.color.MIDNIGHT_BLUE)  # Door
        arcade.draw_circle_filled(230, 212, 5, arcade.color.SILVER_CHALICE)
        arcade.draw_rectangle_outline(160, 250, 50, 50, arcade.color.BLACK)  # Window
        arcade.draw_rectangle_filled(160, 250, 49, 49, arcade.color.LIGHT_CYAN)
        arcade.draw_line(135, 250, 185, 250, arcade.color.BLACK)
        arcade.draw_line(160, 275, 160, 225, arcade.color.BLACK)
        arcade.draw_rectangle_outline(340, 250, 50, 50, arcade.color.BLACK)  # Window
        arcade.draw_rectangle_filled(340, 250, 49, 49, arcade.color.LIGHT_CYAN)
        arcade.draw_line(315, 250, 365, 250, arcade.color.BLACK)
        arcade.draw_line(340, 275, 340, 225, arcade.color.BLACK)
        arcade.draw_rectangle_filled(250, 50, 80, 200, arcade.color.GRAY)  # Path
        for fence in range(4, 500, 12):  # Fence
            arcade.draw_rectangle_filled(fence, 50, 10, 100, arcade.color.SADDLE_BROWN)
        arcade.draw_rectangle_filled(499, 150, 5, 315, arcade.color.SADDLE_BROWN)
        arcade.draw_rectangle_filled(250, 75, 500, 10, arcade.color.SADDLE_BROWN)
        arcade.draw_rectangle_filled(250, 25, 500, 10, arcade.color.SADDLE_BROWN)

    def on_update(self, delta_time: float):
        for sun in self.sun_list:
            sun.update_sun()


def main():
    window = MyGame(SW, SH, "Animation")
    arcade.run()


if __name__ == '__main__':
    main()
