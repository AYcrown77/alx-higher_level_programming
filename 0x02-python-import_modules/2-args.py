#!/usr/bin/python3
if __name__ == "__main__":
    import sys

arg_len = len(sys.argv) - 1
if arg_len == 0:
    print("{:d} arguments.".format(arg_len))
if arg_len == 1:
    print("{:d} argument:".format(arg_len))
    print("{:d}: {}".format(arg_len, sys.argv[arg_len]))
if arg_len > 1:
    print("{:d} arguments:".format(arg_len))
    for i in range(arg_len + 1):
        print("{:d}: {}".format(i, sys.argv[i]))
