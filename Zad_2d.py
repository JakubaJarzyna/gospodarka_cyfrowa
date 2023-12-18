#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 12:10:09 2023

@author: nowy
"""

def print_every_second_number(numbers):
    for i in range(0, len(numbers), 2):
        print(numbers[i])

if __name__ == "__main__":
    number_list = list(range(10))
    print_every_second_number(number_list)
