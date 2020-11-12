#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kenzie assignment: Lists!
"""
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Instructions:
# Complete each function below by writing the code for it. main() is already
# set up to test all the functions with a few different inputs, printing 'OK'
# for each function once it returns the correct result.
# The starter code for each function includes a bare 'return' which is just a
# placeholder for your code.

# Your name, plus anyone who helped you with this assignment.
# Give credit where credit is due.
__author__ = "???"

# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.


def match_ends(words):
    # your code here
    return


# B. front_x
# Given a list of strings, return a list with the strings in
# sorted order, except group all the strings that begin with
# 'x' first.
# Example:
#   ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
#   ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each
# of them before combining them.


def front_x(words):
    # your code here
    return


# C. sort_last
# Given a list of non-empty tuples, return a list sorted in
# increasing order by the last element in each tuple.
# Example
#   [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
#   [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element from each tuple.


def sort_last(tuples):
    # your code here
    return


# D. remove_adjacent
# Given a list of numbers, return a list where all adjacent
# equal elements have been reduced to a single element.
# Example:
#   [1, 2, 2, 3] -> [1, 2, 3]
# You may create a new list or modify the passed in list.
# Hint: Don't use set()


def remove_adjacent(nums):
    # your code here
    return


# E. zip_merge
# Given two lists, combine the values from their corresponding
# indices into a single list.
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# result = ['My', 'name', 'is', 'Kelly']
# Hint: Think of it as "zipping" two lists together.  Is there
# a built-in function in python that will do this?


def zip_merge(list1, list2):
    # your code here
    return


# F. empty_filter
# Given a single list containing strings, empty strings, and
# None values:  Return a new list with the same elements, but
# strip out (filter) the empty strings and None values away.
# example: list1 = ["Mike", "", "Emma", None, "Kelly", "", "Brad", None]
# result:  ["Mike", "Emma", "Kelly", "Brad"]
# Hint: There is a Python idiom for doing this.  Can you find it?


def empty_filter(list1):
    # your code here
    return


# G. linear_merge
# Given two lists sorted in increasing order, create and
# return a merged list of all the elements in sorted order.
# You may modify the passed in lists.
# The solution should work in "linear" time, making a single
# pass of both lists.
# Hint: Don't use `sort` or `sorted` -- they are not O(n)
# linear time and the two lists are already provided in
# ascending sorted order.


def linear_merge(list1, list2):
    # your code here
    return
