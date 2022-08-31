#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for num in list(a_dictionary.keys()):
        if a_dictionary[num] == value:
            del a_dictionary[num]
    return a_dictionary
