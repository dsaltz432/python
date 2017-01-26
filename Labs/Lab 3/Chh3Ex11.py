#
# CSC161 Fall 2014
#
# Daniel Saltz
#
# Chapter 3, Exercise 11
#
# Lab Section TR 2:00-3:15
#
# Class Section TR 6:15-7:30

def main() :
    print("This program calculates the sum of the first n natural numbers, given n.")

    n = eval(input("Enter the value for n: "))
    sum = 0

    for i in range(n + 1):
        sum += i

    print("The sum is: ", sum)

main()
