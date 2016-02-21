#! /ust/bin/env python


"""
IO streams, context manager, RAM, lazy evaluation, generators, generator
expressions, execution mode
"""


from __future__ import print_function, division
import lesson5
import os
import sys

lesson5.calculate()



file_path = os.path.abspath(sys.argv[1])


def print_parsed_csv(fp, sep=","):
    with open(fp) as input_file:
        for line in input_file:
            print(*line.strip().split(sep))


def my_xrange(start, end, step):
    curr_value = start
    while curr_value < end:
        yield curr_value
        curr_value += step


def my_map_lazy(fn, iterable):
    for item in iterable:
        yield fn(item)


def my_filter_lazy(fn, iterable):
    for item in iterable:
        if fn(item):
            yield item


import itertools

args = zip(xrange(10, 10000, 1000), xrange(10, 10000, 1000))


mapped = [id(num1) == id(num2) for num1, num2 in args if num1 > 1000]
mapped_lazy = (id(num1) == id(num2) for num1, num2 in args if num1 > 1000)

dic = {1: 1, 2: 2, 3: 3}

generated_dict = {key: fn(value) for key, value in dic.iteritems()}


if __name__ == "__main__":
    pass
