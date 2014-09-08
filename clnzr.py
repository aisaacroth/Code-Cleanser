#!/usr/bin/env python
import sys

def print_arguments():
	print("python {0} <filename>".format(sys.argv[0]))

def main(filename):
	pass

if __name__ == "__main__":
	if len(sys.argv) == 2:
		main(sys.argv[1])
	else:
		print_arguments()