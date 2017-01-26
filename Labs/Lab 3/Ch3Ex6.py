#
# CSC161 Fall 2014
#
# Daniel Saltz
#
# Chapter 3, Exercise 6
#
# Lab Section TR 2:00-3:15
#
# Class Section TR 6:15-7:30

def main() :
    print("This program calculates the slope of a line given two points.")

    x1, y1 = eval(input("Enter the first x and y coordinates separated by a comma: "))
    x2, y2 = eval(input("Enter the second x and y coordinates separated by a comma: "))   

    num = y2 - y1
    denom = x2 - x1
    slope = num/denom

    print("The slope of the line is: ", slope)

main()
