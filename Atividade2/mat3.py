class Mat3:
    def __init__(self, a, b, c, d, e, f, g, h, i):
        self.elements = [[a, b, c], [d, e, f], [g, h, i]]

    def __add__(self, other):
        result = Mat3(0, 0, 0, 0, 0, 0, 0, 0, 0)
        for i in range(3):
            for j in range(3):
                result.elements[i][j] = self.elements[i][j] + other.elements[i][j]
        return result

    def __sub__(self, other):
        result = Mat3(0, 0, 0, 0, 0, 0, 0, 0, 0)
        for i in range(3):
            for j in range(3):
                result.elements[i][j] = self.elements[i][j] - other.elements[i][j]
        return result

    def __mul__(self, scalar):
        result = Mat3(0, 0, 0, 0, 0, 0, 0, 0, 0)
        for i in range(3):
            for j in range(3):
                result.elements[i][j] = self.elements[i][j] * scalar
        return result
