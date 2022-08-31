#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def search_replace_num(num):
        return (num if num != search else replace)
    return list(map(search_replace_num, my_list))
