"""exercice 06"""

__author__ = "sossou_e"


def recursive_factorial(n: int) -> int:
    """ FACTORIATION """
    if n <= 1:
        return 1
    return n * recursive_factorial(n - 1)
