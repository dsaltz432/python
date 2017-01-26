#
# CSC161 Fall 2014
#
# Daniel Saltz
#
# Chapter 3, Exercise 15
#
# Lab Section TR 2:00-3:15
#
# Class Section TR 6:15-7:30
import math

def main() :
    print("This program estimates the value of pi.")

    n = eval(input("Enter the number of terms you want to sum: "))
    num = 4
    sum = 0

    for i in range(n + 1):
        sum += num /(2*i + 1)*(-1)**(i)

    closeToPi = math.pi - sum

    if(closeToPi < 0):
        closeToPi *= -1
    
    print("Your estimation was ", closeToPi, "away from the real value of pi")

main()
