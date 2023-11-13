#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 13:02:22 2023

@author: nowy
"""

def polacz_i_poteguj(list1, list2):
    polaczona_lista = list(set(list1 + list2))
    lista_wynikow = [element ** 3 for element in polaczona_lista]
    return lista_wynikow


lista_a = [1, 2, 3, 4, 5]
lista_b = [3, 6, 5, 8, 9]


print(polacz_i_poteguj(lista_a, lista_b))
