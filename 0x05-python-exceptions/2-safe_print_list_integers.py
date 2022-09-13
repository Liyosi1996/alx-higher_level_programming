#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = print_int = 0
    while True:
        try:
            if num < x:
                print("{:d}".format(my_list[num]), end="")
                num += 1
                print_int += 1
            else:
                print()
                return print_int
        except (ValueError, TypeError):
            num += 1
