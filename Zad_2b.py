#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 12:05:35 2023

@author: nowy
"""


def multiply_by_2_v1(numbers):
    for i in range(len(numbers)):
        numbers[i] *= 2
    return numbers

def multiply_by_2_v2(numbers):
    return [x * 2 for x in numbers]

number_list = [1, 2, 3, 4, 5]
print(f"Oryginalna lista: {number_list}")

result_v1 = multiply_by_2_v1(number_list.copy())  # Use .copy() to avoid modifying the original list
print(f"Wynik z użyciem pętli for: {result_v1}")

result_v2 = multiply_by_2_v2(number_list)
print(f"Wynik z użyciem listy składowej: {result_v2}")
