from Atividade2.mat2 import Mat2

def test_mat2_addition():
    m1 = Mat2(1, 2, 3, 4)
    m2 = Mat2(5, 6, 7, 8)
    result = m1 + m2
    assert result.elements == [[6, 8], [10, 12]]

def test_mat2_subtraction():
    m1 = Mat2(10, 10, 10, 10)
    m2 = Mat2(3, 3, 3, 3)
    result = m1 - m2
    assert result.elements == [[7, 7], [7, 7]]

def test_mat2_multiplication():
    m1 = Mat2(2, 3, 4, 5)
    scalar = 2
    result = m1 * scalar
    assert result.elements == [[4, 6], [8, 10]]

