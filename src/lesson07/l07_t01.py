# -*- coding: UTF-8 -*-

import argparse
import datetime
import os
from os.path import join, getsize, getmtime
import sys


def get_time_str(root, f):
    file_time = datetime.datetime.fromtimestamp(getmtime(join(root, f)))
    return file_time.strftime("%Y-%m-%d %H:%M:%S")


def get_size_str(root, f):
    size = getsize(join(root, f))
    return "{:17,d}".format(size)


def check_conditions(root, f, extension, date):
    if not str.lower(f).endswith(str.lower(extension)):
        return False
    file_date = datetime.date.fromtimestamp(getmtime(join(root, f)))
    if file_date < date:
        return False
    return True


def print_files(root, dirs, files, folders, extension, date):
    print(" Directory of {}\n".format(root))
    if folders:
        for d in dirs:
            print("{}    <DIR>          {}".format(get_time_str(root, d), d))
    for f in files:
        if check_conditions(root, f, extension, date):
            print("{} {} {}".format(get_time_str(root, f),
                                    get_size_str(root, f),
                                    f))
    print("")


def main(date, extension, folders, path, recursive):
    g = os.walk(path)
    print_files(*(g.__next__()),
                folders=folders,
                extension=extension,
                date=date)
    if recursive:
        for root, dirs, files in g:
            print_files(root, dirs, files, folders, extension, date)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Displays a list of files and subdirectories in a "
                    "directory.")
    parser.add_argument("-d",
                        default=datetime.date.min,
                        type=lambda s: datetime.datetime.strptime(s,
                                                 "%Y-%m-%d").date(),
                        help="filters files by modification date "
                             "(-d YYYY-MM-DD)")
    parser.add_argument("-e",
                        default="",
                        help="filters files by extension (-e EXT)")
    parser.add_argument("-f",
                        action="store_true",
                        help="displays folders")
    parser.add_argument("-p",
                        default=sys.path[0],
                        help="specifies path to list (-p PATH)")
    parser.add_argument("-r",
                        action="store_true",
                        help="proceeds subfolders recursively")
    args = parser.parse_args()
    main(args.d, args.e, args.f, args.p, args.r)
