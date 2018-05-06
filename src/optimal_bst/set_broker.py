#!/usr/bin/env python
# -*- coding: utf-8 -*-


def set_broker():
    s = [(37, 19), (51, 17), (21,3), (22,12), (35, 21),
(32,14), (19, 6), (10, 6), (29, 17), (45, 10), (2, 4), (27, 9), (19, 6), (34,3)]
    first_set = [x[0] for x in s]
    second_set = [x[1] for x in s]
    print("Set of indexes: ", first_set)
    print("Set of frequencies: ", second_set)


if __name__ == "__main__":
    set_broker()