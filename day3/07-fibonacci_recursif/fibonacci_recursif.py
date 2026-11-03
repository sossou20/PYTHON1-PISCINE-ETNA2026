""" exercice 07"""

__author__ = "sossou_e"


def fibonacci(n: int) -> int:
    """fibonacci vas y """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
