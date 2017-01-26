#
# CSC161 Fall 2014
#
# Daniel Saltz
#
# Chapter 6, Exercise 14
#
# Lab Section TR 2:00-3:15
#
# Class Section TR 6:15-7:30

def sumList(nums) :
    sum = 0   
    for i in nums :
        sum = sum + i
    return sum

def squareEach(nums) :
    counter = 0
    for i in nums :
        squared = i**2
        nums[counter] = squared 
        counter += 1
    return nums

def convert() :
    inFile = open(raw_input ("Enter the file path: "), "r")
    data = inFile.read()
    data = data.split()
    data = [int(i) for i in data] # mapping each item as an int
    squaredList = squareEach(data) # squaring all of the items in the list
    sum = sumList(squaredList) # adding all of the squares together
    print sum
 
def main():
    convert()
    
main()
