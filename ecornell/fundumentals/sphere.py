"""
This is a simple script that calculates the diameter, circumference,
surface area, and volume of a sphere

Author: Bryan Ruiz
Date: 01/21/2024
"""

import math

radius = float(input('Enter the radius: '))
# print(radius)

diameter = 2*radius
print(f'Diameter     : {diameter}')

circumference = 2*math.pi*radius
print(f'Circumference: {circumference}')

surface_area = 4*math.pi*radius*radius
print(f'Surface area : {surface_area}')

volume = (4/3)*math.pi*(radius*radius*radius)
print(f'Volume       : {volume}')