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
print('***********************************************************************************')
print('dealing 5 cards')
for i in range(0 , 5):
    print(game.deal())
game.fan()
print('***********************************************************************************')
game.shuffle()
print("Is it ordered after shuffle? -", game.isOrdered())
game.fan()
print('***********************************************************************************')
game.order()
print("Is it Ordered after 'order'? - ", game.isOrdered())
game.fan()
print('***********************************************************************************')
