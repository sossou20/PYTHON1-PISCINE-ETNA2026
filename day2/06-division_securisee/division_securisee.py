""" exercice06"""

__author__ = "sossou_e"


def safe_divide(a: int, b: int) -> float:
    """division_securiser"""
    try:
        return a / b
    except ZeroDivisionError:
        return "Erreur : division par zéro"
