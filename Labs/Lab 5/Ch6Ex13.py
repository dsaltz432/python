#
# CSC161 Fall 2014
#
# Daniel Saltz
#
# Chapter 6, Exercise 13
#
# Lab Section TR 2:00-3:15
#
# Class Section TR 6:15-7:30

def toNumbers(strList) :
    
    numList = strList
    count = 0
    
    for i in strList :
        i = count
        count += 1
        numList[i] = count
    print numList 
    
def main():
    
    list = ["The","Dog","twelve","grass","ball", ""]
    toNumbers(list)
    
main()