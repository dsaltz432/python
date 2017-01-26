#
# CSC161 Fall 2014
#
# Daniel Saltz
#
# Chapter 2, Exercise 11
#
# Lab Section TR 2:00-3:15
#
# Class Section TR 6:15-7:30

def main():
    print("This program is a simple interactive calculator.")

    for i in range(100):
        input1 = eval(input("Enter a mathematical expression: "))
        print ("The answer to your expression is: ", input1)

main()

               
