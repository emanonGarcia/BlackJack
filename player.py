class Player:

    purse = 100
    score = {'ace': (1, 11), 'two': 2, 'three': 3, 'four': 4,
                'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
                'nine': 9, 'ten': 10, 'jack': 10, 'queen': 10,
                'king': 10}

    def __init__(self, name=None):
        if not name:
            self.name = input("What name do you want to play as? ")
        else:
            self.name = name
        self.hand = []
        self.hidden_hand = ['_']

    def __str__(self):
        return "{}: {}".format(self.name, self.purse)

    def __repr__(self):
        return "name: {}, purse: {}".format(self.name, self.purse)

    def show_hand(self):
        return str(self.hand)

    def show_hidden_hand(self):
        return self.hidden_hand

    def get_value(self):
        self.soft_hand = 0
        self.hard_hand = 0

        for card in self.hand:
            if card.value == "ace":
                self.soft_hand += 1
                if self.hard_hand < 22:
                    self.hard_hand += 11
            else:
                self.soft_hand += Player.score[card.value]
                self.hard_hand += Player.score[card.value]

    def show_hand_value(self):
        if self.hard_hand == self.soft_hand:
            return self.hard_hand
        elif self.hard_hand > 21:
            self.hard_hand = self.soft_hand
            return self.hard_hand
        else:
            return (self.soft_hand, self.hard_hand)
