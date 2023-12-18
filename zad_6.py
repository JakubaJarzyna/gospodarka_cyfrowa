#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 10:08:11 2023

@author: nowy
"""


def combine_and_cube(list1, list2):
    combined_list = list(set(list1 + list2))
    cubed_results = [element ** 3 for element in combined_list]
    return cubed_results

list_a = [1, 2, 3, 4, 5]
list_b = [3, 6, 5, 8, 9]

print(combine_and_cube(list_a, list_b))
