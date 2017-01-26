#
# CSC161 Fall 2014
#
# Daniel Saltz
#
# Chapter 5, Exercise 4
#
# Lab Section TR 2:00-3:15
#
# Class Section TR 6:15-7:30

def main() :
    
    s = raw_input("Please enter a string: ")
    s = s.title()
    s = s.split()
    x = ""
    
    for i in s :
        x = x + i[0]
    print x
    
main()