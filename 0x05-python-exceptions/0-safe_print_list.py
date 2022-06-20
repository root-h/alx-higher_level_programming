#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list
    Args:
        my_list: list
        x: integer rep. number of elements to print
    Return: actual number of elements printed
    """
    i = 0
    while i < x:
        try:
            print(my_list[i], end="")
        except IndexError:
            break
        else:
            i += 1

    print()
    return i
