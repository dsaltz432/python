#
# CSC161 Fall 2014
#
# Daniel Saltz
#
# Chapter 3, Exercise 1
#
# Lab Section TR 2:00-3:15
#
# Class Section TR 6:15-7:30

import math

def main() :
    print("This program calculates the volume and surface area of a sphere.")
    radius = eval(input("Please enter the radius of the sphere: "))
    volume = 4/(3*math.pi*radius**3)
    area = 4*math.pi*radius**2

    print("The volume and area of the sphere are ", volume, ", ", area, ", respectively.")

main()
