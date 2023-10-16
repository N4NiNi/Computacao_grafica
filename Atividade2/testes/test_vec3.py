from Atividade2.vec3 import Vec3

def test_vec3_addition():
    v1 = Vec3(1, 2, 3)
    v2 = Vec3(4, 5, 6)
    result = v1 + v2
    assert result.x == 5
    assert result.y == 7
    assert result.z == 9

def test_vec3_subtraction():
    v1 = Vec3(5, 5, 5)
    v2 = Vec3(2, 2, 2)
    result = v1 - v2
    assert result.x == 3
    assert result.y == 3
    assert result.z == 3

def test_vec3_multiplication():
    v1 = Vec3(2, 3, 4)
    scalar = 2
    result = v1 * scalar
    assert result.x == 4
    assert result.y == 6
    assert result.z == 8

def test_vec3_division():
    v1 = Vec3(6, 8, 10)
    scalar = 2
    result = v1 / scalar
    assert result.x == 3
    assert result.y == 4
    assert result.z == 5

def test_vec3_negation():
    v1 = Vec3(1, 2, 3)
    result = -v1
    assert result.x == -1
    assert result.y == -2
    assert result.z == -3

def test_vec3_length():
    v1 = Vec3(3, 4, 5)
    assert v1.length() == 7.0710678118654755  # Valor esperado após cálculo

