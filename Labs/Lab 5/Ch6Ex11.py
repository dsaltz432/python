#
# CSC161 Fall 2014
#
# Daniel Saltz
#
# Chapter 6, Exercise 11
#
# Lab Section TR 2:00-3:15
#
# Class Section TR 6:15-7:30

def squareEach(nums) :
      
    for i in nums :
        squared = i**2
        print squared
        
def main():
    
    list = [0, 1, 2, 37, 3, 4, 5]
    squareEach(list)
    
main()