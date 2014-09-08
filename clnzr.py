#!/usr/bin/env python
import sys

def print_arguments():
    print("python {0} <filename>".format(sys.argv[0]))

def retrieve_file(filename):
    origin_file = open(filename, 'r')
    return origin_file

def get_lines(origin_file):
    origin_list = origin_file.readlines()
    return origin_list

def main(filename):
    pass

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print_arguments()