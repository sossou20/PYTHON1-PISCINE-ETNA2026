""" exercice 4"""

__author__ = "sossou_e"


def is_leap_year(year: int) -> bool:
    """ bissextyile """
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
