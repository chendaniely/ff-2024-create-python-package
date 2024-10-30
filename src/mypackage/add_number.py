# pyright: strict
"""A module that adds numbers together"""


def add_num(num_1: int | float, num_2: int | float) -> int | float:
    """A function that adds two numbers together

    Parameters
    ----------
    num_1 : number
        a number
    num_2 : number
        another number to add

    Returns
    -------
    number
        sum of the numbers
    """
    return num_1 + num_2
