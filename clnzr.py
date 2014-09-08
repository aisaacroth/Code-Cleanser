#!/usr/bin/env python
import sys

def print_arguments():
    print("python {0} <filename>".format(sys.argv[0]))

def retrieve_lines_from_file(filename):
    origin_file = retrieve_file(filename)
    origin_list = get_lines(origin_file)
    origin_file.close()
    return origin_list

def retrieve_file(filename):
    return open(filename, 'r')

def get_lines(origin_file):
    return origin_file.readlines()

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

def clean(filename):
    origin_list = retrieve_lines_from_file(filename)
    clean_list = reformat_lines(origin_list)
    write_clean_file(filename, clean_list)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        clean(sys.argv[1])
    else:
        print_arguments()