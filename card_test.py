from card import Card
from deck import Deck
from player import Player


def test_card_instance():
    assert str(Card('hearts', 'ace')) == 'A' + chr(9829)

def test_same_card():
    assert Card('hearts', 'ace') == Card('hearts', 'ace')

def test_differnt_card():
    assert Card('hearts', 'ace') != Card('spades', 'ace')

def test_full_deck_size():
    deck = Deck()
    assert len(deck.deck) == 52

def test_deck_size_after_card_dealt():
    deck = Deck()
    deck.deal_card()
    assert len(deck.deck) != 52

def test_deck_shuffle():
    deck1 = Deck()
    deck2 = Deck()
    deck2.shuffle()
    assert deck1.deck != deck2.deck

def test_player():
    player = Player('Sam')
    assert player.name == 'Sam'

def test_players_hand_one_card():
    player = Player('Sam')
    card = Card('hearts', 'ace')
    player.hand.append(card)
    assert player.hand[0] == Card('hearts', 'ace')

def test_players_hand_two_cards():
    player = Player('Sam')
    card1 = Card('hearts', 'ace')
    player.hand.append(card1)
    card2 = Card('spades', 'ace')
    player.hand.append(card2)
    assert str(player.hand[1]) == 'A' + chr(9824)
