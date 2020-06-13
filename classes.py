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
    def __init__(self, center=point(0, 0, 0), radius=1, material=None):
        self.id = id(self)
        self.center = center
        self.radius = radius
        self.transform = [[1, 0, 0, 0],
                           [0, 1, 0, 0],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]]
        self.material = material

class intersection:
    def __init__(self, t, obj):
        self.t = t
        self.obj = obj

class pointLight:
    def __init__(self, position=point(0, 0, 0), intensity=(1, 1, 1)):
        self.position = position
        self.intensity = intensity

class Material:
    def __init__(self, color=(1, 1, 1), ambient = 0.1, diffuse = 0.9, specular = 0.9, shininess = 150.0):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess
