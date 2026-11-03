""" conversion note lettre """

__author__ = "sossou_e"


def grade_conversion(score: int) -> str:
    """ conversion_note """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
