"""exercice 12"""

__author__ = "sossou_e"


def is_prime_optimized(n: int) -> bool:
    """ nombre premier optimized """
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
