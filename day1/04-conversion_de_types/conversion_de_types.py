""" exercice """

__author__ = "sossou_e"


def convert_type(value) -> str:
    """ conversion de type """
    if type(value) is str:
        return int(value)
    return str(value)
