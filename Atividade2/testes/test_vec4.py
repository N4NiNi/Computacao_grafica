from Atividade2.vec4 import Vec4

def test_vec4_addition():
    v1 = Vec4(1, 2, 3, 4)
    v2 = Vec4(5, 6, 7, 8)
    result = v1 + v2
    assert result.x == 6
    assert result.y == 8
    assert result.z == 10
    assert result.a == 12

def test_vec4_subtraction():
    v1 = Vec4(10, 10, 10, 10)
    v2 = Vec4(3, 3, 3, 3)
    result = v1 - v2
    assert result.x == 7
    assert result.y == 7
    assert result.z == 7
    assert result.a == 7

def test_vec4_multiplication():
    v1 = Vec4(2, 3, 4, 5)
    scalar = 2
    result = v1 * scalar
    assert result.x == 4
    assert result.y == 6
    assert result.z == 8
    assert result.a == 10

def test_vec4_division():
    v1 = Vec4(8, 10, 12, 14)
    scalar = 2
    result = v1 / scalar
    assert result.x == 4
    assert result.y == 5
    assert result.z == 6
    assert result.a == 7

def test_vec4_negation():
    v1 = Vec4(1, 2, 3, 4)
    result = -v1
    assert result.x == -1
    assert result.y == -2
    assert result.z == -3
    assert result.a == -4


