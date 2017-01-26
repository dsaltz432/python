#
# CSC161 Fall 2014
#
# Daniel Saltz
#
# Chapter 7, Exercise 1
#
# Lab Section TR 2:00-3:15
#
# Class Section TR 6:15-7:30

def main() :
    
    hours = float(raw_input("Please enter the weekly hours worked: "))
    overTime = float(raw_input("Please enter the weekly overtime hours worked: "))
    hoursRate = 40
    overTimeRate = 60    
    wage = hours * hoursRate + overTime * overTimeRate
    
    print ("Your weekly wage is ${0:0.2f}".format(wage))
    
main()
    