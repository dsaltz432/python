#
# CSC161 Fall 2014
#
# Daniel Saltz
#
# Chapter 3, Exercise 17
#
# Lab Section TR 2:00-3:15
#
# Class Section TR 6:15-7:30

import math

def main() :
    print("This program estimates the value of a square root.")

    x = float(input("Enter the number of which you want to find the square root: "))
    numGuess = int(input("Enter the number guesses you want the computer to make: "))
    firstGuess = x/2

    newGuess = (firstGuess + (x/firstGuess))/2
    newGuessValue = newGuess
                 
    for i in range(numGuess):
        newGuess= (newGuessValue + (x/newGuessValue))/2
        newGuessValue = newGuess

    realSqrt = math.sqrt(x)  
    closeToReal = realSqrt - newGuess
    
    if (closeToReal < 0) :
        closeToReal *= -1    
    
    print("Your estimation was ", closeToReal, "away from the real square root value")

main()
