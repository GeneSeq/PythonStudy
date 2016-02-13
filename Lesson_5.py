#! usr/bin/env python


"""

"""


from __future__ import division, print_function
import operator


# Task 2 from hw


def my_max(*args):
    if not args:
        raise ValueError("No arguments passed")
    def find_max(sequence):
        if not isinstance(sequence, (tuple, list)):
            raise ValueError("Recieved only one non-list/tuple argument")
        current_max = sequence[0]
        for element in sequence:
            if not isinstance(element, int):
                raise ValueError("Recieved argument is not int")
            if current_max < element:
                current_max = element
        return current_max
    return find_max(args[0] if len(args) == 1 else args)


# Task 2.1 from hw
# We don't need tuple/list - any iterable object


def my_max(*args):
    if not args:
        raise ValueError("No arguments passed")
    def find_max(sequence):
        sequence_iterator = iter(sequence)
        current_max = next(sequence_iterator)
        for element in sequence_iterator:
            if not isinstance(element, int):
                raise ValueError("Recieved argument is not int")
            if current_max < element:
                current_max = element
        return current_max
    return find_max(args[0] if len(args) == 1 else args)


# Task 3 from hw
# My_map


def my_map(fn, elements, **kwargs):
    result = []
    for element in elements:
        result.append(fn(element, **kwargs))
    return result


# Task 4 from hw


def calculate(numbers, operations):
    if len(numbers) != len(operations) + 1:
        raise ValueError("Not enough mana")
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
            raise ValueError("Operation {} is not supported".format(opre))
        acc = oper_func(acc, num)
    return acc


# ***


def my_max