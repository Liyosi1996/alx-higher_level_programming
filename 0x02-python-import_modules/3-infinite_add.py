#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sum = 0
        for j in range(len(sys.argv) - 1):
            sum += int(sys.argv[j + 1])
        print('{}'.format(sum))
