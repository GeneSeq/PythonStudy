#! /usr/bin/env python


"""

"""


from __future__ import  division, print_function
from itertools import ifilter, imap, izip


# Hamming
def ham(seq1, seq2):
    """
    :type seq1: str
    :param seq1:
    :type seq2: str
    :param seq2:
    :return:
    """
    if len(seq1) != len(seq2):
        raise ValueError("")
    return sum(char1 != char2 for char1, char2 in izip(seq1, seq2))


# # p-distance
# def p_distance(seq1, seq2):
#     """
#     :type seq1: str
#     :param seq1:
#     :type seq2: str
#     :param seq2:
#     :return:
#     """
#     if len(seq1) != len(seq2):
#         raise ValueError("")
#     # (sum(char1 != char2 and char1 != "-" and char2 != "-"
#                 # for char1, char2 in izip(seq1, seq2)))/(sum((char1 != char2 and char1 != "-" and char2 != "-"), (char1 == char2) for char1, char2 in zip(seq1, seq2)))


# Dot_product
def matrix_mul(mx1, mx2):
    """
    :type mx1: list
    :param mx1:
    :type mx2: list
    :param mx2:
    :return:
    """
    if ncol_mx1 != nrow_mx2:
        raise ValueError("")
    nrow_mx1, ncol_mx1 = len(mx1), len(mx1[0])
    nrow_mx2, ncol_mx2 = len(mx2), len(mx2[0])
    multipl_result = [[None for j in xrange(ncol_mx2)]
                      for i in xrange(nrow_mx1)]
    def get_col(mx, j):
        return [row[j] for row in mx]