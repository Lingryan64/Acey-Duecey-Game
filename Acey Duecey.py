import random

class myCards:
    decklist = ['2C','3C','4C','5C','6C','7C','8C','9C','10C','JC',   
          'QC','KC','AC','2D','3D','4D','5D','6D','7D','8D',
          '9D','10D','JD','QD','KD','AD','2H','3H','4H','5H',
          '6H','7H','8H','9H','10H','JH','QH','KH','AH','2S',
          '3S','4S','5S','6S','7S','8S','9S','10S','JS','QS',
          'KS','AS']
    orgDeckList = ['2C','3C','4C','5C','6C','7C','8C','9C','10C','JC',   
          'QC','KC','AC','2D','3D','4D','5D','6D','7D','8D',
          '9D','10D','JD','QD','KD','AD','2H','3H','4H','5H',
          '6H','7H','8H','9H','10H','JH','QH','KH','AH','2S',
          '3S','4S','5S','6S','7S','8S','9S','10S','JS','QS',
          'KS','AS']
        
    def deal(self):
        return self.decklist.pop(0)
    
    def shuffle(self):
        self.decklist = list(self.orgDeckList)
        random.shuffle(self.decklist)
    def fan(self):
        print(self.decklist)
    def isOrdered(self):
        x = []
        c = -1
        while len(x) != len(self.decklist):
            c = c+1
            for i in range(0, len(self.decklist)):
                if str(self.orgDeckList[c]) == str(self.decklist[i]):
                    x.append(self.orgDeckList[c])
        if x == self.decklist:
            return True
        else:
            return False
    def order(self):
        x = []
        c = -1
        while len(x) != len(self.decklist):
            c = c+1
            for i in range(0, len(self.decklist)):
                if str(self.orgDeckList[c]) == str(self.decklist[i]):
                    x.append(self.orgDeckList[c])   
        self.decklist  = x
                 
game = myCards()
game.shuffle()
checker = ['L','2','3','4','5','6','7','8','9','1','J',   
          'Q','K','A']
playerM = 500
cardC = 52
tcount = 0
play = True
bet = 'filler'
print("Welcome to Acey Duecey! you have $500 Good Luck!")

while play == True:
    highlow = 'none'
    x = False
    if cardC < 2:
        carcC = 52
        game.shuffle()
    print("Dealing new set of cards")
    #cardOne handeler
    cardOne = str(game.deal())
    cardC -= 1
    
    if cardOne == 'A':
        while highlow != "high" or "low":
            highlow = input("Do you want your ace as high or low? : ")
            if highlow == 'high':
                cardOne = 'A'
                break
            if highlow == 'low' :
                cardOne = 'L'
                break
            else:
                highlow = input("please enter high or low : ")
    #cardTwo Handeler
    cardTwo = str(game.deal())
    cardC -= 1
    
    #decideds if player hasnt taken a second turn before bet
    if tcount != 2:
        if highlow == 'high':
            bet = input("you are between (High Ace) and (" + cardTwo +") - do you want to bet?   yes/no : ")
            if bet == 'no':
                tcount += 1
        if highlow == 'low':
            bet = input("you are between (Low Ace) and (" + cardTwo +") - do you want to bet?   yes/no : ")
            if bet == 'no':
                tcount += 1
        else:
            bet = input("you are between ("+ cardOne +") and (" + cardTwo + ") - do you want to bet?   yes/no : ")
            if bet == 'no':
                tcount += 1
    if bet == 'yes':
        while x == False:
            wager = int(input("Enter your wager : "))
            if int(wager) > int(playerM):
                print("You currently only have $", playerM)
            if wager <= playerM:
                x = True
        cardThree = str(game.deal())[0]
        cardC -= 1
    if tcount == 2:
        tcount = 0
        
        if highlow == 'high':
            print("you are between (High Ace) and (" + cardTwo +")")
        if highlow == 'low':
            print("you are between (Low Ace)  and (" + cardTwo +")")      
        else:
            print("you are between ("+ cardOne +")    and (" + cardTwo + ")")
        while x == False:
            wager = int(input("Enter your wager, you have to bet : "))
            if int(wager) > int(playerM):
                print("You currently only have $", playerM)
            if wager <= playerM:
                x = True
                
    cardThree = str(game.deal())
    cardC -= 1
        
        #makes card two the higher index number if card one is higher
    if int(checker.index(str(cardOne)[0])) > int(checker.index(str(cardTwo)[0])):
        y = str(cardTwo)
        cardTwo = str(cardOne)
        cardOne = y
            
        #section for deciding game if statements are using the indexed location of drawn cards from checker to compare
        #this part compares cards one and two to see if they are equal to 3 as well as checks if card 3 is in range

    if int(checker.index(str(cardOne)[0])) < int(checker.index(str(cardThree)[0])) < int(checker.index(str(cardTwo)[0])):
        playerM += wager
        print("You won! you drew ("+ str(cardThree) +") you have $" + str(playerM))
            
    elif int(checker.index(str(cardOne)[0])) == int(checker.index(str(cardThree)[0])) or int(checker.index(str(cardTwo)[0]))== int(checker.index(str(cardThree)[0])):
        playerM -= wager
        print("Sorry you lost you drew ("+ str(cardThree) +")  you have $" + str(playerM) + " in funds left")
             
            
    else:
        playerM -= wager
        print("Sorry you lost you drew ("+ str(cardThree) +")  you have $" + str(playerM) + " in funds left")
            
        
                                                                                                        
    if playerM == 0:
        print("Sorry you are out of money")
        play = False

                                                            






















