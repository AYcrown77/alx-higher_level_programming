#!/usr/bin/python

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maxim = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > maxim:
            maxim = my_list[i]
    return maxim
