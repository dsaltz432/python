#
# CSC161 Fall 2014
#
# Daniel Saltz
#
# Chapter 3, Exercise 7
#
# Lab Section TR 2:00-3:15
#
# Class Section TR 6:15-7:30

import math

def main() :
    print("This program calculates the slope of a line given two points.")

    x1, y1 = eval(input("Enter the first x and y coordinates separated by a comma: "))
    x2, y2 = eval(input("Enter the second x and y coordinates separated by a comma: "))   

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    print("The distance bewteen the two lines is: ", distance)

main()
