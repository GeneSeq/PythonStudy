#! /usr/bin/env python


"""
Lesson 5 code
"""


from __future__ import division, print_function
from itertools import izip
import operator


FLOAT_PREC = 10


# Task 2
def my_max(*args):
    if not args:
        raise ValueError("No arguments passed")

    def find_max(sequence):
        if not isinstance(sequence, (tuple, list)):
            raise ValueError("Received one arguments that is not of "
                             "type Union[tuple, list])")
        current_max = sequence[0]
        for element in sequence:
            if not isinstance(element, int):
                raise ValueError("")
            if current_max < element:
                current_max = element
        return current_max

    return find_max(args[0] if len(args) == 1 else args)

# Task 2.1


def my_max_iter(*args):
    if not args:
        raise ValueError("No arguments passed")

    def find_max(sequence):
        sequence_iterator = iter(sequence)
        current_max = next(sequence_iterator)
        for element in sequence:
            if not isinstance(element, int):
                raise ValueError("")
            if current_max < element:
                current_max = element
        return current_max

    return find_max(args[0] if len(args) == 1 else args)


# Task 3

def root(num, p=2):
    return num**(1/p)


def my_map(fn, elements, **kwargs):
    result = []
    for element in elements:
        result.append(fn(element, **kwargs))
    return result


# Task 4

def calculate(numbers, operations):
    if len(numbers) != len(operations) + 1:
        raise ValueError("msg")
    operation_dict = {
        "+": operator.add,
        "*": operator.mul,
        "/": operator.div
    }
    numbers_iterator = iter(numbers)
    acc = next(numbers_iterator)
    for num, oper in zip(numbers_iterator, operations):
        oper_func = operation_dict.get(oper)
        if not oper_func:
            raise ValueError("Operation {} is not supported".format(oper))
        acc = oper_func(acc, num)
    return acc


def calculate_functional(numbers, operations):
    if len(numbers) != len(operations) + 1:
        raise ValueError("msg")
    oper_dict = {
        "+": operator.add,
        "*": operator.mul,
        "/": operator.div
    }
    number_iterator = iter(numbers)
    return reduce(lambda acc, (num, oper): oper_dict[oper](acc, num),
                  izip(number_iterator, operations), next(number_iterator))


def my_max_functional(iterable):
    return reduce(lambda curr_max, num: num if num > curr_max else curr_max,
                  iterable)

