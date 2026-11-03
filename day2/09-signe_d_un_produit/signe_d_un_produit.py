"""signe _d un produit """

__author__ = "sossou.e"


def product_sign(a: int, b: int) -> str:
    """signe d'un nombre"""
    if a == 0 or b == 0:
        return "nul"
    elif (a > 0 and b > 0) or (a < 0 and b < 0):
        return "positif"
    else:
        return "negatif"
