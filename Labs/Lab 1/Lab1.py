#
# CSC161 Fall 2014
#
# Daniel Saltz
#
# Chapter 1, Exercise 5
#
# Lab Section TR 2:00-3:15
#
# Class Section TR 6:15-7:30




def main():
    print ("This program illustrates a chatoic function")
    n = eval(input("How many numbers should I print?"))
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(n):
        x = 2.0 * x * (1 - x)
        print(x) 

main()


