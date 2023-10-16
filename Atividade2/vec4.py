class Vec4:
    def __init__(self, x, y, z, a):
        self.x = x
        self.y = y
        self.z = z
        self.a = a

    def __add__(self, other):
        return Vec4(self.x + other.x, self.y + other.y, self.z + other.z, self.a + other.a)

    def __sub__(self, other):
        return Vec4(self.x - other.x, self.y - other.y, self.z - other.z, self.a - other.a)

    def __mul__(self, scalar):
        return Vec4(self.x * scalar, self.y * scalar, self.z * scalar, self.a * scalar)

    def __truediv__(self, scalar):
        return Vec4(self.x / scalar, self.y / scalar, self.z / scalar, self.a / scalar)

    def __neg__(self):
        return Vec4(-self.x, -self.y, -self.z, -self.a)