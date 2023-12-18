#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 12:02:23 2023

@author: nowy
"""


def collect_names(number_of_names=5):
    names_list = []

    for i in range(number_of_names):
        name = input(f"Wprowadź imię {i + 1}: ")
        names_list.append(name)

    return names_list

if __name__ == "__main__":
    gathered_names = collect_names()
    print(f"Zebrane imiona: {gathered_names}")
