#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    s = sum([a * b for a, b in my_list])
    res = s / sum([b for a, b in my_list])
    return res
