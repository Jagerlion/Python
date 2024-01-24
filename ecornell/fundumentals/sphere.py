# Write your code below:
"""
This is a simple code that calculates the diameter,
circumference, surface area, and volume of a sphere.

Author: Alia Guzman
Date: 01/21/2024
"""
import math

# take the input with the radius
# make it equal to some variable you will use for each formula
radius = float(input("Enter the sphere's radius: "))
#print(radius)

# calculate the diameter first
diameter = 2*radius
print(f'Diameter     : {diameter}')

# calculate the circumference of a sphere
circumference = 2* math.pi*radius
print(f'Circumference: {circumference}')

# calculate the surface area of a sphere
surface_area = 4* math.pi*radius*radius
print(f'Surface area : {surface_area}')

# calculate the volume of a sphere
volume = (4/3)*math.pi*(radius*radius*radius)
print(f'Volume       : {volume}')