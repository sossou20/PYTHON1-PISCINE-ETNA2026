""" exercice 12"""

__author__ = "sossou_e"


def multiply(a: int, b: int) -> int:
    """multiplication """
    result = 0
    for _ in range(abs(b)):
        result += a
    if b < 0:
        return -result
    return result
