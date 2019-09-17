# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 14:46:43 2019

@author: Raj Suthar
"""
import math

radius = float(input('Enter the radius of circle to find it\'s area:' ))
area = math.pi*(radius**2)

print('Area of the circle having the radius '+str(radius)+' is '+str(area))