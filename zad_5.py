#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 10:05:37 2023

@author: nowy
"""


def check_value_in_list(lst, value):
    return value in lst

numbers_list = [1, 2, 3, 4, 5]
value_to_check = int(input("Wprowadź liczbę do sprawdzenia: "))

if check_value_in_list(numbers_list, value_to_check):
    print(f"Lista zawiera wartość: {value_to_check}")
else:
    print(f"Lista nie zawiera wartości: {value_to_check}")
