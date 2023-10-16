
class Mat4:
    def __init__(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p):
        self.elements = [[a, b, c, d], [e, f, g, h], [i, j, k, l], [m, n, o, p]]

    def __add__(self, other):
        result = Mat4(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        for i in range(4):
            for j in range(4):
                result.elements[i][j] = self.elements[i][j] + other.elements[i][j]
        return result

    def __sub__(self, other):
        result = Mat4(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        for i in range(4):
            for j in range(4):
                result.elements[i][j] = self.elements[i][j] - other.elements[i][j]
        return result

    def __mul__(self, scalar):
        result = Mat4(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        for i in range(4):
            for j in range(4):
                result.elements[i][j] = self.elements[i][j] * scalar
        return result