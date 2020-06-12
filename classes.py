objects_id = 0
class point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.w = 1.0

class vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.w = 0.0

class ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

class Sphere:
    def __init__(self, center=point(0, 0, 0), radius=1):
        self.id = id(self)
        self.center = center
        self.radius = radius
        self.transform = [[1, 0, 0, 0],
                           [0, 1, 0, 0],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]]
class intersection:
    def __init__(self, t, obj):
        self.t = t
        self.obj = obj
