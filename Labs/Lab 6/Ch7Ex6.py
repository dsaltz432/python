#
# CSC161 Fall 2014
#
# Daniel Saltz
#
# Chapter 7, Exercise 6
#
# Lab Section TR 2:00-3:15
#
# Class Section TR 6:15-7:30

def main() :
    
    speed = float(raw_input("Please enter a speed: "))
    speedLimit = float(raw_input("Please enter a speed limit: "))
     
    initial = 50
    addFine = 0  
    
    speedCounter = speed
        
    addSome = 0   
    while speedCounter > speedLimit :
        speedCounter -= 1
        addSome += 5
    
    if speed <= speedLimit :
        print "You are driving legally"
        
    elif speed > 90 :
        addFine += 200       
        
    fine = initial + addSome + addFine
    print ("Your fine is ${0:0.2f}".format(fine))
    
main()
    