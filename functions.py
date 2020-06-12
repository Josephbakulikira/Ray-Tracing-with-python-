from constants import *
from classes import *
from math import cos, sin, pi, pow, sqrt
from random import randint
from decimal import Decimal
object_id = 0

# -------------------------VECTORS AND POINTS FUNCTIONS------------------------------------------------------------------

def Compare(a, b):
    if abs(a-b) < EPSILON:
        return True
    else:
        return False

def AddingTuples(a, b):
    x = a.x + b.x
    y = a.y + b.y
    z = a.z + b.z
    w = a.w + b.w
    if w == 0:
        return vector3(x, y, z)
    else:
        return point(x, y, z)

def SubtractingTuples(a, b):
    x = a.x - b.x
    y = a.y - b.y
    z = a.z - b.z
    w = a.w - b.w
    if w == 0:
        return vector3(x, y, z)
    else:
        return point(x, y, z)

def NegatingTuples(a):
    a.x = a.x * -1
    a.y = a.y * -1
    a.z = a.z * -1
    a.w = a.w * -1
    return a

def TuplePowers(v, power):
    x = pow(v.x,power)
    y = pow(v.y,power)
    z = pow(v.z,power)
    if v.w == 1:
        return point(x, y, z)
    else:
        return vector3(x, y, z)

def TupleSqrt(v):
    x = sqrt(v.x)
    y = sqrt(v.y)
    z = sqrt(v.z)
    if v.w == 1:
        return point(x, y, z)
    else:
        return vector3(x, y, z)

def MultiplyTuple(a, scalar):
    a.x = a.x * scalar
    a.y = a.y * scalar
    a.z = a.z * scalar
    a.w = a.w * scalar
    return a

def DivideTuple(a, scalar):
    a.x = a.x / scalar
    a.y = a.y / scalar
    a.z = a.z / scalar
    a.w = a.w / scalar
    return a

def GetMagnitude(vector):
    return (vector.x**2 + vector.y**2+vector.z**2)** 0.5

def NormalizeVector(vector):
    magnitude = (vector.x**2 + vector.y**2+vector.z**2)** 0.5
    vector.x = vector.x/magnitude
    vector.y = vector.y/magnitude
    vector.z = vector.z/magnitude
    return vector

def DotProduct(v1, v2):
    return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z + v1.w * v2.w

def CrossProduct(v1, v2):
    return vector3(v1.y*v2.z-v1.z * v2.y, v1.z * v2.x - v1.x * v2.z, v1.x * v2.y - v1.y * v2.x)


# -------------------------COLORS FUNCTIONS------------------------------------------------------------------

def AddColors(a, b):
    return (a[0]+b[0], a[1]+b[1], a[2]+b[2])

def SubtractingColors(a, b):
    return (a[0]-b[0], a[1]-b[1], a[2]-b[2])

def MultiplyColor(a, p):
    return (a[0]*p, a[1]*p, a[2]*p)

def HadamartProduct(a, b):
    return (a[0]*b[0], a[1]*b[1], a[2]*b[2])

#----------------------------------MATRICES------------------------------------------------------------------
def PointToMatrix1(a):
    return [[a.x, a.y, a.z, a.w]]
def PointToMatrix2(a):
    return [[a.x], [a.y], [a.z], [a.w]]

def VectorToMatrix1(a):
    return [[a.x, a.y, a.z, a.w]]
def VectorToMatrix2(a):
    b = [[a.x],
        [a.y],
        [a.z],
        [a.w]]
    return  b

def MatrixToVector1(a):
    return vector3(a[0][1], a[0][2], a[0][3])
def MatrixToVector2(a):
    return vector3(a[0][0], a[1][0], a[2][0])

def MatrixToPoint1(a):
    return point(a[0][1], a[0][2], a[0][3])
def MatrixToPoint2(a):
    return point(a[0][0], a[1][0], a[2][0])

def MultiplyMatrix(a, b):
    check = 2
    if isinstance(a, point):
        a = PointToMatrix1(a)
        check = 1
    elif isinstance(a, vector3):
        check = 0
        a = VectorToMatrix1(a)
    if isinstance(b, point):
        check=3
        b = PointToMatrix2(b)
    elif isinstance(b, vector3):
        check = 4
        b = VectorToMatrix2(b)
    columns_a = len(a[0])
    rows_a = len(a)
    columns_b = len(b[0])
    rows_b = len(b)
    result = [[i for i in range(columns_b)] for j in range(rows_a)]
    if columns_a != rows_b:
        print("Error! the number of columns of the first matrix must be equal to the number of rows of the second!")
        return None
    for x in range(rows_a):
        for y in range(columns_b):
            sum = 0
            for k in range(columns_a):
                sum += a[x][k] * b[k][y]
            result[x][y] = sum
    if check == 1:
        return MatrixToPoint1(result)
    elif check == 0:
        return MatrixToVector1(result)
    elif check == 3:
        return MatrixToPoint2(result)
    elif check == 4:
        return MatrixToVector2(result)
    return result

def TransposeMatrix(M):
    cols =len(M[0])
    rows = len(M)
    result = [[i for i in range(cols)] for j in range(rows)]
    for x in range(rows):
        for y in range(cols):
            result[x][y] = M[y][x]
    return result

def SubMatrix(M, row, col):
    _row = (len(M))
    _col = (len(M[0]))
    rows = _row-1
    cols = _col-1
    result = [[i for i in range(cols)] for j in range(rows)]

    for x in range(_row):
        for y in range(_col):
            if x != row and y != col:
                a,b = x, y
                if x > row:
                    a = x-1
                if y > col:
                    b = y-1
                result[a][b] = M[x][y]
    return result

def Minor(M, row, col):
    sub = SubMatrix(M, row, col)
    return sub[0][0] * sub[1][1] - sub[0][1] * sub[1][0]

def Cofactor(M, row, col):
    minor = Minor(M, row, col)
    e = row + col
    if (e % 2) == 0:
        return minor
    else:
        return -minor

def Determinant(M):
    det = 0
    v = []

    if len(M) == 2 and len(M[0] == 2):
        return M[0][0] * M[1][1] - M[0][1]*M[1][0]
    else:
        for i in range(len(M[0])):
            a = SubMatrix(M, 0, i)
            value = 0
            for j in range(len(a[0])):
                b = Cofactor(a, 0, j)
                value += a[0][j] * b
            if (0 + i) % 2 == 0:
                det += value * M[0][i]
            else:
                det -= value * M[0][i]

    return det


def InverseMatrix(M):
    det = Determinant(M)
    if det == 0:
        return M
    else:
        matrix = [[i for i in range(4)] for j in range(4)]
        for x in range(4):# 4 is the number of rows
            for y in range(4):# 4 is the number of columns_a
                a = SubMatrix(M, x, y)
                value = 0
                for j in range(3):
                    value+= Cofactor(a, 0, j) * a[0][j]
                if (x+y)%2 == 0:
                    matrix[x][y] = value
                else:
                    matrix[x][y] = -value
        matrix = TransposeMatrix(matrix)
        for x in range(4):
            for y in range(4):
                matrix[x][y] = matrix[x][y]/det

        return matrix

def InverseTransform(t):
    return transform(-t.x, -t.y, -t.z)

def TranslationMatrix(x, y, z):
    return [[1, 0 ,0, x],
            [0, 1, 0, y],
            [0, 0, 1, z],
            [0, 0, 0, 1]]

def ScalingMatrix(x, y, z):
    return [[x, 0 ,0, 0],
            [0, y, 0, 0],
            [0, 0, z, 0],
            [0, 0, 0, 1]]

def DegreeToRadian(deg):
    return (deg * PI) /180

def XRotationMatrix(rad):
    return [[1, 0, 0, 0],
            [0, cos(rad), -sin(rad), 0],
            [0, sin(rad), cos(rad), 0],
            [0, 0, 0, 1]]
def YRotationMatrix(rad):
    return [[cos(rad), 0, sin(rad), 0],
            [0, 1, 0, 0],
            [-sin(rad), 0, cos(rad), 0],
            [0, 0, 0, 1]]
def ZRotationMatrix(rad):
    return [[cos(rad), -sin(rad), 0, 0],
            [sin(rad), cos(rad), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]]

def ShearingMatrix(xy, xz, yx, yz, zx, zy):
    return [[1, xy, xz, 0],
            [yx, 1, yz, 0],
            [zx, zy, 1, 0],
            [0, 0, 0, 1]]

#-----------------------------Ray----------------------------
def hit(i):
    try:
        m = min(v.t for v in i if v.t > 0 )
        return m
    except :
        return None

def transform(r, m):
    origin = MultiplyMatrix(m, r.origin)
    dir = MultiplyMatrix(m, r.direction)
    return ray(origin, dir)

def set_transform(s, t):
    s.transform = t

def position(r, t):
    return AddingTuples(r.origin, MultiplyTuple(r.direction, t))

def Intersections(*args):
    return [*args]

def Intersect(s, r):
    r = transform(r, InverseMatrix(s.transform))

    L = SubtractingTuples(r.origin, s.center )
    a = DotProduct(r.direction, r.direction)
    b = 2 * DotProduct(r.direction, L)
    c = DotProduct(L, L)-1.0
    discriminant = (b ** 2)-(4 * a * c)

    if discriminant < 0:
        return []
    else:
        t1 = float((-b - sqrt(discriminant))/(2*a))
        t2 = float((-b + sqrt(discriminant))/(2*a))
        i1 = intersection(t1, s)
        i2 = intersection(t2, s)
        p = Intersections(i1, i2)
        return p



# r = ray(point(0, 0, -5), vector3(0, 0, 1))
# m = ScalingMatrix(2, 2, 2)
# s = Sphere(point(0, 0, 0), 1)
# set_transform(s, m)
# xs = Intersect(s, r)
# print(len(xs))
# print(xs[0].t)
# print(xs[1].t)

# r2 = transform(r, m)
#
# t = TranslationMatrix(2, 3, 4)
#
#
# print("-----origin-----")
# print("{}, {}, {} ".format(r2.origin.x, r2.origin.y, r2.origin.z))
# print("---direction---")
# print("{}, {}, {} ".format(r2.direction.x, r2.direction.y, r2.direction.z))
# print(s.transform)
# # print("{}, {}, {}, {}".format(xs.x, xs.y, xs.z, xs.w))
