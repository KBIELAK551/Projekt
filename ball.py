from random import randint


window_width = 800
window_height = 800

sphere_radius = 20
ball_diameter = sphere_radius * 2


class Ball:
    def __init__(self, x, y, infected):
        self.x = x
        self.y = y
        self.infected = infected
        self.vx = randint(-10, 10)
        self.vy = randint(-10, 10)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x > window_width - sphere_radius or self.x < sphere_radius:
            self.vx = -self.vx
        if self.y > window_height - sphere_radius or self.y < sphere_radius:
            self.vy = - self.vy