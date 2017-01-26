"""
-------------------------------
NAME: Daniel Saltz
PROJECT: Project 2
-------------------------------
"""
from time import *
from random import *
from graphics import *

win = GraphWin("Black Jack", 800, 700)
win.setCoords(0, 0, 100, 100)
win.setBackground('#145E14')
playing = False

# Initiating the text that changes as the logic of the game changes
message = Text(Point(50,50), "New Deal?")
message.setSize(36)
message.setTextColor(color_rgb(0,255,0))
message.setFace('arial')
message.setStyle('bold')
message.draw(win)

class Card():
    """ Class for an individual Black Jack playing card. """
    def __init__(self, rank, suit):
        ''' Constructs cards by taking in a rank and suit as parameters. '''
        assert(2 <= rank <= 14), "Improper card rank " + str(rank)
        assert(0 <= suit <= 3), "Improper card suit" + str(suit)
        
        self.rank = rank # 2-14
        self.suit = suit # 0-3
        
    def __str__(self):
        ''' Returns a string representing the card "name". '''
        dictSuit = {0:'Diamonds', 1: 'Hearts', 2: 'Spades', 3: 'Clubs'}
        dictRank = {14: 'Ace', 13: 'King', 12: 'Queen', 11: 'Jack', 10:'10',9:'9',8:'8',7:'7',6:'6',5:'5',4:'4',3:'3',2:'2'}
        cardNameString = dictRank[self.rank] + " of " + dictSuit[self.suit]
        return cardNameString

    def imageIndex(self):
        ''' Given a card's rank and suit, this function returns what 
        should be the index of images[]. This function will be used so that
        if the function returns 4, images[4] should print. '''
        return self.suit + 4*(self.rank - 2)

    def value(self):
        ''' Returns the maximum Black Jack value of the card as determined by
        card's rank. '''
        dictRank = {14:1, 13:7, 12:7, 11:7, 10:7, 9:9, 8:8, 7:7, 6:6, 5:5, 4:4, 3:3, 2:2}
        cardValue = dictRank[self.rank]
        return cardValue   

def testCard():
    """ Runs several tests to ensure that the Card class is working. """ 
    c1 = Card(2,3)
    c1name = str(c1)
    assert(c1name == "2 of Clubs")
    c2 = Card(10,0) 
    c2name = str(c2)
    assert(c2name == "10 of Diamonds")
    c3 = Card(13,2)
    c3name = str(c3)
    assert(c3name == "King of Spades")
    c4 = Card(2,3)
    c4name = str(c4)
    assert(c4name == "2 of Clubs")
    c5 = Card(9,1)
    c5name = str(c5)
    assert(c5name == "9 of Hearts")
testCard()  

class CardStack():
    """ Class to simulate a stack of cards. """
    def __init__(self, cardList):
        """ Initializes the list of cards used to create the stack of cards. """
        self.cardList = cardList

    def count(self):
        """ This function will return an integer representing the CardStack's 
        count in blackjack. It includes an algorithm for determining the proper 
        value of an ace.
        """
        count = 0
        for i in self.cardList :
            c = i
            count += Card.value(c)
        
        a = 0
        # Changes the value of an ace from a 1 to a 6 if doing so keeps the count below 22
        while (a < self.countAces()):
            if count + 6 < 22: 
                count += 6
            a += 1

        return count

    def countAces(self):
        """ This method counts the number of aces in a hand. """
        aces = 0
        for card in self.cardList:
            if card.value() == 1:
                aces += 1
        return aces

    def busted(self):
        ''' Checks to see if a hand is busted. '''
        if CardStack.count(self) > 21:
            return True
        else:
            return False

    def addCard(self, newCard):
        """ Takes in a card as a parameter, and adds it to the list of cards. """
        self.cardList.append(newCard)

    def popCard(self):
        """ Removes and returns the bottom most card from the CardStack. """
        return self.cardList.pop()       
  
def testCardStack_addCard():
    """ Runs several tests to ensure the CardStack.addCard(...) method is
    working correcly. """
    x = [Card(3,3), Card(5,0)]
    y = Card(14,2)
    c = CardStack(x)
    print (c)   
    CardStack.addCard(c,y)
    print (c) 

    p = [Card(2,3), Card(14,0), Card(3,1)]
    y = Card(13,0)
    c = CardStack(p)
    print (c)   
    CardStack.addCard(c,y)
    print (c) 
#testCardStack_addCard()

def testCardStack_count():
    """ Runs several tests to ensure that the CardStack.count() method 
    is working. """
    h1 = CardStack([Card(2,3), Card(10,0), Card(10,1)])
    assert(h1.count() == 16)
    h2 = CardStack([Card(7,3), Card(3,0), Card(14,0), Card(14,1), Card(14,2)])
    assert(h2.count() == 19)
    h3 = CardStack([Card(14,3), Card(14,0), Card(14,1)])
    assert(h3.count() == 21)
    h4 = CardStack([Card(7,3), Card(14,0), Card(2,1)])
    assert(h4.count() == 16)
    h5 = CardStack([Card(2,3), Card(2,0), Card(2,1), Card(12,0), Card(14,3)])
    assert(h5.count() == 20)
testCardStack_count()

def createGUI():
    """ Draws the buttons and text of the interface. """
    # Draws green lines
    bottom = Rectangle(Point(3,45), Point(97,46))
    bottom.setFill(color_rgb(0,200,0))
    top = bottom.clone()
    top.move(0,10)
    top.draw(win)
    bottom.draw(win)

    # Draws blackhawk text
    black = Text(Point(20,90), "BLACK")
    black.setSize(33)
    hawk = Text(Point(33,90), "JACK")
    hawk.setSize(33)
    hawk.setTextColor('red')
    black.draw(win)
    hawk.draw(win)

    # Draws player text
    text = Text(Point(50,30), "PLAYER")
    text.setSize(36)
    text.setStyle('bold')
    text.setTextColor(color_rgb(0,255,0))
    text.setFace('times roman')
    text.draw(win)

    # Draws dealer text
    text = Text(Point(50,80), "DEALER")
    text.setSize(36)
    text.setStyle('bold')
    text.setTextColor(color_rgb(0,255,0))
    text.setFace('times roman')
    text.draw(win)

    # Draw the "Deal" button and text 
    button = Rectangle(Point(2,20), Point(12,24))
    button.setFill('gray')
    button.draw(win)
    text = Text(Point(7,22), "Deal")
    text.setSize(15)
    text.draw(win)

    # Draw the "Stand" button and text 
    button = Rectangle(Point(2,12), Point(12,16))
    button.setFill('gray')
    button.draw(win)
    text = Text(Point(7,14), "Stand")
    text.setSize(15)
    text.draw(win)

    # Draw the "Hit" button and text 
    button = Rectangle(Point(2,4), Point(12,8))
    button.setFill('gray')
    button.draw(win)
    text = Text(Point(7,6), "Hit")
    text.setSize(15)
    text.draw(win)

    # Draw the "Quit" button and text         
    button = Rectangle(Point(2,90), Point(8,94))
    button.setFill('gray')
    button.draw(win)
    text = Text(Point(5,92), "Quit")
    text.setSize(15)
    text.draw(win)

class callButtons:
    """ Contains the function for each button in the program.
    For each button, the function will return True if the button is 
    clicked on, or False if it isn't clicked on. """
    def inQuit(self,x,y):
        return ((x >= 2) & (x <= 8)) & ((y >= 90) & (y <= 94)) 

    def inHit(self,x,y):
        return ((x >= 2) & (x <= 12)) & ((y >= 4) & (y <= 8)) 

    def inStand(self,x,y):
        return ((x >= 2) & (x <= 12)) & ((y >= 12) & (y <= 16)) 

    def inDeal(self,x,y):
        return ((x >= 2) & (x <= 12)) & ((y >= 20) & (y <= 24)) 

class DrawCardsLogic:
    def createDeck(self):
        """ Creates a full deck of cards. It then shuffles the list of cards each
        time the method is invoked """
        for rank in range(2,15):
            for suit in range(0,4):
                card = Card(rank, suit)
                self.deck.append(card)
        shuffle(self.deck)

    def collectImages(self):
        """ Collects the 52 cards from the same location as the python file. """
        for i in range(1,53):
            x = "images/" + str(i) + ".gif"
            y = Image(Point(50,50), x)
            self.images.append(y)
        self.images.reverse()

    def __init__(self):
        """ Invokes callInit(), which initializes all of the instance variables.  """
        DrawCardsLogic.callInit(self)

    def callInit(self):
        """ Initializes all of the instance variables. """
        self.images = []
        DrawCardsLogic.collectImages(self)
        self.hand = []
        self.deck = []
        self.dealer = []
        self.collectPlayer = []
        self.collectDealer = []
        self.moveD = 0
        self.moveP = 0
        self.text5 = ""
        self.moveText = ""
        self.text4 = ""
        self.mText = ""
        self.imageMovePX = -20
        self.imageMovePY = -35
        self.imageMoveDX = -20
        self.imageMoveDY = 17
        self.collectImagesP = []
        self.collectImagesD = []
        self.copyImageP = []
        self.copyImageD = []

        DrawCardsLogic.createDeck(self)
        self.deckStack = CardStack(self.deck)
        self.playerStack = CardStack(self.hand)
        self.dealerStack = CardStack(self.dealer)   

    def drawPlayerCard(self):
        ''' Draws the original card for the player. For each additional card, 
        the image is shifted to the right and then drawn.''' 
        pic = Card.imageIndex(self.hand[-1])
        self.copyImageP = self.images[pic].clone()
        self.copyImageP.move(self.imageMovePX,self.imageMovePY)
        self.copyImageP.draw(win)
        self.imageMovePX += 10
        self.collectImagesP.append(self.copyImageP)

    def drawDealerCard(self):
        ''' Draws the original card for the dealer. For each additional card, 
        the image is shifted to the right and then drawn.''' 
        pic = Card.imageIndex(self.dealer[-1])
        self.copyImageD = self.images[pic].clone()
        self.copyImageD.move(self.imageMoveDX,self.imageMoveDY)
        self.copyImageD.draw(win) 
        self.imageMoveDX += 10
        self.collectImagesD.append(self.copyImageD)

    def unDraw(self):
        """ Undraws each card that is drawn after one hand. """
        for i in self.collectImagesP:
            i.undraw()
        for i in self.collectImagesD:
            i.undraw()

    def addPlayer(self):
        """ Adds a card to the player's hand. """
        card1 = CardStack.popCard(self.deckStack)
        CardStack.addCard(self.playerStack, card1)
        return card1

    def addDealer(self):
        """ Adds a card to the dealer's hand. """
        card3 = CardStack.popCard(self.deckStack)
        CardStack.addCard(self.dealerStack, card3)
        return card3 

    def Deal(self):
        """ Deals 2 cards to the player and one to the dealer. """
        global playing
        message.setText("Hit or Stand?")
        DrawCardsLogic.addPlayer(self)
        DrawCardsLogic.drawPlayerCard(self)
        sleep(.75)
        DrawCardsLogic.addPlayer(self)
        DrawCardsLogic.drawPlayerCard(self)
        sleep(.75)
        DrawCardsLogic.addDealer(self)
        DrawCardsLogic.drawDealerCard(self)
        playing = True

    def Hit(self):
        """ Adds a card to the player's hand, and then draw's it. """
        DrawCardsLogic.addPlayer(self)
        DrawCardsLogic.drawPlayerCard(self)

    def Stand(self):
        """ Adds a card to the dealer's hand, draw's it, then waits .75 of a second. """
        DrawCardsLogic.addDealer(self)
        DrawCardsLogic.drawDealerCard(self)
        sleep(.75)

    def playGame(self):
        """ Executes the logic of the game. The player loses if he goes over 21.
        If the dealer goes over 21, the player wins. If neither go over 21, the highest
        count wins. If it's a tie, they push. """
        global playing
        while True:
            pt = win.getMouse()
            x = pt.getX()
            y = pt.getY()
            z = callButtons()

            if callButtons.inQuit(z,x,y):
                break
            if callButtons.inDeal(z,x,y): 
                DrawCardsLogic.unDraw(self)
                DrawCardsLogic.callInit(self)
                DrawCardsLogic.Deal(self) 
            elif playing:
                if callButtons.inHit(z,x,y):         
                    DrawCardsLogic.Hit(self)
                    if CardStack.busted(self.playerStack):
                        message.setText("You busted. New game?")
                        playing = False

                if playing and callButtons.inStand(z,x,y):  
                    if not CardStack.busted(self.playerStack):      
                        while CardStack.count(self.dealerStack) < 18:
                            DrawCardsLogic.Stand(self) 

                        if CardStack.count(self.dealerStack) > 21:
                            message.setText("The Dealer Busted. You win!")
                        else:
                            if CardStack.count(self.dealerStack) > CardStack.count(self.playerStack):
                                message.setText("Dealer wins! New deal?")

                            elif CardStack.count(self.dealerStack) == CardStack.count(self.playerStack):
                                message.setText("It's a tie! New deal?")
                            else:
                                message.setText("You won! New deal?")
                        playing = False
        return False
            
def main():
    """ Plays Black Jack until the player doesn't want to play anymore. """
    # Creates the GUI
    createGUI()

    # Plays the game, and then closes the window
    x = DrawCardsLogic()
    DrawCardsLogic.playGame(x)
    win.close()
main()