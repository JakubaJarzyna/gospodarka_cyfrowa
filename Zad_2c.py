#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 12:09:07 2023

@author: nowy
"""

def print_even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)

if __name__ == "__main__":
    number_list = list(range(10))
    print_even_numbers(number_list)

