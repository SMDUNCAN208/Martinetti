import random
class Die :
    def __init__(self, _dieSides) :
        self.numSides = _dieSides

    def roll ( self ) :
        dieNum = random.randint(1,6)


class Player :
    def __init__ (self, _name) :
        self.name = _name
        self.gameWon = 0
        self.indexOne = 0
        self.indexTwelve = 0

class Martinetti :
    def __init__ (self, _dieOne, _dieTwo, _dieThree, _playerOne, _playerTwo) :
        self.dieOne = _dieOne
        self.dieTwo = _dieTwo
        self.dieThree = _dieThree
        self.players = [_playerOne, _playerTwo]
        self.one = [1,2,3,4,5,6,7,8,9,10,11,12]
        self.twelve = [12,11,10,9,8,7,6,5,4,3,2,1]
        self.numPlayers = 2

    def simulateGame (self) :
        gameOver = 1

        while gameOver == 1 :
            end = false
            doneOne = false
            doneTwelve = false

            i = 0

            while end == false :
                indexesOne = [0,0]
                indexesTwelve = [0,0]
                dieFirst = dieOne.roll()
                dieSecond = dieTwo.roll()
                dieThird = dieThree.roll()

                print(players[i].name + " rolled a " + dieFirst + ", " + dieSecond + " , and a " + dieThird)

            if indexesOne[i] < 12 : 
                while doneOne == false :
                        if one[indexesOne[i]] == dieOne or one[indexesOne[i]] == dieTwo or one[indexesOne[i]] == dieThree or one[indexesOne[i]] == dieOne + dieTwo or one[indexesOne[i]] == dieOne + dieThree or one[indexesOne[i]] == dieTwo + dieThree or one[indexesOne[i]] == dieOne + dieTwo + dieThree :
                            print(players[i].name + " hase crossed off " + one[indexesOne[i]])
                            indexesOne[i] += 1
                            if indexesOne[i] == 12 :
                                doneOne = doneOne + 1
                        else :
                            doneOne = true
                            print (players[i].name + "'s turn is over")
            elif indexesTwelve[i] < 12 and indexesOne[i] == 12 :
                while doneTwelve == false:
                    if twelve[indexesTwelve[i]] == dieOne or twelve[indexesTwelve[i]] == dieTwo or twelve[indexesTwelve[i]] == dieThree or twelve[indexesTwelve[i]] == dieOne + dieTwo or twelve [indexesTwelve[i]] == dieOne + dieThree or twelve [indexesTwelve[i]] == dieTwo + dieThree or twelve[indexesTwelve[i]] == dieOne + dieTwo + dieThree :
                            print(players[i].name + " has crossed off " + twelve[indexesTwelve[i]])
                            twelve[i] += 1
                            indexesTwelve[i] += 1

                            if indexesTwelve[i] == 12 :
                                doneTwelve = true

                    else :
                        doneTwele = true
                        print (players[i].name + "'s turn is over")
                            
                    if indexesTwelve[i] == 12 :
                        players[i].gamesWon += 1
                        end = true
                        print(player[i].name + " has won the game!")
                        
                      

                             
class Tests : 
    def __init__( self ) :
        dieFirst = Die(6) #First die
        dieSecond = Die(6) #Second die
        dieThird = Die(6) # Third die
        cecilia = Player(Cecilia)
        eva = Player (Eva)
        test = Martinetti(dieFirst, dieSecond, dieThird, cecilia, eva)
        test.simulateGame()
