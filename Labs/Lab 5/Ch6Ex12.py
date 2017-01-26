#
# CSC161 Fall 2014
#
# Daniel Saltz
#
# Chapter 6, Exercise 12
#
# Lab Section TR 2:00-3:15
#
# Class Section TR 6:15-7:30

def sumList(nums) :
      
    sum = 0    
    for i in nums :
        sum = sum + i
        print sum
        
def main():
    
    list = [0, 1, 1, 3, 4, 5]
    sumList(list)
    
main()