import turtle
import numpy as np
import random
import pyscreenshot


class DrawFern:
    def __init__(self, show_points=False, color='black', speed=2, loop_over=10000):
        self.stem = np.array([[0, 0], [0, 0.16]])
        self.stem_c = np.array([[0], [0]])
        self.smaller_leaflets = np.array([[0.85, 0.04], [-0.04, 0.85]])
        self.smaller_leaflets_c = np.array([[0], [1.60]])
        self.left_large_leaflets = np.array([[0.20, -0.26], [0.23, 0.22]])
        self.left_leaflets_c = np.array([[0], [1.6]])
        self.right_large_leaflets = np.array([[-0.15, 0.28], [0.26, 0.24]])
        self.right_large_leaf_c = np.array([[0], [0.44]])
        self.show_points = show_points
        self.loop_over = loop_over
        self.pen = turtle.Turtle()
        self.pen.color(color)
        self.pen.speed(speed)
        self.pen.penup()
        self.x_y = np.array([[0], [0]])

    def generate_points(self, matrix, coefficient):
        self.x_y = np.add(np.dot(matrix, self.x_y), coefficient)
        if self.show_points:
            print(f'Drawing Point At: {self.x_y}')

    def plot_point(self):
        self.pen.goto(65 * self.x_y[0][0], 37 * self.x_y[1][0] - 252)
        self.pen.pendown()
        self.pen.dot()
        self.pen.penup()

    def start(self):
        for _ in range(self.loop_over):
            self.plot_point()
            if (_ % 1000) == 0:
                image = pyscreenshot.grab()
                image.save(f'iteration{_}.png')
            random_number = random.random() * 100
            if random_number < 1:
                self.generate_points(self.stem, self.stem_c)
            elif random_number < 86:
                self.generate_points(self.smaller_leaflets, self.smaller_leaflets_c)
            elif random_number < 93:
                self.generate_points(self.left_large_leaflets, self.left_leaflets_c)
            else:
                self.generate_points(self.right_large_leaflets, self.right_large_leaf_c)


if __name__ == '__main__':
    draw = DrawFern(show_points=False, speed=1000000)
    draw.start()
