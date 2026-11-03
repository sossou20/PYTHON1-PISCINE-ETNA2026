"""categorieoh"""

__author__ = "sossou_e"


def age_category(age: int) -> str:
    """categorie d'age"""
    if age < 12:
        return "enfant"
    elif age < 18:
        return "ado"
    elif age < 70:
        return "adulte"
    else:
        return "senior"
