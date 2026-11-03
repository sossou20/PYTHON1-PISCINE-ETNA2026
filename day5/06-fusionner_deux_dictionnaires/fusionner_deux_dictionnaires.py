""" exercice 6"""

__author__ = "sossou_e"


def merge_dicts(d1: dict, d2: dict) -> dict:
    """ fusionner deux dictionnaire """
    result = d1.copy()
    result.update(d2)
    return result
