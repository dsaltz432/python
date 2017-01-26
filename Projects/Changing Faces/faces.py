from graphics import *
from time import sleep

class Face:
    def __init__(self, window, center, size):
        self.window = window
        eyeSize = 0.15 * size
        eyeOff = size / 3.0
        mouthSize = 0.8 * size
        mouthOff = size / 2.0
        self.head = Circle(center, size)
        self.head.draw(window)
        self.leftEye = Circle(center, eyeSize)
        self.leftEye.move(-eyeOff, -eyeOff)
        self.rightEye = Circle(center, eyeSize)
        self.rightEye.move(eyeOff, -eyeOff)
        self.leftEye.draw(window)
        self.rightEye.draw(window)
        self.p1 = center.clone()
        self.p1.move(-mouthSize/2, mouthOff)
        self.p2 = center.clone()
        self.p2.move(mouthSize/2, mouthOff)
        self.mouth = Line(self.p1, self.p2)
        self.mouth.draw(window)

    def Smile(self):
        self.mouth.undraw()
        p3 = self.p1.clone()
        p3.move(-10, -20)
        p4 = self.p2.clone()
        p4.move(10, -20)
        self.mouth = Polygon(p3, self.p1, self.p2, p4)
        self.mouth.draw(self.window)

    def Normal(self):
        self.mouth.undraw()
        self.mouth = Line(self.p1, self.p2)
        self.mouth.draw(self.window)

    def Gasp(self):
        self.mouth.undraw()
        self.mouth = Circle(Point(200,230), 15)
        self.mouth.draw(self.window)

    def Toungue(self):
        self.mouth.undraw()
        self.mouth = Rectangle(Point(180,230), Point(220, 210))
        t = Oval(Point(193, 220), Point(207, 270))
        self.mouth.draw(self.window)
        t.draw(self.window)
        time.sleep(.5)
        t.undraw()

    def inSmile(self, x, y) :
        return ((x >= 10) & (x <= 140)) & ((y >= 40) & (y <= 80)) 

    def inNormal(self, x, y) :
        return ((x >= 10) & (x <= 140)) & ((y >= 100) & (y <= 140)) 

    def inGasp(self, x, y) :
        return ((x >= 10) & (x <= 140)) & ((y >= 300) & (y <= 340)) 
       
    def inToungue(self, x, y) :    
        return ((x >= 320) & (x <= 380)) & ((y >= 300) & (y <= 340)) 

    def Exit(self, x, y) :
        return ((x >= 320) & (x <= 380)) & ((y >= 20) & (y <= 80)) 

    def drawButtons(self) :
        # Draws smile button
        smileButton = Rectangle(Point(10,80), Point(140,40))
        smileButton.setFill("red")    
        smileButton.draw(self.window)
        smileText = Text(Point(75,60), "Smile")
        smileText.setSize(18)
        smileText.draw(self.window)

        # Draws normal button
        normalButton = Rectangle(Point(10,100), Point(140,140))
        normalButton.setFill("blue")    
        normalButton.draw(self.window)
        normalText = Text(Point(75,120), "Normal")
        normalText.setSize(18)
        normalText.draw(self.window)

        # Draws gasp button
        gaspButton = Rectangle(Point(10,300), Point(140,340))
        gaspButton.setFill("green")    
        gaspButton.draw(self.window)
        gaspText = Text(Point(75,320), "Gasp!")
        gaspText.setSize(18)
        gaspText.draw(self.window)

        # Draws toungue button
        toungueButton = Rectangle(Point(320,300), Point(380,340))
        toungueButton.setFill("orange")    
        toungueButton.draw(self.window)
        toungueText = Text(Point(350,320), "Ha!")
        toungueText.setSize(18)
        toungueText.draw(self.window)

        # Draws exit button
        exitButton = Rectangle(Point(320,20), Point(380,80))
        exitButton.setFill("black")    
        exitButton.draw(self.window)
        exitText = Text(Point(350,50), "Exit")
        exitText.setTextColor("white")
        exitText.setSize(18)
        exitText.draw(self.window)

def main() :
    window = GraphWin("Hello", 400, 400)
    center = Point(200,200)
    size = 80

    # Creates instance of the Face class
    FaceOne = Face(window, center, size)
    Face.drawButtons(FaceOne)
    quit = False

    while not quit: 
        point = window.getMouse()
        x = point.getX()
        y = point.getY()
        
        quit = Face.Exit(FaceOne, x, y) 
        if quit :
            break

        if Face.inSmile(FaceOne, x,y) :
            Face.Smile(FaceOne)

        if Face.inNormal(FaceOne, x,y) :
            Face.Normal(FaceOne)

        if Face.inGasp(FaceOne, x,y) :
            Face.Gasp(FaceOne)

        if Face.inToungue(FaceOne, x,y) :
            Face.Toungue(FaceOne)

    window.close()
main()