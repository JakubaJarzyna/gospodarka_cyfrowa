#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 12:18:40 2023

@author: nowy
"""

class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Biblioteka w {self.city}, ul. {self.street}, {self.zip_code}, Godziny otwarcia: {self.open_hours}, Telefon: {self.phone}"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Pracownik: {self.first_name} {self.last_name}, Data zatrudnienia: {self.hire_date}, Data urodzenia: {self.birth_date}, Adres: {self.city}, ul. {self.street}, {self.zip_code}, Telefon: {self.phone}"


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Książka autorstwa {self.author_name} {self.author_surname}, Data publikacji: {self.publication_date}, Liczba stron: {self.number_of_pages}, Dostępna w: {self.library}"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = ", ".join(str(book) for book in self.books)
        return f"Zamówienie złożone przez: {self.student}, Obsługiwane przez: {self.employee}, Data zamówienia: {self.order_date}, Książki w zamówieniu: {books_str}"


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}"


library1 = Library("Warszawa", "Marszałkowska", "00-001", "9-17", "22 123 45 67")
library2 = Library("Kraków", "Floriańska", "31-019", "10-18", "12 345 67 89")

book1 = Book(library1, "2001-01-01", "Jan", "Kowalski", 300)
book2 = Book(library1, "2002-02-02", "Anna", "Nowak", 250)
book3 = Book(library2, "2003-03-03", "Piotr", "Wiśniewski", 200)
book4 = Book(library2, "2004-04-04", "Katarzyna", "Maj", 350)
book5 = Book(library2, "2005-05-05", "Andrzej", "Dąbrowski", 150)

employee1 = Employee("Marek", "Zieliński", "2010-06-01", "1985-01-01", "Warszawa", "Marszałkowska", "00-001", "22 987 65 43")
employee2 = Employee("Joanna", "Kwiatkowska", "2012-07-01", "1987-02-02", "Kraków", "Floriańska", "31-019", "12 876 54 32")
employee3 = Employee("Tomasz", "Kaczmarek", "2014-08-01", "1989-03-03", "Warszawa", "Marszałkowska", "00-001", "22 765 43 21")

student1 = Student("Lukasz", "Borowicz")
student2 = Student("Magdalena", "Kowalska")
student3 = Student("Karol", "Nowak")

order1 = Order(employee1, student1, [book1, book2], "2023-03-15")
order2 = Order(employee2, student2, [book3, book4, book5], "2023-03-16")


print(order1)
print(order2)
