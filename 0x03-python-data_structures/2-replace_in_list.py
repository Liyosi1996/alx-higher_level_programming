#!/usr/bin/python3
def replace_in_list(my_list, num, element):
    if num > (len(my_list) - 1) or num < 0:
        return my_list
    else:
        my_list[num] = element
        return my_list
