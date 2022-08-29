#!/usr/bin/python

def divisible_by_2(my_list=[]):
    ret_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            ret_list += [1]
        else:
            ret_list += [0]
    return (ret_list)
