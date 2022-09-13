#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div = []
    result = 0
    if list_length <= 0:
        print("out of range")
        return div
    while div < list_length:
        try:
            div.append(my_list_1[result] / my_list_2[result])
        except ZeroDivisionError:
             print("division by 0")
             div.append(0)
        except TypeError:
             print("wrong type")
              div.append(0)
        except IndexError:
             print("out of range")
             div.append(0)
        finally:
            result += 1
    return div
