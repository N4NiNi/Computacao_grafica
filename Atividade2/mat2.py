class Mat2:
    def __init__(self, a, b, c, d):
        self.elements = [[a, b], [c, d]]

    def __add__(self, other):
        result = Mat2(0, 0, 0, 0)
        for i in range(2):
            for j in range(2):
                result.elements[i][j] = self.elements[i][j] + other.elements[i][j]
        return result

    def __sub__(self, other):
        result = Mat2(0, 0, 0, 0)
        for i in range(2):
            for j in range(2):
                result.elements[i][j] = self.elements[i][j] - other.elements[i][j]
        return result

    def __mul__(self, scalar):
        result = Mat2(0, 0, 0, 0)
        for i in range(2):
            for j in range(2):
                result.elements[i][j] = self.elements[i][j] * scalar
        return result