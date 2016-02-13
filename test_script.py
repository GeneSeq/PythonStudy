#! /usr/bin/env


from __future__ import print_function, division
import sys
import os


def print_parsed_csv(fp, sep=","):
    with open(fp) as input_file:
        for line in input_file:
            print(*line.strip().split(sep)[:5])


def main():
    file_path = os.path.abspath(sys.argv[1])
    print_parsed_csv(file_path, sep="\t")


if __name__ == "__main__":
    main()