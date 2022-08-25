#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ar = len(sys.argv)
    if ar == 1:
        print("{} arguments.".format(ar - 1))
    elif ar == 2:
        print("{} arguments:".format(ar - 1))
    else:
        print("{} arguments:".format(ar - 1))
    for j in range(1, ar):
        print("{}: {}".format(j, sys.argv[j]))
