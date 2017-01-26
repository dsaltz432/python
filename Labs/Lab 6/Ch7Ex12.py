#
# CSC161 Fall 2014
#
# Daniel Saltz
#
# Chapter 7, Exercise 12
#
# Lab Section TR 2:00-3:15
#
# Class Section TR 6:15-7:30

def main() :
    
    # Acquiring date from the user
    dateStr = input("Please enter a date in the form mm/dd/yyyy")
    monthStr, dayStr, yearStr = dateStr.split("/")
    
    # Changing the data from strings to ints
    month, day, year = int(monthStr), int(dayStr), int(yearStr)
       
    valid = True
    leapYear = False
    
    # Determining if it's a leap year
    if (year % 4 == 0) & (year % 100 == 0) & (year % 400 == 0) :
        leapYear = True    
    
    if (month == 1)|(month == 3)|(month == 5)|(month == 7)|(month == 8)|(month == 10)|(month == 12):
        if day > 31 :
            valid = False
    elif (month == 4)|(month == 6)|(month == 9)|(month == 11):
        if day > 30 :
            valid = False 
    elif month == 2 :
        if leapYear == True :
            if day > 28 :
                valid = False            
        elif day > 29 :
            valid = False
      
    # Printing out the results
    if (year > 2014) & (valid == True):
        print ("You entered a valid date in the future.") 
    elif (valid == True) :
        print ("You entered a valid date.")
    else :
        print ("You entered an invalid date.")
        
main()
    