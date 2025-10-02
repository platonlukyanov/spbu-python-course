from typing import Iterable
import math


class Vector:
    """Vector class that supports multiplication (scalar product), length calculation and angle calculation\

    Example of usage:
    >>> vec1 = Vector(1, 1, 1)
    >>> vec2 = Vector(4, 5, 6)
    >>> vec1 * vec2 # returns 30
    >>> vec1.length() # 1
    >>> vec1.angle(vec2) # returns 90
    """

    values: Iterable[int | float] = []

    def __init__(self, *values: int | float):
        self.values = values

    def __mul__(self, other) -> int | float:
        """Calculates the scalar product of two vectors"""
        scalar_product = 0

        for x, y in zip(self.values, other.values):
            scalar_product += x * y

        return scalar_product

    def length(self):
        """Calculates the length of the vector"""
        sum_of_squares = 0
        for x in self.values:
            sum_of_squares += x**2

        return math.sqrt(sum_of_squares)

    def angle(self, other):
        """Calculates the angle between two vectors. Returns an angle in degrees"""
        dot_product = self * other
        length_product = self.length() * other.length()
        return math.acos(dot_product / length_product) * 180 / math.pi


class Matrix:
    """Matrix class that supports addition, multiplication and transposition
    Example of usage:
    >>> mat1 = Matrix(
    ...     [1, 2, 3],
    ...     [4, 5, 6],
    ...     [7, 8, 9]
    ... )
    >>> mat2 = Matrix(
    ...     [1, 2, 3],
    ...     [4, 5, 6],
    ...     [7, 8, 9]
    ... )
    >>> mat1 + mat2 # returns Matrix([[2, 4, 6], [8, 10, 12], [14, 16, 18]])
    >>> mat1 * mat2 # returns Matrix([[30, 36, 42], [66, 81, 96], [102, 126, 150]])
    >>> mat1.transpose() # returns Matrix([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
    """

    values: Iterable[Iterable[int | float]] = []

    def __init__(self, *values: Iterable[int | float]):
        self.values = values

    def __add__(self, other):
        """Adds two matrices"""
        if len(self.values) != len(other.values):
            raise ValueError("Matrices must have the same dimensions")

        result = []
        for i in range(len(self.values)):
            result.append([])
            for j in range(len(self.values[0])):
                result[i].append(self.values[i][j] + other.values[i][j])
        return Matrix(*result)

    def __mul__(self, other):
        """Multiplies two matrices"""
        if len(self.values[0]) != len(other.values):
            raise ValueError("Matrices must have the same dimensions")

        result = []
        for i in range(len(self.values)):
            result.append([])
            for j in range(len(other.values[0])):
                result[i].append(
                    sum(
                        self.values[i][k] * other.values[k][j]
                        for k in range(len(self.values[0]))
                    )
                )
        return Matrix(*result)

    def transpose(self):
        """Transposes a matrix"""
        result = []
        for i in range(len(self.values[0])):
            result.append([])
            for j in range(len(self.values)):
                result[i].append(self.values[j][i])
        return Matrix(*result)

    def __eq__(self, other):
        """Checks if two matrices are equal"""
        if len(self.values) != len(other.values):
            return False
        for i in range(len(self.values)):
            if len(self.values[i]) != len(other.values[i]):
                return False
            for j in range(len(self.values[i])):
                if self.values[i][j] != other.values[i][j]:
                    return False
        return True
