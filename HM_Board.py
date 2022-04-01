""" File: HM_Board.py
    Author: Jackson Covey
    Purpose: This program is meant to act as a Card List of the
    cards released in the 1st edition of in a H&M The Hiring TCG.
    It will contain a set of created Card Objects that are hard-coded

    USAGE:
    
"""
from HM_Card_List import CHARACTER_TYPES
import random
# board can be [None, None, None, None, None] and have 2.
# or you can have 1 big one



class Board():

    def __init__(self, deck_one, deck_two):
        '''
        This constructor defines the Board Class's public

        Arguments: player_one, Player
                   one_floor_zone, 
                   one_t_and_a_zone,
                   one_boh_zone,
                   one_deck, 
                   one_discard_pile,
                   one_removed_from_field,
                   one_hand,
                   one_has_won,

                   player_two, Player
                   two_floor_zone, 
                   two_t_and_a_zone,
                   two_boh_zone,
                   two_deck
                   two_discard_pile,
                   two_removed_from_field,
                   two_hand,
                   two_has_won,

        # write the functions and what they do
        '''
        # decks must be stacks when passed
        # one side of the board
        self.player_one = Player('player 1', deck_one, 'red')
        self.one_floor_zone = self.player_one.floor_zone
        self.one_t_and_a_zone = self.player_one.t_and_a_zone
        self.one_boh_zone = self.player_one.boh_zone
        self.one_deck = self.player_one.deck
        self.one_discard_pile = self.player_one.discard_pile
        self.one_removed_from_field = self.player_one.removed_from_field
        self.one_hand = self.player_one.hand
        self.one_has_won = self.player_one.has_won
        # other side of the board
        self.player_two = Player('player 2', deck_two, 'blue')
        self.two_floor_zone = self.player_two.floor_zone
        self.two_t_and_a_zone = self.player_two.t_and_a_zone
        self.two_boh_zone = self.player_two.boh_zone
        self.two_deck = self.player_two.deck
        self.two_discard_pile = self.player_two.discard_pile
        self.two_removed_from_field = self.player_two.removed_from_field
        self.two_hand = self.player_two.hand
        self.two_has_won = self.player_two.has_won


class Player():
    def __init__(self, name, deck, color):
        '''
        This constructor defines the Player Class's public
        variables.

        Arguments: 
                   name, String
                   floor_zone, Card List
                   t_and_a_zone, Card List
                   boh_zone, Card List
                   deck, Card Stack
                   discard_pile, Card Set
                   removed_from_field, Card Stack
                   hand, Card list
                   has_won, Boolean
        '''
        self.name = name
        self.floor_zone = [None, None, None, None, None]
        self.current_num_on_floor = 0
        self.t_and_a_zone = [None, None, None, None, None]
        self.boh_zone = []
        self.tapped_boh = 0
        self.deck = deck
        self.discard_pile = set([])
        self.removed_from_field = Stack()
        self.hand = []
        self.has_won = False
        self.ongoing_abilities = []
        self.color = color

    def set_color(self):
        for card in self.deck.get_list():
            card.color = self.color

    def get_hand(self):
        '''
        This function is a getter method for the player's hand

        Arguments: n/a
        Return Values: List of Cards
        '''
        return self.hand
    
    def get_deck(self):
        '''
        This function is a getter method for the player's deck

        Arguments: n/a
        Return Values: Stack of Cards
        '''
        return self.deck

    def shuffle_deck(self):
        '''
        This function shuffles the player's deck

        Arguments: n/a
        Return Values: n/a
        '''
        new_deck = Stack()
        deck = self.deck.get_list()
        while len(deck) > 0:
            card = random.choice(deck)
            deck.remove(card)
            new_deck.push(card)
        self.deck = new_deck
    
    def draw(self):
        '''
        This function xdraws a card

        Arguments: n/a
        Return Values: n/a
        '''
        drawn_card = self.deck.pop()
        print(drawn_card.get_name() + ' was drawn\n')
        self.hand.append(drawn_card)
        return drawn_card

    def set_t_and_a_zone(self):
        '''
        This function sets the player's t&a zone at the beginning of the game

        Arguments: n/a
        Return Values: n/a
        '''
        for i in range(5):
            self.t_and_a_zone[i] = self.deck.pop()

    def play_character_card(self, card_name):
        '''
        plays a card on the floor
        '''
        # finds card by name
        played_card = None
        for card in self.hand:
            if card.get_name() == card_name:
                played_card = card
        # checks if player has enough boh to play
        if self.can_play(played_card):
            position = input("what position would you like to place " +
            played_card.get_name() + ' in?\n').strip()
            if not position.isnumeric():
                print('enter a number 1-5')
                return False
            position = int(position) - 1
            # check if board restrictions prevent play
            if self.floor_zone[position] is not None:
                print('sorry, there is already something there\n')
                return False
            elif self.board_is_full(self.floor_zone):
                print('sorry, the board is full\n')
                return False
            # taps the # of boh points
            print()
            total_boh = 0
            for i in range(len(self.boh_zone)):
                if total_boh == played_card.get_cost():
                    break
                if not self.boh_zone[i].is_tapped():
                    total_boh += 1
                    self.boh_zone[i].tap()
            self.tapped_boh += played_card.get_cost()
            # plays the card on the floor @ position
            played_card.set_position(position)
            self.floor_zone[position] = played_card
            self.current_num_on_floor += 1
            # removes card from hand
            self.hand.remove(played_card)
            
            return True

    def play_spell_card(self, other_player, card_name):
        # finds card by name
        played_card = None
        for card in self.hand:
            if card.get_name() == card_name:
                played_card = card
        # checks if player has enough boh to play
        if self.can_play(played_card):
            if played_card.can_target == 'all_allies':
                targets = self.target_all_allies(played_card)
            elif played_card.can_target == 'ally':
                # this actually might work
                targets = self.find_valid_spell_targets(other_player, played_card)
            elif played_card.can_target == 'all_opponents':
                targets = self.target_all_opponents(other_player, played_card)
            elif played_card.can_target == 'ally\\hand':
                # this actually might work
                targets = self.find_valid_spell_targets(other_player, played_card)
            elif played_card.can_target == 'AOE':
                targets = self.target_all_opponents(other_player, played_card) + self.target_all_allies(played_card)
            else:
                targets = self.find_valid_spell_targets(other_player, played_card)
            if len(targets) == 0:
                print("you cannot play that1:")
                return False
            total_boh = 0
            for i in range(len(self.boh_zone)):
                if total_boh == played_card.get_cost():
                    break
                if not self.boh_zone[i].is_tapped():
                    total_boh += 1
                    self.boh_zone[i].tap()
            self.tapped_boh += played_card.get_cost()
            # applies Spell buffs
            played_card.set_targets(targets)
            # adds spell cards to Character 
            for target in targets:
                target.add_spell_cards([played_card])
            # removes card from hand
            self.hand.remove(played_card)
            return True
        return False

    def play_fashion_card(self, other_player, card_name):
        # finds card by name
        played_card = None
        for card in self.hand:
            if card.get_name() == card_name:
                played_card = card
        # checks if player has enough boh to play
        if self.can_play(played_card):
            target = self.find_valid_equip_target(other_player, played_card)
            if target == False:
                print("You cannot play that2:")
                return False
            total_boh = 0
            for i in range(len(self.boh_zone)):
                if total_boh == played_card.get_cost():
                    break
                if not self.boh_zone[i].is_tapped():
                    total_boh += 1
                    self.boh_zone[i].tap()
            self.tapped_boh += played_card.get_cost()
            # gives buffs and effects 
            # of note, spells dont give effects for some reason
            played_card.set_target(target)
            played_card.apply_factors()
            played_card.give_effects()
            target.add_equipped_cards([played_card])
            # removes card from hand
            self.hand.remove(played_card)
            return True
        return False

    def can_play(self, card):
        '''
        checks if you can play card based on boh cost
        '''
        if card.can_play == False:
            return False
        cost = card.get_cost()
        if cost > len(self.boh_zone):
            print('Sorry, you need more BOH for that card')
            return False
        elif cost > len(self.boh_zone) - self.tapped_boh:
            print('Sorry, you need more untapped BOH for that card')
            return False
        # commented out cuz spells can_play needs to be checked in respect
        # to opponents cards as well as self.board cards
        #elif card.get_type() == 'SPELL' or card.get_type() == 'FASHIONITEM':
        ##    if self.board_is_empty(self.floor_zone):
        #        print('Sorry, the floor has no valid targets for that card')
        #        return False
        return True

    def board_is_full(self, zone):
        for card in zone:
            if card is None:
                return False
        return True

    def board_is_empty(self, zone):
        for card in zone:
            if card is not None:
                return False
        return True    

    def play_boh(self, card_name):
        '''
        plays card in boh zone
        '''
        # finds card by name
        played_card = None
        for card in self.hand:
            if card.get_name() == card_name:
                played_card = card
        # places card in boh zone
        self.boh_zone.append(played_card)
        self.hand.remove(played_card)

    def discard(self, target):
        'discards a card'
        self.discard_pile.add(target)
        for card in target.get_spell_cards():
            self.discard_pile.add(card)
        target.remove_spell_cards()
        self.hand.remove(target)

    def untap_all(self):
        '''
        untaps everything
        '''
        print("floor zone:")
        for card in self.floor_zone:
            if card is not None:
                if card.get_type() in CHARACTER_TYPES:
                    # checks if there are any restrictioncs
                    if card.do_not_untap:
                        if card.do_not_untap_turns == 1:
                            card.do_not_untap = False
                            card.do_not_untap_turns = 0
                        else:
                            card.do_not_untap_turns -= 1
                    else:
                        card.untap()
                else:
                    card.untap()
        print('boh zone:')
        for card in self.boh_zone:
            if card is not None:
                card.untap()
        self.tapped_boh = 0

    def remove_turn_restrictions(self):
        for card in self.hand:
            if card is not None:
                if card.can_play == False and card.can_play_turns > 0:
                    card.can_play_turns -= 1
                    if card.can_play_turns == 0:
                        card.can_play = True

    def find_valid_spell_targets(self, other_player, played_card):
        targets = []
        # checks for ally\\hand tag
        if "hand" in played_card.can_target:
            target = self.target_in_hand(played_card)
            if target is not None:
                return targets.append(target)
        
        if played_card.get_target_num() > self.current_num_on_floor + other_player.current_num_on_floor:
            target_num = self.current_num_on_floor + other_player.current_num_on_floor
        else:
            target_num = played_card.get_target_num()
        for i in range(target_num):
            target_one = None
            target_two = None
            x = True
            while x:
                card_name = input("what card would you like to target with " +
                played_card.get_name() + '?\n').strip()
                for card in self.floor_zone:
                    if card is not None:
                        if card.get_name() == card_name:
                            target_one = card
                            x = False
                            break
                if target_one not in self.floor_zone and not played_card.can_target == 'all':
                    print('please enter valid target')
                else:
                    for card in other_player.floor_zone:
                        if card is not None:
                            if card.get_name() == card_name:
                                target_two = card
                                x = False
                                break
                if target_one is not None and target_two is not None:
                    command = input('would you like to target your card, or your opponents? (1,2)\n').strip()
                    if command == '1':
                        target = target_one
                    elif command == '2':
                        target = target_two
                elif target_one is None:
                    target = target_two
                elif target_two is None:
                    target = target_one
                # checks immunity
                if target_one is None and target_two is None:
                    print('target not valid')
                elif type(target) != type('String'):
                    if target.immune == True:
                        print('character is immune, cannot select\n')
                        return targets
                elif target in targets:
                    return targets
            targets.append(target)
        return targets

    def target_all_allies(self, played_card):
        targets = []
        for card in self.floor_zone:
            if card is not None:
                if card.immune == False:
                    targets.append(card)
        return targets
    
    def target_all_opponents(self, other_player, played_card):
        targets = []
        for card in other_player.floor_zone:
            if card is not None:
                if card.immune == False:
                    targets.append(card)
        return targets

    def find_valid_equip_target(self, other_player, played_card):
        target = None
        target_one = None
        target_two = None
        if self.board_is_empty(other_player.floor_zone) and self.board_is_empty(self.floor_zone):
            return False
        x = True
        while x:
            card_name = input("what card would you like to target with " +
            played_card.get_name() + '?\n').strip()
            for card in self.floor_zone:
                if card is not None:
                    if card.get_name() == card_name and not card.immune:
                        target_one = card
                        x = False
                        break
            if target_one not in self.floor_zone and not played_card.can_target == 'all':
                print('please enter valid target')
            else:
                for card in other_player.floor_zone:
                    if card is not None:
                        if card.get_name() == card_name and not card.immune:
                            target_two = card
                            x = False
                            break
            if target_one is not None and target_two is not None:
                command = input('would you like to target your card, or your opponents? (1,2)').strip()
                if command == '1':
                    target = target_one
                elif command == '2':
                    target = target_two
            elif target_one is None:
                target = target_two
            elif target_two is None:
                target = target_one

        return target
    print()


    def untap(self, target):
        '''
        untaps target card
        '''
        target.untap()
        if target in self.boh_zone:
            self.tapped_boh -= 1

    def play_from_t_and_a_zone(self, other_player, target_num):
        assert target_num <= 4
        card_to_play = self.t_and_a_zone[target_num]
        self.t_and_a_zone[target_num] = None
        # adds card to hand first to avoid issues with play functions
        self.hand.append(card_to_play)
        while True:
            print(card_to_play.get_name())
            print('do you want to play this card, or ' + 
                  'add it to your hand?\n')
            print('type "hand" or "play"')
            answer = input().strip()
            if answer == 'play':
                if card_to_play.get_type() in CHARACTER_TYPES:
                    card_to_play.set_cost(0)
                    if self.play_character_card(card_to_play.get_name()):
                        break
                    else: 
                        print('\ncannot play character, select "hand"\n')
                elif card_to_play.get_type() == 'SPELL':
                    if not self.board_is_empty(self.floor_zone):
                        card_to_play.set_cost(0)
                        if self.play_spell_card(other_player, card_to_play.get_name()):
                            break
                        else:
                            print('\ncannot play spell, select "hand"\n')
                    else:
                        # adds to hand if not playable
                        print('\ncard is not playable and is added to hand\n')
                        break
                elif card_to_play.get_type() == 'FASHIONITEM':
                    if not self.board_is_empty(self.floor_zone):
                        card_to_play.set_cost(0)
                        if self.play_fashion_card(other_player, card_to_play.get_name()):
                            break
                        else:
                            print('\ncannot play fashion item, select "hand"\n')
                    else:
                        # adds to hand if not playable
                        print('\ncard is not playable and is added to hand\n')
                        self.hand.append(card_to_play)
                        break
            elif answer == 'hand':
                # card is already added to hand
                print('\nthe card was added to your hand, but does not cost 0\n')
                print('card cost = ' + str(card_to_play.get_cost()))
                break
            else:
                print('please enter a valid command\n')

    def target_in_hand(self, played_card):
        if played_card.can_target == 'ally\\hand':
            x = True
            while x:
                choice = input("do you want to target a card in your hand?" +
                ' yes/no\n').strip()
                if choice == 'yes':
                    break
                elif choice == 'no':
                    return None
                else:
                    print("enter yes or no\n")
        x = True
        while x:
            card_name = input("what card would you like to target with " +
            played_card.get_name() + '?\n').strip()
            for card in self.hand:
                if card is not None:
                    if card.get_name() == card_name:
                        target = card
                        x = False
                        break
            if target not in self.hand:
                print('please enter valid target')
        return target



class Stack():
    '''
    Stacks as an array
    '''
    def __init__(self):
        self._stack = []
        self._size = 0
        
    def get_list(self):
        return self._stack

    def is_empty(self):
        if self._size == 0:
            return True

    def pop(self):
        if self._stack != []:
            return_val = self._stack[-1]
            self._stack = self._stack[:len(self._stack) - 1]
            self._size -= 1
            return return_val
        else:
            return 

    def peek(self, num):
        stack_items = []
        for i in range(num):
            stack_items.append(self._stack[i])
        return stack_items

    def push(self, item):
        self._stack.append(item)
        self._size += 1

    def size(self):
        return self._size

    def put_on_bottom(self, item):
        self._stack = [item] + self._stack
        self._size += 1


def stack_test():
    x = Stack()
    x.push(1)
    x.push(2)
    print(x.pop())
    print(x.pop())
    print(x.pop())