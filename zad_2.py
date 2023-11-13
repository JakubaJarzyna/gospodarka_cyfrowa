#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:05:16 2023

@author: nowy
"""


def mnozenie(a,b):
    return a * b 

first_number = int(input("Podaj pierszą liczbę: "))
second_number = int(input("Podaj drugą liczbę: "))
iloczyn = mnozenie(first_number, second_number)
print("Iloczyn liczb wynosi: ",iloczyn)