#
# CSC161 Fall 2014
#
# Daniel Saltz
#
# Chapter 8, Exercise 7
#
# Lab Section TR 2:00-3:15
#
# Class Section TR 6:15-7:30


# Determine if the number is prime
def Prime(num): # returns True if it's prime
    num = int(num)
    if num == 2 :
        return True
    elif num < 2 :
        return False
    else :
        for i in range(2, num) :
            if (num % i == 0) :
                return False
        else :
            return True

def main(): 
    # Recieves number from user
    inputNum = int(input("Please enter an even number: "))

    # Makes sure it's an even number
    if inputNum % 2 != 0 : 
        print ("You did not enter an even number.")
        
    # Deals with the exception of the number 2
    elif inputNum == 2 :
        print("The number 2 does not qualify for Goldbach's Conjecture.")
  
    else: 
        for evenNum in range(2, inputNum + 1): 
            if (evenNum != 2) & (evenNum % 2 == 0): # Determines if the number is even
                print(evenNum)
                for x in range(2, evenNum + 1):
                    if Prime(x): # determines if the number is prime
                        for y in range(2, evenNum + 1):
                            if Prime(y):
                                if (x + y == evenNum):                                  
                                    if (x <= y):
                                        print("  ","=", x, "+", y)
                                        
main()