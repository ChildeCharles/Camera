import tkinter as tk
import geometric_figure as figure
from axis import Axis
import constant

class Scene(object):
    def __init__(self, master, width=800, height=800, background_color="black"):
        self.width = width
        self.height = height
        self.background_color = background_color
        self.canvas = tk.Canvas(master, width=self.width, height=self.height, background=self.background_color)
        self.canvas.pack()

        self.move_step = float(constant.MOVE_STEP)
        self.zoom_step = float(constant.ZOOM_STEP)
        self.rotate_step = float(constant.ROTATE_STEP)
        self.d = 200  # Distance from viewport

        self.figures = []
        self.initialize_figures()
        self.draw()

    def initialize_figures(self):
        self.figures.append(figure.Cuboid(figure.Point3D(-6, 0, 5), 3, 3, 3))
        self.figures.append(figure.Cuboid(figure.Point3D(-6, -10, 15), 5, 5, 5))
        self.figures.append(figure.Cuboid(figure.Point3D(6, 0, 5), 3, 3, 3))
        self.figures.append(figure.Cuboid(figure.Point3D(6, -10, 15), 5, 5, 5))

    def draw(self):
        self.canvas.delete(tk.ALL)
        for shape in self.figures:
            shape.draw(self)

    def move_handler(self, event):
        source = event.keysym
        if source == "w":
            self.move(self.move_step, Axis.Y)
        elif source == "s":
            self.move(-self.move_step, Axis.Y)
        elif source == "a":
            self.move(self.move_step, Axis.X)
        elif source == "d":
            self.move(-self.move_step, Axis.X)
        elif source == "Up":
            self.move(-self.move_step, Axis.Z)
        elif source == "Down":
            self.move(self.move_step, Axis.Z)
        else:
            print('"{0}" pressed but it isn\'t bound to anything'.format(source))
        self.draw()

    def move(self, distance, axis):
        for shape in self.figures:
            for point in shape.points:
                point.translate(distance, axis)

    def rotate_handler(self, event):
        source = event.keysym
        if source == "w":
            self.rotate(self.rotate_step, Axis.X)
        elif source == "s":
            self.rotate(-self.rotate_step, Axis.X)
        elif source == "a":
            self.rotate(-self.rotate_step, Axis.Y)
        elif source == "d":
            self.rotate(self.rotate_step, Axis.Y)
        elif source == "Up":
            self.rotate(-self.rotate_step, Axis.Z)
        elif source == "Down":
            self.rotate(self.rotate_step, Axis.Z)
        else:
            print('"Ctrl + {0}" pressed but it isn\'t bound to anything'.format(source))
        self.draw()

    def rotate(self, angle, axis):
        for shape in self.figures:
            for point in shape.points:
                point.rotate(angle, axis)

    def zoom_handler(self, event):
        source = event.keysym
        if source == "plus" or source == "KP_Add":
            self.d += self.zoom_step
        elif source == "minus" or source == "KP_Subtract":
            self.d -= self.zoom_step
        else:
            print('"{0}" pressed but it isn\'t bound to anything'.format(source))
        self.draw()

