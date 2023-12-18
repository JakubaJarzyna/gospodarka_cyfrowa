#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 10:04:16 2023

@author: nowy
"""

def check_sum_greater_than_third(a, b, c):
    return (a + b) >= c

number1 = int(input("Podaj pierwszą liczbę: "))
number2 = int(input("Podaj drugą liczbę: "))
number3 = int(input("Podaj trzecią liczbę: "))

if check_sum_greater_than_third(number1, number2, number3):
    print("Suma dwóch pierwszych liczb jest większa bądź równa trzeciej liczbie.")
else:
    print("Suma dwóch pierwszych liczb jest mniejsza od trzeciej liczby.")
