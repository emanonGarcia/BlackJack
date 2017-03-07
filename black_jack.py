from deck import Deck
from player import Player
import os


class BlackJack:

    BLACK_JACK = 21
    BUST = 22

    def __init__(self):
        os.system('clear')
        self.setup()
        self.game_play()

    def setup(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Player("Dealer")

    def game_play(self):
        self.deck.shuffle()
        self.player.hand = [self.deck.deal_card() for x in range(2)]
        self.dealer.hand = [self.deck.deal_card() for x in range(2)]
        self.dealer.hidden_hand.append(self.dealer.hand[1])
        self.player.get_value()
        print("\n{}'s hand: {}, {}".format(self.player.name, self.player.show_hand(), self.player.show_hand_value()))
        print("{}'s hand: {}".format(self.dealer.name, self.dealer.show_hidden_hand()))
        self.player_turn()

    def player_turn(self):
        print("\nYour hand: {}, {}".format(self.player.show_hand(), self.player.show_hand_value()))
        while self.player.hard_hand < BlackJack.BUST and self.player.hard_hand != BlackJack.BLACK_JACK:
            user_input = input("Do you [H]it or [S]tand? ")
            if len(user_input) == 0:
                continue
            if user_input.lower() == 'h' or user_input[0].lower() == 'h':
                self.player.hand.append(self.deck.deal_card())
                self.player.get_value()
                print("\nYour hand: {}, {}".format(self.player.show_hand(), self.player.show_hand_value()))
                print("{}'s hand: {}".format(self.dealer.name, self.dealer.show_hidden_hand()))
            if user_input.lower() == 's' or user_input[0].lower() == 's':
                self.dealer.get_value()
                print("\n{}'s hand: {}, {}".format(self.dealer.name, self.dealer.show_hand(), self.dealer.hard_hand))
                self.dealer_turn()
            else:
                continue
        if self.player.hard_hand == BlackJack.BLACK_JACK:
            if len(self.player.hand) == 2:
                print("BLACK JACK!")
            self.dealer.get_value()
            self.dealer_turn()
        print("**You Bust, Dealer wins**\n{}'s hand: {}".format(self.dealer.name, self.dealer.show_hand()))
        while True:
            user_input = input("Play again? (Y/n): ")
            if user_input.lower() == 'y' or user_input[0].lower() == 'y':
                self.deck = Deck()
                self.dealer = Player("Dealer")
                self.game_play()

            elif user_input.lower() == 'n' or user_input[0].lower() == 'n':
                exit()
            else:
                continue

    def dealer_turn(self):
        while self.dealer.hard_hand <= 16 and self.dealer.hard_hand != BlackJack.BLACK_JACK:
            self.dealer.hand.append(self.deck.deal_card())
            self.dealer.get_value()
            print("\nYour hand: {}, {}".format(self.player.show_hand(), self.player.hard_hand))
            print("{}'s hand: {}, {}".format(self.dealer.name, self.dealer.show_hand(), self.dealer.hard_hand))
        if self.dealer.hard_hand == BlackJack.BLACK_JACK and len(self.dealer.hand) == 2:
            print("Dealer gets BLACK JACK!")
        if self.dealer.hard_hand == self.player.hard_hand:
            print("Push!")
        elif self.dealer.hard_hand < self.player.hard_hand:
            if self.dealer.hard_hand > BlackJack.BLACK_JACK:
                print("**Dealer Busts, You wins**")
            print("You win!")
        elif self.dealer.hard_hand > BlackJack.BLACK_JACK:
            print("**Dealer Busts, You wins**")
        else:
            print("You lose!")
        while True:
            user_input = input("Play again? (Y/n): ")
            if user_input.lower() == 'y' or user_input[0].lower() == 'y':
                self.deck = Deck()
                self.dealer = Player("Dealer")
                self.game_play()

            elif user_input.lower() == 'n' or user_input[0].lower() == 'n':
                exit()
            else:
                continue


BlackJack()
