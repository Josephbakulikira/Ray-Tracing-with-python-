from constants import *
from classes import point, vector3

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

def MultiplyMatrix(a, b):
    columns_a = len(a[0])
    rows_a = len(a)
    columns_b = len(b[0])
    rows_b = len(b)
    result = [[i for i in range(columns_b)] for j in range(rows_a)]
    for x in range(rows_a):
        for y in range(columns_b):
            sum = 0
            for k in range(columns_b):
                sum += a[x][k] * b[k][y]
            result[x][y] = sum

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

A = [[3, -9, 7, 3], [3, -8, 2, -9], [-4, 4, 4, 1], [-6, 5, -1, 1]]
B = [[8, 2, 2, 2], [3, -1, 7, 0], [7, 0, 5, 4], [6, -2, 0, 5]]

C = MultiplyMatrix(A, B)
D = InverseMatrix(B)
print(InverseMatrix(identity_matrix))
