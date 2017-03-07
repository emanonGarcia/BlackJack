from card import Card
import random


class Deck:

    def __init__(self):
        self.deck = [Card(suit, value) for value in Card.values.keys() for suit in Card.suits]

    def __repr__(self):
        return str(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()

    def __str__(self):
        for card in self.deck:
            return card
