"""exercice5"""

__author__ = "sossou_e"


def max_of_three(a: int, b: int, c: int) -> int:
    """comparaison de trois nombres"""
    result = a
    if b > result:
        result = b
    if c > result:
        result = c
    return result
