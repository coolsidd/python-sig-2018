#!/usr/bin/python

import os
import sys
import difflib


if len(sys.argv) != 3:
    print("Usage ./file_comparer.py file_1 file_2")
    sys.exit(-1)

home_dir = os.getcwd()


def compare(first_file, second_file):
    with open(first_file, 'r') as master, open(second_file, 'r') as slave:
        diff = difflib.unified_diff(
            master.readlines(), slave.readlines(), lineterm='')
        print(''.join(diff))



        # get the files from the user and find their absolute paths
file_1, file_2 = sys.argv[1:]
file_1, file_2 = os.path.abspath(file_1), os.path.abspath(file_2)

# check is the files exist
if os.path.isfile(file_1) and os.path.isfile(file_2):
    compare(file_1, file_2)
else:
    if not os.path.isfile(file_1):
        print("file :{} does not exist".format(file_1))
    if not os.path.isfile(file_2):
        print("file :{} does not exist".format(file_2))
    sys.exit(-2)
