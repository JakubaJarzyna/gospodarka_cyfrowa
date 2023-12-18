#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 13:01:48 2023

@author: nowy
"""

def sprawdz_wartosc(lista, wartosc):
    """Zwraca True, jeśli wartość znajduje się w liście."""
    return wartosc in lista

lista = [1, 2, 3, 4, 5]
wartosc = int(input("Wprowadź liczbę do sprawdzenia: "))

if sprawdz_wartosc(lista, wartosc):
    print("Lista zawiera wartość:", wartosc)
else:
    print("Lista nie zawiera wartości:", wartosc)
    