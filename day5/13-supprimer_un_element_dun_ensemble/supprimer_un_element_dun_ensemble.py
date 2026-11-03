""" suppression de element d'un ensemble """

__author__ = "sossou_e"


def remove_from_set(s: set, elem) -> set:
    """ supprimer un element specifique dans un ensemble """
    if elem in s:
        s.remove(elem)
    return s
