#!/usr/bin/env python

def demande_entier():
    number = int(input("Please enter an integer: "))
    return number

number_1 = demande_entier()
number_2 = demande_entier()

print(f"The sum is: {number_1 + number_2}")

