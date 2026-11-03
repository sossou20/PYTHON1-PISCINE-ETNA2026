""" exercice 9"""

__author__ = "sossou_e"


def remove_duplicates(lst: list) -> list:
    """suppression des doublins """
    return list(dict.fromkeys(lst))
