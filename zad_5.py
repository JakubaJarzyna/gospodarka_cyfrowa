#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:54:56 2023

@author: nowy
"""

def sprawdz_wartosc(lista, wartosc):
    return wartosc in lista

lista = [1, 2, 3, 4, 5]
wartosc_int = int(input("Wprowadź liczbę do sprawdzenia: "))

# czy_zawiera = sprawdz_wartosc(lista, wartosc_int)
if sprawdz_wartosc(lista, wartosc_int):
    print("Lista zawiera wartość : ", wartosc_int)
else:
    print("Lista nie zawiera wartości : ", wartosc_int)