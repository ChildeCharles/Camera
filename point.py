import numpy
from math import sin, cos
from axis import Axis


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def transform(self, matrix):
        standardized_point = numpy.array([self.x, self.y, self.z, 1], dtype=float)
        result = numpy.matmul(matrix, standardized_point)
        self.x = result[0]
        self.y = result[1]
        self.z = result[2]

    def translate(self, distance, axis: Axis):
        if axis in Axis:
            matrix = numpy.array([
                                [1, 0, 0, 0],
                                [0, 1, 0, 0],
                                [0, 0, 1, 0],
                                [0, 0, 0, 1]
                                ], dtype=float)
            matrix[axis.value, 3] = distance
            self.transform(matrix)
        else:
            raise Exception('Couldn\'t find specified axis. "{axis}" is not defined in Axis class.'.format(axis=axis))

    def rotate(self, angle, axis: Axis):
        if axis is Axis.X:
            matrix = numpy.array([
                [1,          0,           0, 0],
                [0, cos(angle), -sin(angle), 0],
                [0, sin(angle),  cos(angle), 0],
                [0,          0,           0, 1]
                ], dtype=float)
        elif axis is Axis.Y:
            matrix = numpy.array([
                [cos(angle),  0, sin(angle), 0],
                [0,           1,          0, 0],
                [-sin(angle), 0, cos(angle), 0],
                [0,           0,          0, 1]
                ], dtype=float)
        elif axis is Axis.Z:
            matrix = numpy.array([
                [cos(angle), -sin(angle), 0, 0],
                [sin(angle),  cos(angle), 0, 0],
                [0,           0,          1, 0],
                [0,           0,          0, 1]
                ], dtype=float)
        else:
            raise Exception('Couldn\'t find specified axis. "{axis}" is not defined in Axis class.'.format(axis=axis))
        self.transform(matrix)

    def get_perspective_projected_point(self, scene):
        point_projected_x = scene.width / 2 + self.x * scene.d / self.z
        point_projected_y = scene.height / 2 + self.y * scene.d / self.z
        return Point2D(point_projected_x, point_projected_y)