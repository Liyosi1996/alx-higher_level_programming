#!/usr/bin/python3
def magic_calculation(a, b):
    total = 0
    for j in range(1, 3):
        try:
            if j > a:
                raise Exception('Too far')
            else:
                total += a ** b / j
        except:
            total = b + a
            break
        return total

