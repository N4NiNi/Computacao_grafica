from Atividade2.mat3 import Mat3

def test_mat3_addition():
    m1 = Mat3(1, 2, 3, 4, 5, 6, 7, 8, 9)
    m2 = Mat3(9, 8, 7, 6, 5, 4, 3, 2, 1)
    result = m1 + m2
    assert result.elements == [[10, 10, 10], [10, 10, 10], [10, 10, 10]]

def test_mat3_subtraction():
    m1 = Mat3(10, 10, 10, 10, 10, 10, 10, 10, 10)
    m2 = Mat3(3, 3, 3, 3, 3, 3, 3, 3, 3)
    result = m1 - m2
    assert result.elements == [[7, 7, 7], [7, 7, 7], [7, 7, 7]]

def test_mat3_multiplication():
    m1 = Mat3(2, 3, 4, 5, 6, 7, 8, 9, 10)
    scalar = 2
    result = m1 * scalar
    assert result.elements == [[4, 6, 8], [10, 12, 14], [16, 18, 20]]


