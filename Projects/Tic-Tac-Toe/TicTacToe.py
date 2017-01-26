from graphics import *
import time
from random import *

playAsO = False
playAsX = True
Hard = True
Medium = False
Easy = False
drawnX = True
drawnO = False


win = GraphWin("Tic-Tac-Toe", 700,500)
win.setCoords(0, 0, 100, 100)

class Board:
	""" This class holds the state information for a game of TicTacToe 
	as well as provides methods to add a move and determine a winner. Each
	of the squares on the Tic-Tac-Tow board are labeled with a number 1-9.
	The figure below shows the board labeling used. 

        1|2|3
        -----
        4|5|6
        -----
        7|8|9

    Attributes:
      movesList - a growing list of squares picked by the players on their
                   turn in the order they were picked. Thus, the first list
                   element is always the square where X first went, the second
                   list element is always where O went after X, etc. In other 
                   words, the even indexed elements are X's moves, the
                   odd indexed elements are O's moves. When the list has
                   9 elements, the game board must be full.
    """

	def __init__(self):
		self.movesList = []
		self.remainingList = [1,2,3,4,5,6,7,8,9]
		self.wins = 0
		self.losses = 0
		self.ties = 0

	def restart(self):
		""" Assing the wins, losses and ties to their initial state"""
		self.movesList = []
		self.wins = 0
		self.losses = 0
		self.ties = 0

	def TryMove(self, squareNum):
		""" Checks if squareNum is a valid move and if so adds it to 
        movesList.
        Returns 0 if valid move, 1 otherwise. """

		assert(1 <= squareNum <= 9)
		# if the picked square has not previously been picked
		if (not squareNum in self.movesList): 
			self.movesList.append(squareNum)
			return 0 # signify valid move
		else:
			return 1 # signify illegal move, list not updated

	def MoveCount(self):
		"""Returns the number of squares which have been played on. """
		return len(self.movesList)

	def IsWin(self):
		""" Returns 0 if no winner, 1 if X wins, 2 if O wins,
		0 if  the game continues """
		# winning combos are: 123, 456, 789, 147, 258, 369, 159, 357
		winningSets = ({1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},
						{1,5,9},{3,5,7})
		xSquares = set(self.movesList[::2])  #even indexed squares
		oSquares = set(self.movesList[1::2]) #odd indexed squares
		for winningSet in winningSets:
			if winningSet.issubset(xSquares): #does X have this winning combo?
				return 1
			elif winningSet.issubset(oSquares): #does O have this winning combo?
				return 2
				
		if (self.MoveCount() == 9): # tie
			return 3
		else:
			return 0 # keep playing
			
	def GetRemainingSquares(self):
		""" Returns list of squares which have not been played on. """
		return list(set(range(1,10)) - set(self.movesList))

class Game:
	""" Creates and updates the data for the board""" 
	def __init__(self):
		self.b = Board()
		self.buttonList = []
		for square in range(0, 9):
			newButton =  Button(square)
			self.buttonList.append(newButton)
		self.wins, self.losses, self.ties = 0,0,0        
		self.state = 0
		self.collectXPlayed, self.collectOPlayed = [],[]

	def resetBoard(self):
		self.b = Board()      
		self.state = 0
		self.unDraw()

	def noScores(self):
		""" Reinitializes the data """
		self.wins, self.losses, self.ties = 0,0,0     

	def unDraw(self):
		""" Collects all of the X's and O's that have been played 
		and erases them """ 
		for i in self.collectXPlayed:
			self.buttonList[i].X1.undraw()
			self.buttonList[i].X2.undraw()

		for i in self.collectOPlayed:
			self.buttonList[i].O.undraw()

	def chooseSide(self, xORo, GUIInstance):
		""" Determines if the user wants to be an X or an O """ 
		global playAsX, playAsO
		x = xORo.getX()
		y = xORo.getY()  
		if 92 < x < 98 and 65 < y < 72: # Clicked on X button
			GUIInstance.checkX()
			playAsO = False
			return 1

		elif 82 < x < 88 and 65 < y < 72: # Clicked on O button
			GUIInstance.checkO()
			playAsO = True
			return 1
		else:
			return 0

	def selectX(self):
		""" Determines if the user clicks in the X box"""
		return 92 < x < 98 and 65 < y < 72 # Clicked on X button

	def selectO(self):
		""" Determines if the user clicks in the O box"""
		return 82 < x < 88 and 65 < y < 72 # Clicked on X button

	def drawSquare(self, squareNum):
		""" Draws the appropriate squares given that the user selects X or O.
		If the user doesn't select a box and just starts playing, the default setting
		has the user playing as an X. """ 
		global playAsX, playAsO
		xClicked = True
		oClicked = False

		if playAsO:
			oClicked = True
			xClicked = False

		if self.b.MoveCount() == 1: # Determines what to do for the first move
			if xClicked: # User chose X, or was chosen by default
				self.buttonList[squareNum-1].X1.draw(win)
				self.buttonList[squareNum-1].X2.draw(win)
				self.collectXPlayed.append(squareNum-1)
				self.state += 1
			else: # User chose O
				self.buttonList[squareNum-1].O.draw(win)
				self.collectOPlayed.append(squareNum-1)
				self.state += 2

		else: # Determines what to do for all moves except the first move
			if self.state % 2 == 0:
				self.buttonList[squareNum-1].X1.draw(win)
				self.buttonList[squareNum-1].X2.draw(win)
				self.collectXPlayed.append(squareNum-1)
				self.state += 1
			else:
				self.buttonList[squareNum-1].O.draw(win)
				self.collectOPlayed.append(squareNum-1)
				self.state += 1

	def Winner(self):
		""" Increments the values """ 
		if self.b.IsWin() == 0:
			return self.b.IsWin()
		elif self.b.IsWin() == 1:
			self.wins += 1
		elif self.b.IsWin() == 2:
			self.losses += 1
		else:
			self.ties += 1

	def getNewWins(self):
		self.noScores()
		return self.wins

	def getNewLosses(self):
		self.noScores()
		return self.losses

	def getNewTies(self):
		self.noScores()
		return self.ties

	def getWins(self):
		return self.wins

	def getLosses(self):
		return self.losses

	def getTies(self):
		return self.ties

	def drawClick(self, click):
		"""Draws the object when the square is clikced on """
		x = click.getX()
		y = click.getY()

		if ((x >= 10) & (x <= 28)) & ((y >= 74) & (y <= 95)) and self.b.TryMove(1) == 0:  
			Game.drawSquare(self,1)
			self.b.remainingList.remove(1)
		elif ((x >= 30) & (x <= 51)) & ((y >= 74) & (y <= 95)) and self.b.TryMove(2) == 0:
			Game.drawSquare(self,2)
			self.b.remainingList.remove(2)
		elif ((x >= 53) & (x <= 70)) & ((y >= 74) & (y <= 95)) and self.b.TryMove(3) == 0:
			Game.drawSquare(self,3)
			self.b.remainingList.remove(3)
		elif ((x >= 10) & (x <= 28)) & ((y >= 49) & (y <= 72)) and self.b.TryMove(4) == 0:
			Game.drawSquare(self,4)
			self.b.remainingList.remove(4)
		elif ((x >= 30) & (x <= 51)) & ((y >= 49) & (y <= 72)) and self.b.TryMove(5) == 0:
			Game.drawSquare(self,5)
			self.b.remainingList.remove(5)
		elif ((x >= 53) & (x <= 70)) & ((y >= 49) & (y <= 72)) and self.b.TryMove(6) == 0:
			Game.drawSquare(self,6)
			self.b.remainingList.remove(6)
		elif ((x >= 10) & (x <= 28)) & ((y >= 25) & (y <= 47)) and self.b.TryMove(7) == 0: 
			Game.drawSquare(self,7)
			self.b.remainingList.remove(7)
		elif ((x >= 30) & (x <= 51)) & ((y >= 25) & (y <= 47)) and self.b.TryMove(8) == 0:
			Game.drawSquare(self,8)
			self.b.remainingList.remove(8)
		elif ((x >= 53) & (x <= 70)) & ((y >= 25) & (y <= 47)) and self.b.TryMove(9) == 0:
			Game.drawSquare(self,9)
			self.b.remainingList.remove(9)

	def checkIfClicked(self, click):
		x = click.getX()
		y = click.getY()

		if ((x >= 10) & (x <= 28)) & ((y >= 74) & (y <= 95)):  
			return True
		elif ((x >= 30) & (x <= 51)) & ((y >= 74) & (y <= 95)):
			return True
		elif ((x >= 53) & (x <= 70)) & ((y >= 74) & (y <= 95)):
			return True
		elif ((x >= 10) & (x <= 28)) & ((y >= 49) & (y <= 72)):
			return True
		elif ((x >= 30) & (x <= 51)) & ((y >= 49) & (y <= 72)):
			return True
		elif ((x >= 53) & (x <= 70)) & ((y >= 49) & (y <= 72)):
			return True
		elif ((x >= 10) & (x <= 28)) & ((y >= 25) & (y <= 47)): 
			return True
		elif ((x >= 30) & (x <= 51)) & ((y >= 25) & (y <= 47)):
			return True
		elif ((x >= 53) & (x <= 70)) & ((y >= 25) & (y <= 47)):
			return True

	def randomAI(self):
		""" Randomly generates a move for the computer to make,
		based on what moves are available """ 
		computerChoice = choice(self.b.remainingList)
		self.b.movesList.append(computerChoice)
		Game.drawSquare(self, computerChoice)
		self.b.remainingList.remove(computerChoice)

	def perfectAI(self):
		if self.computerCanWin():
			#print("win")
			pass
		elif self.needToBlock():
			#print("blocked")
			pass
		#elif self.blockScenario2():
		#	print("weird middle2")
		#	#pass
		elif self.blockScenario():
			#print("weird middle")
			pass

		elif self.goToCorner():
			#print("corner")
			pass
		elif self.pickMiddle():
			#print("middle")
			pass
		else:
			#print("random")
			self.randomAI()

	def mediumAI(self):
		prob = .8
		result  = random()
		# print result
		if prob > result:
			self.perfectAI()
		else:
			self.randomAI()

	def blockScenario(self):
		''' This function handles the following scenario:

			The user has played 3 moves. One has been to a corner,
			and and the two other moves have been in the opposite 
			middle spaces from the corner move (not the actual middle).
			The computer will want to move to another corner, but 
			doing so will allow the user to win. Instead, the computer
			needs to be programmed to move to the middle in this 
			circumstance, which is the perfect move in this scenario.
		''' 

		trickySets = ({1,6,8},{3,4,8},{9,4,2},{7,6,2})
		checkList = self.b.movesList[::2]
		found = False

		if len(checkList) == 3:
			# print("hi")
			for i in trickySets:
				# print i
				if i.issubset(set(checkList)):
					computerChoice = 5
					found = True 
		if found:
			self.b.movesList.append(computerChoice)
			Game.drawSquare(self, computerChoice)
			self.b.remainingList.remove(computerChoice)
		return found	

	def blockScenario2(self):
		''' This function handles the following scenario:

			The user has played two moves. One has been to a middle space,
			but not the actual middle. The other move has to be to the
			middle space nearest the first move. The perfect move for
			the computer in this scenario is to move to the middle.
		''' 
		trickySets = ({2,6},{6,8},{8,4},{4,2})
		checkList = self.b.movesList[::2]
		found = False

		if len(checkList) == 2:
			for i in trickySets:
				if i.issubset(set(checkList)):
					computerChoice = 5
					found = True 
		if found:
			self.b.movesList.append(computerChoice)
			Game.drawSquare(self, computerChoice)
			self.b.remainingList.remove(computerChoice)
		return found

	def blockScenario3(self):
		''' This function handles the following scenario:

			The user has played two moves. One has been to a middle space,
			but not the actual middle. The other move has to be to the
			middle space nearest the first move. The perfect move for
			the computer in this scenario is to move to the middle.
		''' 
		trickySets = ({2,6},{6,8},{8,4},{4,2})
		checkList = self.b.movesList[::2]
		found = False

		if len(checkList) == 2:
			for i in trickySets:
				if i.issubset(set(checkList)):
					computerChoice = 5
					found = True 
		if found:
			self.b.movesList.append(computerChoice)
			Game.drawSquare(self, computerChoice)
			self.b.remainingList.remove(computerChoice)
		return found

	def goToCorner(self):
		""" Forces the computer to move to a corner """
		remainingSet = set(self.b.remainingList)
		cornersList = [1,3,7,9]
		cornersSet = set(cornersList)
		found = False
		sameList = []

		for i in remainingSet:
			for j in cornersSet:
				if j == i:
					sameList.append(i)
		if len(sameList) != 0:
			computerChoice = choice(sameList)
			sameList.remove(computerChoice)
			found = True
		if found:
			self.b.movesList.append(computerChoice)
			Game.drawSquare(self, computerChoice)
			self.b.remainingList.remove(computerChoice)
		return found

	def pickMiddle(self):
		found = False
		for i in self.b.remainingList:
			if i == 5:
				computerChoice = i
				found = True
		if found:
			self.b.movesList.append(computerChoice)
			Game.drawSquare(self, computerChoice)
			self.b.remainingList.remove(computerChoice)
		return found	

	def computerCanWin(self):
		""" Forces the computer play a winning move, if possible """
		winningSets = ({1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},
						{1,5,9},{3,5,7})
		checkList = self.b.movesList[1::2]
		found = False

		''' This will be implemented once X always goes first
		global playAsX, playAsO
		xClicked = True
		oClicked = False
		xSquares = self.b.movesList[::2] 
		oSquares = self.b.movesList[1::2] 
		checkList = []
		if playAsO: # Determines which shape the computer should block against
			checkList = xSquares
		else:
			checkList = oSquares
		'''

		for i in self.b.remainingList:
			checkList.append(i)
			for j in winningSets:
				if j.issubset(set(checkList)):
					computerChoice = i
					found = True
					break
			if found == True:
				break
			else:
				checkList.remove(i)
		if found:
			self.b.movesList.append(computerChoice)
			Game.drawSquare(self, computerChoice)
			self.b.remainingList.remove(computerChoice)
		return found	

	def needToBlock(self):
		""" Forces the computer to block a user from winning """
		winningSets = ({1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},
						{1,5,9},{3,5,7})
 		checkList = self.b.movesList[::2]
		found = False

 		''' This will be implemented once X always goes first
		global playAsX, playAsO
		checkList = []
		xClicked = True
		oClicked = False
		oSquares = self.b.movesList[::2] 
		xSquares = self.b.movesList[1::2]

		if playAsO: # Determines which shape the computer should block against
			checkList = xSquares
		else:
			checkList = oSquares
		'''

		for i in self.b.remainingList:
			checkList.append(i)
			for j in winningSets:
				if j.issubset(set(checkList)):
					computerChoice = i
					found = True
					break
			if found == True:
				break
			else:
				checkList.remove(i)
		if found:
			self.b.movesList.append(computerChoice)
			Game.drawSquare(self, computerChoice)
			self.b.remainingList.remove(computerChoice)
		return found

def test_board():
    """ Performs some simple testing of the Board class """
    b = Board()
    assert( not b.TryMove(1) )
    assert( b.TryMove(1) )
    assert( not b.IsWin() )
    assert( not b.TryMove(4) )
    assert( not b.IsWin() )
    assert( not b.TryMove(2) )
    assert( not b.IsWin() )
    assert( not b.TryMove(5) )
    assert( not b.IsWin() )
    assert( not b.TryMove(3) )
    assert( b.IsWin() == 1 )
    print("test_board() passed successfully")
#test_board()

class Button:
	"""  Detects click to the squares on the board, and adjusts the 
	X's and O's accordingly
	"""      
	def __init__(self, squareNum):
		if squareNum == 0 or squareNum == 3 or squareNum == 6:
			xCenter = 19
		elif squareNum == 1 or squareNum == 4 or squareNum == 7:
			xCenter = 40.5
		else: 
			xCenter = 61.5

		if squareNum == 0 or squareNum == 1 or squareNum == 2:
			yCenter = 84.5
		elif squareNum == 3 or squareNum == 4 or squareNum == 5:
			yCenter = 60.5
		else:
			yCenter = 36

		# Creating an X
		self.X1 = Polygon(Point(xCenter+4.5,yCenter+4), Point(xCenter-2.5,yCenter-6), Point(xCenter-4.5,yCenter-4), Point(xCenter+2.5,yCenter+6)) # ave: (40.5,59.5)
		self.X2 = Polygon(Point(xCenter-4.5,yCenter+4), Point(xCenter+2.5,yCenter-6), Point(xCenter+4.5,yCenter-4), Point(xCenter-2.5,yCenter+6))
		self.X1.setFill("blue"), self.X2.setFill("blue")
		self.X1.setOutline("blue"), self.X2.setOutline("blue")  

		# Creating an O
		self.O = Oval(Point(xCenter-4.5,yCenter+6), Point(xCenter+4.5,yCenter-6))
		self.O.setOutline("red"), self.O.setWidth(12)

class GUI:
	""" This class draws the playing screen""" 
	def __init__(self):
		self.winsDisplay = Text(Point(94,56), "0")
		self.lossesDisplay = Text(Point(94,50), "0")
		self.tiesDisplay = Text(Point(94,44), "0")

		self.XBox = Rectangle(Point(92, 65), Point(98, 72))
		self.XBox.setWidth(4)
		self.XBox.setFill("grey")
		self.XBox.draw(win)

		self.OBox = Rectangle(Point(82, 65), Point(88, 72))
		self.OBox.setWidth(4)
		self.OBox.setFill("grey")
		self.OBox.draw(win)
		
		self.X = Text(Point(95, 75.5), 'X')
		self.X.setSize(25), self.X.setStyle("bold")
		self.X.setTextColor("blue")
		self.X.draw(win)
		
		self.O = Text(Point(85, 75.5), 'O')
		self.O.setSize(25), self.O.setStyle("bold")
		self.O.setTextColor("red")
		self.O.draw(win)

		self.winsText = Text(Point(88,56), "Wins: ")
		self.winsText.setSize(18)
		self.winsText.draw(win)

		self.lossesText = Text(Point(88,50), "Losses: ")
		self.lossesText.setSize(18)
		self.lossesText.draw(win)

		self.tiesText = Text(Point(88,44), "Ties: ")
		self.tiesText.setSize(18)
		self.tiesText.draw(win)

		self.tiesDisplay.setSize(18)
		self.winsDisplay.setSize(18)
		self.lossesDisplay.setSize(18)
		self.tiesDisplay.draw(win)
		self.winsDisplay.draw(win)
		self.lossesDisplay.draw(win)

		self.v1 = Rectangle(Point(28,25),Point(30,95))
		self.v2 = Rectangle(Point(51,25),Point(53,95))
		self.h1 = Rectangle(Point(10,47),Point(70,49))
		self.h2 = Rectangle(Point(10,72),Point(70,74))
		self.v1.setFill("gray"), self.v2.setFill("gray")
		self.h1.setFill("gray"), self.h2.setFill("gray")
		self.v1.setOutline("gray"), self.v2.setOutline("gray")
		self.h1.setOutline("gray"), self.h2.setOutline("gray")
		self.h1.draw(win), self.h2.draw(win)
		self.v1.draw(win), self.v2.draw(win)

		self.restart = Rectangle(Point(15,8),Point(31,14))
		self.restartText = Text(Point(23,11), "Restart")
		self.restart.setOutline('red')
		self.restart.setWidth(4)
		self.restart.setFill('#000066')
		self.restartText.setSize(18)
		self.restartText.setTextColor('white')
		self.restart.draw(win), self.restartText.draw(win)

		self.mainMenu = Rectangle(Point(40,8),Point(56,14))
		self.mainMenuText = Text(Point(48,11), "Main Menu")
		self.mainMenu.setOutline('red')
		self.mainMenu.setWidth(4)
		self.mainMenu.setFill('#000066')
		self.mainMenuText.setTextColor('white')
		self.mainMenuText.setSize(18)
		self.mainMenu.draw(win), self.mainMenuText.draw(win)

		self.quit = Rectangle(Point(65,8),Point(81,14))
		self.quitText = Text(Point(73,11), "Quit")
		self.quit.setOutline('red')
		self.quit.setWidth(4)
		self.quit.setFill('#000066')
		self.quitText.setTextColor('white')
		self.quitText.setSize(18)
		self.quit.draw(win), self.quitText.draw(win)

		self.Xcheck1 = Line(Point(93.5,68), Point(94.5,66))
		self.Xcheck2 = Line(Point(94.5,66), Point(97,71))
		self.Xcheck1.setWidth(4), self.Xcheck2.setWidth(4)
		self.Xcheck1.setFill("forest green"), self.Xcheck2.setFill("forest green")
		self.Xcheck1.draw(win), self.Xcheck2.draw(win)

		self.Ocheck1 = self.Xcheck1.clone()
		self.Ocheck2 = self.Xcheck2.clone()
		self.Ocheck1.move(-10,0), self.Ocheck2.move(-10,0)
		self.Ocheck1.setWidth(4), self.Ocheck2.setWidth(4)
		self.Ocheck1.setFill("forest green"), self.Ocheck2.setFill("forest green")

		#if drawnX:
		#	self.Xcheck1.draw(win), self.Xcheck2.draw(win)
		#if drawnO:
		#	self.Ocheck1.draw(win), self.Ocheck2.draw(win)
		
	def checkO(self):
		self.Xcheck1.undraw(), self.Xcheck2.undraw()
		self.Ocheck1.draw(win), self.Ocheck2.draw(win)

	def checkX(self):
		self.Ocheck1.undraw(), self.Ocheck2.undraw()
		self.Xcheck1.draw(win), self.Xcheck2.draw(win)

	def undrawGUI(self):
		self.XBox.undraw()
		self.OBox.undraw()
		self.X.undraw()
		self.O.undraw()
		self.winsText.undraw()
		self.lossesText.undraw()
		self.tiesText.undraw()
		self.tiesDisplay.undraw()
		self.winsDisplay.undraw()
		self.lossesDisplay.undraw()
		self.h1.undraw(), self.h2.undraw()
		self.v1.undraw(), self.v2.undraw()
		self.restart.undraw(), self.restartText.undraw()
		self.mainMenu.undraw(), self.mainMenuText.undraw()
		self.quit.undraw(), self.quitText.undraw()
		self.Ocheck1.undraw(), self.Ocheck2.undraw()
		self.Xcheck1.undraw(), self.Xcheck2.undraw()

	def updateScores(self,game):
		self.winsDisplay.setText(game.getWins())
		self.lossesDisplay.setText(game.getLosses())
		self.tiesDisplay.setText(game.getTies())

		# Assings data to the file
		#r = Record(game.getWins(),game.getLosses(),game.getTies())
		#r.getScores()

	def restartScores(self,game):
		self.winsDisplay.setText(game.getNewWins())
		self.lossesDisplay.setText(game.getNewLosses())
		self.tiesDisplay.setText(game.getNewTies())

	def inQuit(self, point):
		x,y = point.getX(), point.getY()
		return ((x >= 65) & (x <= 81)) & ((y >= 8) & (y <= 14)) 

	def inRestart(self, point):
		x,y = point.getX(),point.getY()
		return ((x >= 15) & (x <= 31)) & ((y >= 8) & (y <= 14)) 

	def inMainMenu(self, point):
		x,y = point.getX(),point.getY()
		return ((x >= 40) & (x <= 56)) & ((y >= 8) & (y <= 14)) 

class FrontPage:
	def __init__(self):
		global count, Hard, Medium, Easy
		self.countH = 0
		self.countM = 0
		self.countE = 0

		# Drawing "Quit" button
		self.restart = Rectangle(Point(15,38),Point(31,44))
		self.restartText = Text(Point(23,41), "Quit")
		self.restart.setOutline('red')
		self.restart.setWidth(4)
		self.restart.setFill('#000066')
		self.restartText.setTextColor('white')
		self.restartText.setSize(18), self.restart.draw(win)
		self.restartText.draw(win)

		# Drawing "Play" button
		self.qRectangle = Rectangle(Point(15,64),Point(31,70))
		self.qRectangle.setOutline('red')
		self.qRectangle.setWidth(4)
		self.qRectangle.setFill('#000066')
		self.qText = Text(Point(23,67), "Play")
		self.qText.setTextColor('white')
		self.qText.setSize(18), self.qRectangle.draw(win)
		self.qText.draw(win)

		self.course = Text(Point(40,90),"Can you defeat Mr. Computer on each level?")
		self.course.setSize(25), self.course.setStyle("bold")
		self.course.setTextColor('#000000')
		self.course.draw(win)

		#self.name = Text(Point(35,89),"-by Daniel Saltz")
		#self.name.setSize(17)
		#self.name.draw(win)

		win.setBackground('#5CADFF')

		self.tic = Text(Point(55,50),"Tic")
		self.tic.setSize(36), self.tic.setTextColor('#FF0066')
		self.tic.setStyle("bold"), self.tic.draw(win)

		self.rules = Text(Point(14,24), "Rules:")
		self.rules1 = Text(Point(47,17), "It is your job to defeat the computer in this famous game of tic tac toe.")
		self.rules2 = Text(Point(50.5,13), "Your objective is to place an X or an O in an empty space on the 3X3 board.")
		self.rules3 = Text(Point(48.5,9), "You win the game by placing 3 consecutive similar shapes on the board.")

		self.rules.setSize(22)
		self.rules1.setSize(17)
		self.rules2.setSize(17)
		self.rules3.setSize(17)
		self.rules.draw(win)
		self.rules1.draw(win)
		self.rules2.draw(win)
		self.rules3.draw(win)

		self.easy = Rectangle(Point(62, 65), Point(68, 72))
		self.easy.setWidth(4)
		self.easy.setFill("grey")
		self.easy.draw(win)

		self.medium = Rectangle(Point(77, 65), Point(83, 72))
		self.medium.setWidth(4)
		self.medium.setFill("grey")
		self.medium.draw(win)
		
		self.hard = Rectangle(Point(92, 65), Point(98, 72))
		self.hard.setWidth(4)
		self.hard.setFill("grey")
		self.hard.draw(win)

		self.hardText = Text(Point(95, 75.5), 'Hard')
		self.hardText.setSize(20)
		self.hardText.setTextColor("#000066")
		self.hardText.draw(win)
		
		self.mediumText = Text(Point(80, 75.5), 'Medium')
		self.mediumText.setSize(20)
		self.mediumText.setTextColor("#000066")
		self.mediumText.draw(win)

		self.easyText = Text(Point(65, 75.5), 'Easy')
		self.easyText.setSize(20)
		self.easyText.setTextColor("#000066")
		self.easyText.draw(win)

		self.Hcheck1 = Line(Point(93.5,68), Point(94.5,66))
		self.Hcheck2 = Line(Point(94.5,66), Point(97,71))
		self.Hcheck1.setWidth(4), self.Hcheck2.setWidth(4)
		self.Hcheck1.setFill("forest green"), self.Hcheck2.setFill("forest green")
		
		self.Mcheck1 = self.Hcheck1.clone()
		self.Mcheck2 = self.Hcheck2.clone()
		self.Mcheck1.move(-15,0), self.Mcheck2.move(-15,0)
		self.Mcheck1.setWidth(4), self.Mcheck2.setWidth(4)
		self.Mcheck1.setFill("forest green"), self.Mcheck2.setFill("forest green")

		self.Echeck1 = self.Hcheck1.clone()
		self.Echeck2 = self.Hcheck2.clone()
		self.Echeck1.move(-30,0), self.Echeck2.move(-30,0)
		self.Echeck1.setWidth(4), self.Echeck2.setWidth(4)
		self.Echeck1.setFill("forest green"), self.Echeck2.setFill("forest green")

		if Hard == True:
			self.Hcheck1.draw(win), self.Hcheck2.draw(win)
		if Medium == True:
			self.Mcheck1.draw(win), self.Mcheck2.draw(win)
		if Easy == True:
			self.Echeck1.draw(win), self.Echeck2.draw(win)

		time.sleep(.5)
		self.tac = Text(Point(67,45),"Tac")
		self.tac.setSize(36), self.tac.setTextColor('#194719')
		self.tac.setStyle("bold"), self.tac.draw(win)

		time.sleep(.5)
		self.toe = Text(Point(79,40),"Toe")
		self.toe.setSize(36), self.toe.setTextColor('yellow')
		self.toe.setStyle("bold"), self.toe.draw(win)

	def checkM(self):
		self.Echeck1.undraw(), self.Echeck2.undraw()
		self.Hcheck1.undraw(), self.Hcheck2.undraw()
		self.Mcheck1.draw(win), self.Mcheck2.draw(win)

	def checkE(self):
		self.Mcheck1.undraw(), self.Mcheck2.undraw()
		self.Hcheck1.undraw(), self.Hcheck2.undraw()
		self.Echeck1.draw(win), self.Echeck2.draw(win)

	def checkH(self):
		self.Echeck1.undraw(), self.Echeck2.undraw()
		self.Mcheck1.undraw(), self.Mcheck2.undraw()
		self.Hcheck1.draw(win), self.Hcheck2.draw(win)

	def undrawPage(self):
		self.restart.undraw()
		self.restartText.undraw()
		self.qRectangle.undraw()
		self.qText.undraw()
		self.course.undraw()
		self.tic.undraw()
		self.tac.undraw()
		self.toe.undraw()
		#self.name.undraw()
		self.rules.undraw()
		self.rules1.undraw()
		self.rules2.undraw()
		self.rules3.undraw()
		self.easy.undraw()
		self.hard.undraw()
		self.medium.undraw()
		self.easyText.undraw()
		self.mediumText.undraw()
		self.hardText.undraw()
		self.Hcheck1.undraw(), self.Hcheck2.undraw()
		self.Mcheck1.undraw(), self.Mcheck2.undraw()
		self.Echeck1.undraw(), self.Echeck2.undraw()
		win.setBackground('#2B6E2B')

	def inCheckE(self, point):
		x,y = point.getX(), point.getY()
		return ((x >= 62) & (x <= 68)) & ((y >= 65) & (y <= 72)) 

	def inCheckM(self, point):
		x,y = point.getX(),point.getY()
		return ((x >= 77) & (x <= 83)) & ((y >= 65) & (y <= 72)) 

	def inCheckH(self, point):
		x,y = point.getX(),point.getY()
		return ((x >= 92) & (x <= 98)) & ((y >= 64) & (y <= 70)) 

	def fixCounts(self):
		if Hard:
			self.countH += 1
			self.countM = 0
			self.countE = 0
		if Medium:
			self.countM += 1
			self.countH = 0
			self.countE = 0
		if Easy:
			self.countE += 1
			self.countM = 0
			self.countH = 0

	def chooseLevel(self,point):
		global Hard, Medium, Easy
		
		if self.inCheckH(point) and not Hard:
			Easy = False
			Medium = False
			Hard = True
			self.fixCounts()
			if self.countH == 0:
				return None
			else:
				self.countH = 0
				self.checkH()
				return None				
		if self.inCheckM(point) and not Medium:
			Hard = False
			Easy = False
			Medium = True
			self.fixCounts()
			if self.countM == 0:
				return None
			else:
				self.countM = 0
				self.checkM()
				return None
		if self.inCheckE(point) and not Easy:
			Hard = False
			Medium = False
			Easy = True
			self.fixCounts()
			if self.countE == 0:
				return None
			else:
				self.countE = 0
				self.checkE()
				return None

	def drawLevel(self):
		if Hard == True:
			return ("Hard")
		elif Medium == True:
			return ("Medium")
		elif Easy == True:
			return ("Easy")

	def inQuit(self, point):
		x,y = point.getX(), point.getY()
		return ((x >= 15) & (x <= 31)) & ((y >= 38) & (y <= 44)) 

	def inPlay(self, point):
		x,y = point.getX(),point.getY()
		return ((x >= 15) & (x <= 31)) & ((y >= 64) & (y <= 70)) 

class Record:
	def __init__(self,wins,losses,ties):
		""" Acquires the updated score count from the Board class"""
		self.table = [0,0,0,0,0,0,0,0,0,0]
		self.wins = wins
		self.losses = losses
		self.ties = ties
		self.score = [self.wins,self.losses,self.ties]

	def getScores(self):
		""" Writes the appropriate file given the input from the consructor"""

		f = open("HighScores.txt","w")
		f.write("\n|-----------|")
		f.write("\n| W | L | T |")
		f.write("\n|-----------|\n")
		x = "| "
		y = " |"
		spce = "   "
		w = str(self.score[0])
		l = str(self.score[1])
		t = str(self.score[2])
		f.write(x+w+spce+l+spce+t+y )
		f.close()

def playOneGame(game, gui,front):
	""" Plays one game of Tic-Tac-Toe"""
	b, z, w = 0, 0, 0
	while True:
		#if b == 0:
			#gui.updateScores(game)
		#	b += 1
		if game.Winner() != 0: # Makes sure that the game isn't over
			gui.updateScores(game)
			break
		point = win.getMouse()
		if gui.inMainMenu(point):
			return "Main Menu"
		if gui.inQuit(point): # Quits when "quit" button is clicked on
			return "quit"
		if z == 0:
			game.chooseSide(point,gui) # Assigns user to X or O
		if game.checkIfClicked(point): # Only responds if a square is clicked
			game.drawClick(point)
			z += 1
			w += 1
			if game.Winner() != 0: # Makes sure that the game isn't over
				gui.updateScores(game)
				break
			time.sleep(1)
			if front.drawLevel() == "Hard":
				game.perfectAI()
			elif front.drawLevel() == "Medium":
				game.mediumAI()
			elif front.drawLevel() == "Easy":
				game.randomAI()

def controlFlow():
	""" Controls the flow of the game. """
	game, front = Game(), FrontPage() # Draws front page
	y, w = 1, 1
	while True:
		while True: 	# Only responds if clicking in a button
			point = win.getMouse()
			playButton = front.inPlay(point)
			quitButton = front.inQuit(point)

			if playButton:	
				break
			if quitButton:
				break
			front.chooseLevel(point) # Changes which level is checked
		if playButton:
			front.undrawPage() 	# Undraws front page
			gui = GUI()			# Draws playing page
			x = 0
			while True: # Keeps playig games until the user clicks to do otherwise
				if x == 0:
					pg = playOneGame(game,gui,front)
					x += 1
					if pg == "quit": 	# Quits when "quit" is clicked during the game
						y = 0
						break
					if pg == "Main Menu":
						w = 0
				if pg == "Main Menu" or w == 0:
					gui.restartScores(game)
					game.resetBoard()	# Undraws the X's and O's
					gui.undrawGUI()		# Undraws the playing page
					front = FrontPage() # Draws the front page
					break
				point = win.getMouse() # Once game ends, this click determines what to do next
				if game.checkIfClicked(point):
					pg2 = playOneGame(game,gui)
					if pg2 == "Main Menu":
						w = 0
				if gui.inRestart(point):
					game.resetBoard()
					bl = playOneGame(game,gui,front)
				if gui.inQuit(point) or y == 0: 	# Quits when "quit" button is clicked on
					y = 0
					break
				if gui.inMainMenu(point) or w == 0:
					gui.restartScores(game)
					game.resetBoard()	# Undraws the X's and O's
					gui.undrawGUI()		# Undraws the playing page
					front = FrontPage() # Draws the front page
					break
		if quitButton:
			front.undrawPage()
			goodbye()
			break
		if y == 0:
			gui.undrawGUI()
			goodbye()
			break

def goodbye():

	byeList = ["See ya!", "Have a nice day!", "Catch you next time!", "Goodbye",
				"Catch ya later!", "Chao", "Adios", "ByeBye", "See ya lata allegata"]
	choose = choice(byeList)
	win.setBackground('gold')
	bye = Text(Point(50, 50), choose)
	bye.setSize(35)
	bye.setTextColor("#000066")
	bye.setStyle("bold")
	bye.draw(win)
	time.sleep(1.3)

def main():
	controlFlow()
	win.close()
main()

