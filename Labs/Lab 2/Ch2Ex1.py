#
# CSC161 Fall 2014
#
# Daniel Saltz
#
# Chapter 2, Exercise 1
#
# Lab Section TR 2:00-3:15
#
# Class Section TR 6:15-7:30


def main():
    print("This program converts degrees Celcius to degrees Fahrenheit.") 
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print ("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()
