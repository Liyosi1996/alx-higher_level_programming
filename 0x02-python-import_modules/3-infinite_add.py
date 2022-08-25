#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    sum = 0
    if len(argv) > 1:
        for j in range(1, len(argv)):
            sum += int(argv[j])
        print('{}'.format(sum))
