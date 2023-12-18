#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 12:44:59 2023

@author: nowy
"""

def mnozenie(a, b):
    """Funkcja do mnożenia dwóch liczb."""
    return a * b 

first_number = int(input("Podaj pierwszą liczbę: "))
second_number = int(input("Podaj drugą liczbę: "))
iloczyn = mnozenie(first_number, second_number)

print("Iloczyn liczb wynosi:", iloczyn)