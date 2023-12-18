#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 12:51:57 2023

@author: nowy
"""

def sprawdz_roznice(a, b, c):
    """Zwraca True, jeśli suma a i b jest większa lub równa c."""
    return (a + b) >= c

liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))
liczba3 = int(input("Podaj trzecią liczbę: "))

if sprawdz_roznice(liczba1, liczba2, liczba3):
    print("Suma dwóch pierwszych liczb jest większa lub równa trzeciej liczby.")
else:
    print("Suma dwóch pierwszych liczb jest mniejsza od trzeciej liczby.")
