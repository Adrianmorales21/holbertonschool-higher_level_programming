#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if set_1 is not None and set_2 is not None:
        set_dif1 = set_1.difference(set_2)
        set_dif2 = set_2.difference(set_1)
        return set.union(set_dif1, set_dif2)
    return ()
