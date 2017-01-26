#
# CSC161 Fall 2014
#
# Daniel Saltz
#
# Chapter 2, Exercise 9
#
# Lab Section TR 2:00-3:15
#
# Class Section TR 6:15-7:30

def main():
    print("This program distances measured in kilometers to miles.")

    kilometers = eval(input("Please enter a distance measured in kilometers: "))
    miles = .62 * kilometers

    print(kilometers, "kilometers is equal to ", miles, "miles.")

main()

               
