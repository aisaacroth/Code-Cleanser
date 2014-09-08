#!/usr/bin/env python
import sys

def clean(filename):
    origin_list = retrieve_lines_from_file(filename)
    clean_list = reformat_lines(origin_list)
    write_clean_file(filename, clean_list)

def print_arguments():
    print("python {0} <filename>".format(sys.argv[0]))

def retrieve_lines_from_file(filename):
    origin_file = open(filename, 'r')
    origin_list = origin_file.readlines()
    origin_file.close()
    return origin_list

def reformat_lines(origin_list):
    clean_list = remove_trailing_whitespace(origin_list)
    complete_list = append_newline(clean_list)
    return complete_list

def remove_trailing_whitespace(origin_list):
    return [line.rstrip() for line in origin_list]

def append_newline(clean_list):
    return [line + "\n" for line in clean_list]

def write_clean_file(filename, complete_list):
    clean_file = open(filename, 'w')
    for line in complete_list:
        clean_file.write("%s" % line)
    clean_file.close()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        clean(sys.argv[1])
    else:
        print_arguments()