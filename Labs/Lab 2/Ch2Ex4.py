#
# CSC161 Fall 2014
#
# Daniel Saltz
#
# Chapter 2, Exercise 4
#
# Lab Section TR 2:00-3:15
#
# Class Section TR 6:15-7:30


def main():
    print("This program prints out temperatures from 0 celsius to 100 celsius.") 

    celsius = 0
    
    for i in range (11):
        fahrenheit = 9/5 * celsius + 32
        print (celsius, "degrees Celsius equals ", fahrenheit, "degrees Fahrenheit.") 
        celsius += 10
main()
