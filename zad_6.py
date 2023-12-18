#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 13:04:27 2023

@author: nowy
"""

def polacz_i_poteguj(lista1, lista2):
    """Łączy dwie listy, usuwa duplikaty i zwraca nową listę z elementami podniesionymi do trzeciej potęgi."""
    polaczona_lista = list(set(lista1 + lista2))
    lista_wynikow = [element ** 3 for element in polaczona_lista]
    return lista_wynikow

lista_a = [1, 2, 3, 4, 5]
lista_b = [3, 6, 5, 8, 9]

print(polacz_i_poteguj(lista_a, lista_b))
