# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:19:50 2019

@author: Raj Suthar
"""

"""(value°F − 32) × 5/9"""


fahrenheit = float(input("Enter the values of temprature in fahrenheit to convert into celsius : "))

celsius = (fahrenheit-32) * (5/9);

print(str(fahrenheit) +" fahrenheit is equals to " + str(celsius) +" celsius")