#!/usr/bin/python3


def max_integer(my_list=[]):
    if my_list is None:
        my_list[0] = None
        return my_list[0]
    my_list.sort()
    my_list.reverse()
    return my_list[0]
