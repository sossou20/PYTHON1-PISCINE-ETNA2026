""" exercice 13 """

__author__ = "sossou_e"


def sum_list(numbers: list) -> int:
    """ renommer le somme des element d'une liste"""
    total = 0
    for number in numbers:
        total += number
    return total
