#!/usr/bin/python3
"""
    a function def pascal_triangle(n): that returns
    a list of lists of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """this function will return a list of lists of integer
    representing pascal's triangle of n
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1] + [prev_row[j] + prev_row[j+1]
                     for j in range(len(prev_row)-1)] + [1]
        triangle.append(row)
    return triangle
