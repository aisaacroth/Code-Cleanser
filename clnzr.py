#!/usr/bin/env python3
''' A simple script to remove access whitespace at the end
of each line in a file.

Author:  Alexander Roth
Date:    2014-09-07
Updated: 2014-10-03
'''
import glob
import sys


def clean(filename):
    origin_list = retrieve_lines_from_file(filename)
    clean_list = reformat_lines(origin_list)
    write_clean_file(filename, clean_list)


def clean_multiple_files(file_type):
    file_list = catch_all_files(file_type)
    for i in file_list:
        clean(i)


def print_arguments():
    print("Single file: python3 {0} <filename>".format(sys.argv[0]))
    print("Mutliple files: python3 {0} all <file extention>".format(sys.argv[0]))


def catch_all_files(file_type):
    file_list = []
    extension = '*.' + str(file_type)
    file_list.extend(glob.glob(extension))
    return file_list


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
    elif len(sys.argv) == 3:
        clean_multiple_files(sys.argv[2])
    else:
        print_arguments()
