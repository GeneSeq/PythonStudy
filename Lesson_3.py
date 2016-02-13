#! /usr/bin/env python


"""
practice
"""


from __future__ import division, print_function


# and
def _and(left, right):
    if bool(left):
        return right
    return left

# or
def _or(left, right):
    if bool(left):
        return left
    return right

# val1 if condition else val2
def tt(val1, cond, val2):
    if bool(cond):
        return val1
    return val2

# any root
def root(p, num):
    return None if not p%2 and num < 0 else num**(1/p)

# not
def _not(val):
    if bool(val):
        return False
    return True

def _not(val):
    return False if bool(val) else True

