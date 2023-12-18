#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 10:02:56 2023

@author: nowy
"""

def check_evenness(number):
    return number % 2 == 0

number = int(input("Wprowadź liczbę: "))

if check_evenness(number):
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
