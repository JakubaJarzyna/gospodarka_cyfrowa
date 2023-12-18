#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 10:00:12 2023

@author: nowy
"""

def multiply(a, b):
    return a * b 

first_number = int(input("Podaj pierwszą liczbę: "))
second_number = int(input("Podaj drugą liczbę: "))
product = multiply(first_number, second_number)
print(f"Iloczyn liczb wynosi: {product}")
