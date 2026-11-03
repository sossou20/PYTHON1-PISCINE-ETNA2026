""" exercice 14 """

__author__ = "sossou_e"


def min_max(numbers: list) -> tuple:
    """ montre le min et msx """
    smallest = numbers[0]
    biggest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
        if number > biggest:
            biggest = number
    return (smallest, biggest)
