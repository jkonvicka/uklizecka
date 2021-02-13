#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

__author__ = "Jakub Konvicka"
__copyright__ = "(c)2021 Jakub Konvicka"
__email__ = "jakub.konvicka@vsb.cz"
__version__ = "0.1.0"
__programname__ = "Uklizecka"
__description__ = "Uklizecka is here to tidy your directory."

import sys
from pathlib import Path
import os


def manual():
    print("Please specify ABSOLUTE directory path where " +
          __programname__ + " will work\n" + "It should look like \'uklizecka.py C:\\Users\\root\\Downloads\'")


def tidy(directory):
    for path in Path(directory).iterdir():
        if path.is_file():
            new_path = directory + "\\" + path.suffix[1:len(path.suffix)]
            if os.path.exists(new_path) is False:
                os.mkdir(new_path)
            Path.rename(path, new_path + "\\" + path.name)


def main():
    if len(sys.argv) != 2 or Path(sys.argv[1]).is_absolute() is False:
        manual()
        return
    else:
        print(__programname__ +
              " will tidy in directory: \'" + (sys.argv[1]) + '\'')
    directory = sys.argv[1]
    print("Directory " + directory + " contains " +
          str(len(os.listdir(directory))) + " files.")
    print("Do you want to tidy here? Y/n: ")
    if input()[0] == 'Y':
        tidy(directory)
        print("Done!")

    print("Bye!")


if __name__ == "__main__":
    main()
