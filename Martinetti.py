import random
class Die :
    def __init__(self, dieSides = 6) :
        self.dieNum = 0

    def __str__ ( self ) :
        return dieNum

    def random ( self ) :
        dieNum = random.randint(1,6)


class Testing :
    def __init__(self)
    dieFirst = Die() #First die
    dieSecond = Die() #Second die
    playerOne = ("") #Add name
    playerTwo = ("") 
    playerThree = ("")
    test = Testing(Martinetti

#test = Testing(Die())


class Player :
    def __init__(self, playerName) :
        self.name = playerName


class Martinetti :
    def __init__ (self, dieFirst, dieSecond, playerNum)
        self.dieOne = dieFirst 
        self.dieTwo = dieSecond
        self.positionOne = [1,2,3,4,5,6,7,8,9,10,11,12] #Marks position going up
        self.positionTwo = [12,11,10,9,8,7,6,5,4,3,2,1] #Marks position going down
        self.playerNum = 2
        self.oneEmpty = false #true if the first array is all 0
        self.twoEmpty = false #true if the second array is all 0
        #0 will mean that a position has been reached

    #Rolls the dice
    def roll (self) 
        dieOne.random()
        dieTwo.random()

    # Checks and changes the position in the game (what numbers are crossed off)
    def position (self)
        roll()
        oneEmpty = false
        twoEmpty = false
        numOne = 0 #number crossed off going up
        numTwo = 0 #number crossed off going down

        for i in xrange(0,11, +1) :
            if positionOne[i] == 0 :
                numOne +

        if numOne == 12 :
            for i in xrange(0,11, +1) :
                if positionTwo[i] == 0 :
                    numTwo +

        if numOne != 12 :
            return numOne #returns position going up

        if numTwo != 12 :
            return numTwo #returns position going down

        return 0 #no more positions
        

    def roll (self)
        dieOne.random()
        dieTwo.random()
        calculate(position())

    def calculate (placement)
        numOne = dieOne.number() #Die one roll
        numTwo = dieTwo.number() #Die two roll

        if placement == 0 :
            #make a winning method

        i = placement
        while i != 0 :
            if positionOne[placement] == numOne :
                positionOne[placement] = 0
            elif positionOne[placement] == numTwo :
                positionOne[placement] = 0
            elif positionOne[placement == numOne + numTwo :
                positionOne[placement] = 0
            else :
                i = 0
