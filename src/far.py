#!/bin/python3

import os
import sys
import re

FILES_TO_MODIFY = []
EXACT = False

def find_and_replace(path, query, replace):
    global FILES_TO_MODIFY, EXACT
    try:
        with open(path, 'r') as fp:
            data = fp.read()
            if EXACT:
                pattern = r'\b' + re.escape(query) + r'\b'
                modified_data = re.sub(pattern, replace, data)
            else:
                modified_data = data.replace(query, replace)
            if modified_data != data:
                FILES_TO_MODIFY.append((path, modified_data))
    except:
        print(f"[far] Failed to open file {path}! Skipping...")


def walkdirs(path, query, replace):
    if os.path.isfile(path):
        find_and_replace(path, query, replace)
    elif os.path.isdir(path):
        for root, _, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                find_and_replace(file_path, query, replace)
    else:
        print("Path does not exist:", path)


def usage():
    print("Usage:")
    print("    far <path> <query> <replace> <-flags>")
    print("Flags:")
    print("    -e    exact occurrences, uses regex to find exact matches to `query`")
    print("    -a    all occurrences, does not use regex to find exact matches to `query`")
    sys.exit(1)


def summary():
    global FILES_TO_MODIFY
    files_len = len(FILES_TO_MODIFY)

    if files_len != 0:
        print(f"[far] Found {files_len} files with the matching query.")
        for i, item in enumerate(FILES_TO_MODIFY):
            path = item[0]
            print(f"[far]    ({i}) {path}")

        print("[far] Type space separated indexes of paths to modify, or `a` for all, or `c` to cancel.")
        modify = input().split()

        if 'c' in modify:
            print("[far] Exiting...")
            return

        if 'a' in modify:
            modify = []
            for i in range(0, files_len):
                modify.append(str(i))

        try:
            modify = [int(m) for m in modify]
        except:
            print("[far] Error during parsing. Exiting...")
            return

        for i in modify:
            path = FILES_TO_MODIFY[i][0]
            data = FILES_TO_MODIFY[i][1]
            with open(path, 'w') as fp:
                fp.write(data)
            print(f"[far] Modified: {path}")

    else:
        print("[far] No files had the matching query.")
    print("[far] Done.")


argv = sys.argv[1::]
argc = len(argv) - 1

if argc < 3:
    usage()

path = argv[0]
query = argv[1]
replace = argv[2]
flag = argv[3]

if flag == "-e":
    EXACT = True
elif flag == "-a":
    EXACT = False
else:
    print(f"[far] Unknown flag {flag}")
    usage()

walkdirs(path, query, replace)

summary()
