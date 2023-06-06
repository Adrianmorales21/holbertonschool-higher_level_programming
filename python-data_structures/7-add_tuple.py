#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    new_tuple = ()
    if tuple_a < 2:
        tuple_a = 0,
    elif tuple_a > 2:
        tuple_a = tuple_a[:2],
    if tuple_b < 0:
        tuple_b = 0,
    elif tuple_b > 2:
        tuple_b = tuple_b[:2]
    new_tuple = tuple_a + tuple_b
    return new_tuple
