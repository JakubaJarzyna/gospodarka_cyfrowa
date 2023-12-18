#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 12:47:24 2023

@author: nowy
"""

def sprawdz_czy_parzysta(liczba):
    """Zwraca 0, jeśli liczba jest parzysta, w przeciwnym razie zwraca resztę z dzielenia przez 2."""
    return liczba % 2

liczba = int(input("Wprowadź liczbę: "))

if sprawdz_czy_parzysta(liczba) == 0:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
