#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:34:10 2023

@author: nowy
"""

def sprawdz_roznice(a,b,c):
    return (a+b) >= c

liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))
liczba3 = int(input("Podaj trzecią liczbę: "))

              
if sprawdz_roznice(liczba1, liczba2, liczba3):
    print("Suma dwóch pierwszych liczb jest większa od trzeciej liczby c:")
else:
    print("Suma dwóch pierwszych liczb jest mniejsza od trzeciej liczby :c")
