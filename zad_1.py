#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 12:17:59 2023

@author: nowy
"""

class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return sum(self.marks) / len(self.marks) > 50


student1 = Student("Jan Kowalski", [60, 70, 80])  
student2 = Student("Anna Nowak", [40, 40, 40])  


print(f"{student1.name} zaliczył/a: {student1.is_passed()}") 
print(f"{student2.name} zaliczył/a: {student2.is_passed()}") 
