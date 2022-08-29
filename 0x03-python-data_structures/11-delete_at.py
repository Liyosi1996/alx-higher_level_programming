#!/usr/bin/python3
def delete_at(my_list=[], num=0):
    if num < 0 or num >= len(my_list):
        return my_list
    else:
        del my_list[num]
    return my_list
