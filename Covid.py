import random

class card():

    def _init_(self, suit, face):
        self.suit = suit
        self.face = face
       
class DeckofCard():
    def _init_(self):
        self.deck = []
    def shuffle_deck(self):
        random.shuffle(self.deck)
    
    def print_deck(self):
        for card in self.deck:
            print(card.face, "of", card.suit)

        self.suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        
        for suit in self.suits:
            for face in faces:
                self.deck.append(card(suit, face))
    def shuffle_deck(self):
        random.shuffle(self.deck)
    def print_deck(self):
        for card in self.deck:
            print(card.face, "f", card.suit, end=" ")


