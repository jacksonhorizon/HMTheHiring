from HM_Card_List import CARD_SET
from HM_Card_List_Player_Two import CARD_SET_2
""" File: HM_Decks.py
    Author: Jackson Covey
    Purpose: This program is meant to emulate the decks found in
        a TCG Card Game.
"""

DECK_1 = CARD_SET

DECK_2 = CARD_SET_2



def print_decks(deck):
    for card in list(deck):
        print(card.get_name())

def print_character_cards():
    print()

def print_spell_cards():
    print()

def print_fashion_items():
    print()

def get_num_characters():
    print()
