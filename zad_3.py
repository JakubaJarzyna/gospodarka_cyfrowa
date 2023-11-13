#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:26:16 2023

@author: nowy
"""

def sprawdz_parzystosc(liczba):
    return liczba % 2

liczba = int(input("Wprowadź liczbę: "))


if sprawdz_parzystosc(liczba) == 0:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
