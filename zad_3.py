#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 09:54:43 2023

@author: nowy
"""

class Property:

    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

class House(Property):

    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot
    
    def __str__(self):
        return (f"Dom: Powierzchnia: {self.area} m², Pokoje: {self.rooms}, "
                f"Cena: {self.price} PLN, Adres: {self.address}, "
                f"Działka: {self.plot} m²")

class Flat(Property):

    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor
    
    def __str__(self):
        return (f"Mieszkanie: Powierzchnia: {self.area} m², Pokoje: {self.rooms}, "
                f"Cena: {self.price} PLN, Adres: {self.address}, Piętro: {self.floor}")

house = House(120, 5, 300000, "ul. Kwiatowa 10, 00-001 Warszawa", 800)
flat = Flat(70, 3, 200000, "ul. Słoneczna 5/10, 31-002 Kraków", 3)

print(house)
print(flat)
