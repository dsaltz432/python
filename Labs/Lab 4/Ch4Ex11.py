#
# CSC161 Fall 2014
#
# Daniel Saltz
#
# Chapter 4, Exercise 11
#
# Lab Section TR 2:00-3:15
#
# Class Section TR 6:15-7:30


from graphics import *

def main() :
    win = GraphWin("Click Me!")
    
    # Acquiring first 2 clicks from the user
    p1 = win.getMouse()
    p2 = win.getMouse()
    
    # Creating the frame of the house
    house = Rectangle(p1, p2)
    house.draw(win)
    
    # Creating the door
    p3 = win.getMouse()
    p1X = p1.getX()
    p2X = p2.getX()
    houseWidth = p2X - p1X
    doorWidth = houseWidth/5
    doorLeftX = p3.getX() - doorWidth/2 
    doorLeftY = p1.getY()
    doorLeftPoint = Point(doorLeftX, doorLeftY)
    doorRightX = p3.getX() + doorWidth/2 
    doorRightY = p3.getY()
    doorRightPoint = Point(doorRightX, doorRightY)
    door = Rectangle(doorLeftPoint, doorRightPoint)
    door.draw(win)

    # Creating the window
    p4 = win.getMouse()
    windWidth = houseWidth/10
    windLeftX = p4.getX() - windWidth/2 
    windLeftY = p4.getY() - windWidth/2 
    windLeftPoint = Point(windLeftX, windLeftY)
    windRightX = p4.getX() + windWidth/2 
    windRightY = p4.getY() + windWidth/2
    windRightPoint = Point(windRightX, windRightY) 
    wind = Rectangle(windLeftPoint, windRightPoint)
    wind.draw(win)
        
    # Creating the triangular roof
    p5 = win.getMouse()
    leftTriX = p1.getX()
    leftTriY = p2.getY()
    leftPoint = Point(leftTriX, leftTriY)
    door = Polygon(leftPoint, p5, p2)
    door.draw(win)
    
    # Wait to close on mouse click
    win.getMouse()
    win.close()
    
main()

                    