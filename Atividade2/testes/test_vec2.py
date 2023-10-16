from Atividade2.vec2 import Vec2


def test_vec2_addition():
    v1 = Vec2(1, 2)
    v2 = Vec2(3, 4)
    result = v1 + v2
    assert result.x == 4
    assert result.y == 6

def test_vec2_subtraction():
    v1 = Vec2(5, 5)
    v2 = Vec2(2, 2)
    result = v1 - v2
    assert result.x == 3
    assert result.y == 3

def test_vec2_multiplication():
    v1 = Vec2(2, 3)
    scalar = 2
    result = v1 * scalar
    assert result.x == 4
    assert result.y == 6

def test_vec2_division():
    v1 = Vec2(6, 8)
    scalar = 2
    result = v1 / scalar
    assert result.x == 3
    assert result.y == 4

def test_vec2_negation():
    v1 = Vec2(1, 2)
    result = -v1
    assert result.x == -1
    assert result.y == -2

