class Player(object):

    def __init__(self):
        self.cardList = []

    def receiveCard(self, card):
        self.cardList.append(card)

    def playCard(self, card):
        pass
