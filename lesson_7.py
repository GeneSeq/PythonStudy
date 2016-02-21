#! /usr/bin/env python


"""
recursion, Fibonachi sequence, dinamic programming
"""


from __future__ import  division, print_function
import os
import sys


def fib_rec(n):
    if n == 0 or n == 1:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)
# it was naive algorithm - not effective, but beutiful
# never write this one


def fib_linear(n):
    fib_sequence = [1, 1]
    for _ in xrange(n-1): # to not do one overstep
        fib_sequence.append(fib_sequence[-2]+fib_sequence[-1])
    return fib_sequence[-1]


def fib_linear_memory_efficient(n):
    fib_prev, fib_prev_prev = 1, 1
    for _ in xrange(n-1):
        fib_prev_prev, fib_prev = fib_prev, fib_prev + fib_prev_prev
    return fib_prev


# there is one more variant - recursive and memory effective, but not now


# from homework Fasta reader
def fasta_reader(fp):
    sequence_stack = []
    with open(fp) as fasta_file:
        for nonempty_line in (line for line in fasta_file if line.strip()): # lazy generator
            if nonempty_line.startswith(">"):
                if sequence_stack:
                    yield sequence_stack[0], "".join(sequence_stack[1])
                sequence_stack = []
                sequence_stack.append(nonempty_line.strip("> \n"))
                sequence_stack.append([])
            elif nonempty_line.startswith("#"):
                continue
            else:
                sequence_stack[-1].append(nonempty_line.strip())
        yield sequence_stack[0], "".join(sequence_stack[1])


