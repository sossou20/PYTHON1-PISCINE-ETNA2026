"""nombre pair ou multiple """

__author__ = "sossou_e"


def check_number(n: int) -> str:
    """nombre pair ou multiple """
    if n % 3 == 0:
        return "multiple de 3"
    elif n % 2 == 0:
        return "pair"
    else:
        return "rien de special"
