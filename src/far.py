#!/bin/python3

import os


def walkdirs(path, query, replace):
    if os.path.isfile(path):
        print("Found file:", path)
    elif os.path.isdir(path):
        for root, _, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                fp = open(file_path, "rw")
    else:
        print("Path does not exist:", path)


def usage():
    print("Usage:")
    print("    far <path> <query> <replace>")
    sys.exit(1)


argv = os.sys.argv[1::]
argc = len(argv) - 1

if argc < 2:
    usage()

path = argv[0]
query = argv[1]
replace = argv[2]

walkdirs(path, query, replace)
