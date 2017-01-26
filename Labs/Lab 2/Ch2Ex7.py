#
# CSC161 Fall 2014
#
# Daniel Saltz
#
# Chapter 2, Exercise 7
#
# Lab Section TR 2:00-3:15
#
# Class Section TR 6:15-7:30

def main():
    print("This program calculates the future value over 10 years.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    period = eval(input("Enter number of times a year your interest is compounded: "))                            
    realInterest = apr/period

    i = 1
    
    for i in [1,2,3,4,5,6,7,8,9,10]:
        principal = principal * (1 + realInterest)
        print ("The value after", i, "year(s) is: ", principal)

main()

               
