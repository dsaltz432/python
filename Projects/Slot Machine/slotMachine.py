"""
-------------------------------
NAME: Daniel Saltz
PROJECT: Project1
-------------------------------
"""

from graphics import *
from random import *

win = GraphWin("Slot Machine", 600, 600)
win.setCoords(0, 0, 100, 100)

# Creating shapes that change color
circle = Circle(Point(40,35),5) 
rect = Rectangle(Point(57,30), Point(67,40)) 
tri = Polygon(Point(80,30), Point(85,40), Point(90,30)) 

# Determines if the click is on the button. Returns True if the button is clicked
# This function takes the x and y coordinates of the mouse click as parameters
def inButton(x,y) :        
    return ((x >= 4) & (x <= 16)) & ((y >= 29) & (y <= 41))  

# Creates the spin button, spin text
def CreateBackground() : 
    button = Rectangle(Point(4,29), Point(16,41))
    button.setFill('red')
    button.draw(win)
    rectOutline = Rectangle(Point(29,10), Point(95,60))
    rectOutline.draw(win)
    Line(Point(51,10), Point(51,60)).draw(win)
    Line(Point(73,10), Point(73,60)).draw(win)
    spinText = Text(Point(10,35), "Spin")
    spinText.setSize(18)
    spinText.draw(win)

# This function is looped in main(), and executes as long as the user hasn't lost
# The two parameters are strings of the bet and the balance. They will later be
# converted to floats  
def Spin(betInput, balanceText) :
    pt = win.getMouse()
    x = pt.getX()
    y = pt.getY()
    bet = float(betInput.getText())
    bal = float(BalanceExtract(balanceText.getText()))
    colors = ['cyan', 'sea green', 'firebrick', 'yellow','deep pink', 'blue violet']
    count = 0

    if inButton(x,y) :
        if bet < 0 :
            print("You're bet must be a positive number.")
        elif bet > bal :
            print("You have insufficient funds. Please enter smaller bet.")
        else:    
            while count < 20 : # This shuffles the colors of the shapes
                # Assigns random colors
                colorC = choice(colors)
                colorR = choice(colors)
                colorT = choice(colors)
                    
                # Fills shapes with random colors
                circle.setFill(colorC)
                rect.setFill(colorR)  
                tri.setFill(colorT)
                count += 1           
            if (colorC == colorR == colorT) :
                a = bal + bet
                balanceText.setText(("Balance: ${0:0.2f}").format(a))
            elif ((colorC == colorR) | (colorC == colorT) | (colorT == colorR)):
                a = bal + bet/2
                balanceText.setText(("Balance: ${0:0.2f}").format(a))
            else :
                a = bal - bet
                balanceText.setText(("Balance: ${0:0.2f}").format(a)) 
                if a == 0 :
                    return False # User has lost the game, stops the loop in main()
    return True           


# Accepts a string from the function CreateBalance() 
# The string will look something like "Balance: $100.00"
# This function extracts all of the values after the character "$"
# Returns a string that is later converted to a float
def BalanceExtract(string) :
    num = ""
    addMore = False
    for i in string :
        if addMore:
            num += i
        if i == "$" :
            addMore = True          
    return num

# Creates text on the window with an initial value of "Balance: $100.00"
# Returns the text as a string
def CreateBalance() :
    balance = 100 
    balanceString = ("Balance: ${0:0.2f}").format(balance)
    balanceText = Text(Point(15,90), balanceString)
    balanceText.setSize(17)
    balanceText.draw(win)
    return balanceText

# Creates text followed by an entry box with the initial value of "0.00"
# Returns a string of what the user enters as their bet
def CreateBet() :      
    betString = ("Bet:  $")
    betText = Text(Point(8,83), betString)
    betText.setSize(17)
    betText.draw(win)    
    betInput = Entry(Point(17,83), 5) 
    betInput.setText("0.00")
    betInput.draw(win)
    return betInput   
     

# Draws the 3 shapes that change color
# Loops through the Spin() function, until the user reaches a balance of $0
# Handles a ValueError, if the user tries to type in a string as a bet
# Once the user loses the game, the window becomes red, and an error message appears
# One more click closes the window
def main() :
    circle.draw(win)
    rect.draw(win)
    tri.draw(win)
    CreateBackground() 
    bt = CreateBalance()
    bi = CreateBet()
    alive = True

    while (alive): 
        try:      
            alive = Spin(bi, bt)
        except ValueError: 
            print ("You must enter a number.")

    win.setBackground('red')
    loseText = Text(Point(50,90), "You Lose")
    loseText.setSize(23)
    loseText.draw(win)


    win.getMouse()
    win.close()     
               
main()