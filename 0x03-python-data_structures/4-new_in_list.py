#!/usr/bin/python3
def new_in_list(my_list, num, element):
    new_list = my_list[:]
    if 0 <= num < len(new_list):
        new_list[num] = element
        return (new_list)
    return (my_list)
