#
# CSC161 Fall 2014
#
# Daniel Saltz
#
# Lab 9
#
# Lab Section TR 2:00-3:15
#
# Class Section TR 6:15-7:30

def sumList(lst):
   if len(lst) == 1:
        return lst[0]
   else:
        return lst[0] + sumList(lst[1:])

def test():
	print(sumList([7, 5, 4, 27, 52, 42, 13, 17]))
test()
