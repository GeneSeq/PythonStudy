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


# From class
# def p_distance(str1, str2):
#     """
#
#     :param str1:
#     :param str2:
#     :return:
#     """
#     if len(str1) != len(str2):
#         raise ValueError("")
#     mismatches = 0
#     for a, b in izip(str1, str2):
#         if a != b and a != "-" and b != "-":
#             mismatches += 1
#         else


def matrix_mul(matr1, matr2):
    nrow_matr1, ncol_matr1 = len(matr1), len(matr1[0])
    nrow_matr2, ncol_matr2 = len(matr2), len(matr2[0])
    if ncol_matr1 != nrow_matr2:
        raise ValueError("")
    matrix_mult_res = [[None for j in xrange(ncol_matr2)]
                       for i in xrange(nrow_matr1)]
    def get_col(matr, j):
        return [row[j] for row in matr]