import arcade
SW = 750
SH = 500


class Ball:
    def __init__(self, x, y, dx, dy, r, c):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.r = r
        self.c = c

    def draw_ball(self):
        arcade.draw_circle_filled(self.x, self.y, self.r, self.c)

    def update_ball(self):
        self.x += self.dx
        self.y += self.dy

        if self.x <= self.r or self.x >= SW - self.r:
            self.dx *= -1
        if self.y <= self.r or self.y >= SH - self.r:
            self.dy *= -1


class Mygame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.RED_DEVIL)
        self.ball = Ball(375, 250, 3, -5, 25, arcade.color.VIVID_SKY_BLUE)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw_ball()

    def on_update(self, delta_time: float):
        self.ball.update_ball()


def main():
    window = Mygame(SW, SH, "My game")
    arcade.run()


if __name__ == '__main__':
    main()
