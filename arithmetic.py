"""
Arithmetic module is to perform arithmetic calculations
like add,sub,etc...
"""


def add(value_1, value_2):
    """
    Add function takes 2 parameters returns total
    :param value_1: any object
    :param value_2: any object
    :return: single object
    """
    return value_1 + value_2


def sub(value_1, value_2):
    """
    Sub function takes 2 parameters returns difference
    :param value_1: any object
    :param value_2: any object
    :return: single object
    """
    return value_1 - value_2


VALUE = 9999

if __name__=="__main__":
    print(add(10,20))
    print(sub(100,200))