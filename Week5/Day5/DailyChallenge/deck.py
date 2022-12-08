import random
class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val


class Deck:
    def __init__(self):
        self.cards = []

        suits = ('♦', '♥', '♣', '♠')
        values = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

        for value in values:
            for suit in suits:
                card = Card(value, suit)
                self.cards.append(card)
                

    def shuffle(self):
        '''Shuffles the deck'''
        random.shuffle(self.cards)

    def deal(self):
        '''Prints a random single card and take it from the deck'''
        card = self.cards.pop()
        print(card.val, card.suit)

deck = Deck()
for card in deck.cards:
    print(card.val, card.suit)

print('shuffled deck:')
deck.shuffle()
for card in deck.cards:
    print(card.val, card.suit)

print('deal:')
card = deck.deal()
