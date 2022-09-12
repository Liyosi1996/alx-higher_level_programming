#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div = []
    result = 0
    if list_length <= 0:
        print("out of range")
        return div
    while result < list_length:
        try:
            result.append(my_list_1[result] / my_list_2[result]
        except TypeError:
            result = 0
            print("wrong type")
            div.append(0)
        except ZeroDivisionError:
            result = 0
            print("division by 0")
            div.append(0)
        except IndexError:
            result = 0
            print("out of range")
            div.append(0)
        finally:
             result += 1
    return div
