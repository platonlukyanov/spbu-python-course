import pytest
from project.homework_1.index import Vector, Matrix


def test_vector_initialization():
    vec = Vector(1, 2, 3)
    assert vec.values[0] == 1
    assert vec.values[1] == 2
    assert vec.values[2] == 3


def test_vector_multiplication():
    vec1 = Vector(1, 2, 3)
    vec2 = Vector(4, 5, 6)
    assert vec1 * vec2 == 32


def test_vector_length():
    vec = Vector(1, 0, 0)
    assert vec.length() == 1


def test_vector_angle():
    vec1 = Vector(1, 0, 0)
    vec2 = Vector(0, 1, 0)
    assert vec1.angle(vec2) == 90


def test_matrix_initialization():
    mat = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
    assert mat.values[0][0] == 1
    assert mat.values[0][1] == 2
    assert mat.values[0][2] == 3
    assert mat.values[1][0] == 4
    assert mat.values[1][1] == 5
    assert mat.values[1][2] == 6
    assert mat.values[2][0] == 7
    assert mat.values[2][1] == 8
    assert mat.values[2][2] == 9


def test_matrix_addition():
    mat1 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
    mat2 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
    mat3 = Matrix([2, 4, 6], [8, 10, 12], [14, 16, 18])
    assert mat1 + mat2 == mat3


def test_matrix_multiplication():
    mat1 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
    mat2 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
    mat3 = Matrix([30, 36, 42], [66, 81, 96], [102, 126, 150])
    assert mat1 * mat2 == mat3


def test_matrix_transposition():
    mat = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
    mat2 = Matrix([1, 4, 7], [2, 5, 8], [3, 6, 9])
    assert mat.transpose() == mat2
