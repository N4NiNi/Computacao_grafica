from Atividade2.mat4 import Mat4

def test_mat4_addition():
    m1 = Mat4(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
    m2 = Mat4(16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
    result = m1 + m2
    assert result.elements == [[17, 17, 17, 17], [17, 17, 17, 17], [17, 17, 17, 17], [17, 17, 17, 17]]

def test_mat4_subtraction():
    m1 = Mat4(10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)
    m2 = Mat4(3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3)
    result = m1 - m2
    assert result.elements == [[7, 7, 7, 7], [7, 7, 7, 7], [7, 7, 7, 7], [7, 7, 7, 7]]

def test_mat4_multiplication():
    m1 = Mat4(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)
    scalar = 2
    result = m1 * scalar
    assert result.elements == [[4, 6, 8, 10], [12, 14, 16, 18], [20, 22, 24, 26], [28, 30, 32, 34]]


