# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:13:12 2019

@author: Raj Suthar
"""

noOfMilesDriven = float(input("Enter the number of miles traveled : "))
noGallonsUsed = float(input("Enter the amount of gallons used : "))

mpg = noOfMilesDriven / noGallonsUsed

print("Your car's MPG is:"+str(mpg))