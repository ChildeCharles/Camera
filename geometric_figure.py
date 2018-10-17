from point import Point3D


# Simplification of creating a cuboid
class Edge:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point


class Cuboid:
    def __init__(self, start_point, width, height, depth):
        # from lower to upper plane, clockwise
        self.p0 = Point3D(start_point.x, start_point.y, start_point.z)
        self.p1 = Point3D(start_point.x, start_point.y, start_point.z + depth)
        self.p2 = Point3D(start_point.x + width, start_point.y, start_point.z + depth)
        self.p3 = Point3D(start_point.x + width, start_point.y, start_point.z)

        self.p4 = Point3D(start_point.x, start_point.y + height, start_point.z)
        self.p5 = Point3D(start_point.x, start_point.y + height, start_point.z + depth)
        self.p6 = Point3D(start_point.x + width, start_point.y + height, start_point.z + depth)
        self.p7 = Point3D(start_point.x + width, start_point.y + height, start_point.z)

        self.points = [self.p0, self.p1, self.p2, self.p3, self.p4, self.p5, self.p6, self.p7]
        self.edges = [
            Edge(self.p0, self.p1), Edge(self.p1, self.p2), Edge(self.p2, self.p3), Edge(self.p3, self.p0),  # down
            Edge(self.p0, self.p4), Edge(self.p1, self.p5), Edge(self.p2, self.p6), Edge(self.p3, self.p7),  # between
            Edge(self.p4, self.p5), Edge(self.p5, self.p6), Edge(self.p6, self.p7), Edge(self.p7, self.p4)]  # up

# Draws all edges of cuboid on a given screen if both starting points of that edge are visible to the camera
    def draw(self, scene):
        for edge in self.edges:
            if edge.start_point.z > 0 and edge.end_point.z > 0:
                start_point = edge.start_point.get_perspective_projected_point(scene)
                end_point = edge.end_point.get_perspective_projected_point(scene)
                scene.canvas.create_line(start_point.x, start_point.y,
                                         end_point.x, end_point.y,
                                         fill="blue")


