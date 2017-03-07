
class Card:

    values = {'ace': 'A', 'two': 2, 'three': 3, 'four': 4,
                'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
                'nine': 9, 'ten': 10, 'jack': 'J', 'queen': 'Q',
                'king': 'K'}
    suits = ["clubs", "diamonds", "hearts", "spades"]
    suits_short = [chr(9827), chr(9830), chr(9829), chr(9824)]

    def __init__(self, suit, value):
        if suit in Card.suits:
            self.suit = suit.lower()
        else:
            raise KeyError("Not a valid suit")
        if value in Card.values:
            self.value = value
        else:
            raise KeyError("Not a valid value")

    def __str__(self):
        return "{}{}".format(Card.values[self.value], Card.suits_short[Card.suits.index(self.suit)])

    def __repr__(self):
        return "{}{}".format(Card.values[self.value], Card.suits_short[Card.suits.index(self.suit)])

    def __eq__(self, other):
        return self.suit == other.suit and self.value == other.value

    def __ne__(self, other):
        return self.suit != other.suit or self.value != other.value
