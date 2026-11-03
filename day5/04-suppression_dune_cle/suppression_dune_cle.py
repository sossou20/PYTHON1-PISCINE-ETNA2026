""" exercice 4"""

__author__ = "sossou_e"


def remove_key(d: dict, key) -> dict:
    """ supression d'unecle """
    if key in d:
        del d[key]
    return d
