#
# CSC161 Fall 2014
#
# Daniel Saltz
#
# Chapter 5, Exercise 9
#
# Lab Section TR 2:00-3:15
#
# Class Section TR 6:15-7:30

def main() :
    sentence = raw_input("Please enter a sentence: ")
    sentence = sentence.split()
    count = 0
    
    for i in sentence :
        count += 1
    print count
    
main()