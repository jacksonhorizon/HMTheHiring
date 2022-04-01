from HM_Board import Board
from HM_Decks import DECK_1, DECK_2
from HM_Board import Stack
from HM_Activate_Effects import check_effects
from HM_Card_List import CHARACTER_TYPES
from graphics_game import graphics
from HM_The_Hiring_Graphics import*
from HM_Import_Images import import_images
import random
""" File: HM_The_Hiring_.py
    Author: Jackson Covey
    Purpose: This program is meant to act as a Card List of the
    cards released in the 1st edition of in a H&M The Hiring TCG.
    It will contain a set of created Card Objects that are hard-coded

    USAGE:asdasdaszdasd
   
"""

def main():

    '''
    It is the driver class for the game
    '''
    # graphics object, any measurements will use 1000, 500
    # 1100 and 600 are used for visual boarder
    # graphic start
    graphic = graphics(1000, 800, 'HM The Hiring')
    # imports images from HM_Images
    import_images(graphic)
    board = initialize_board(graphic)
    start_game(board, board.player_one, board.player_two, graphic)
    rand = random.randint(1, 100)
    if rand % 2 != 0:
        print('player 1 goes first\n')
        graphic.text(850, 400, 'player 1 goes first')
        current_player = board.player_one
        other_player = board.player_two
    else:
        print('player 2 goes first\n')
        graphic.text(850, 400, 'player 2 goes first')
        current_player = board.player_two
        other_player = board.player_one
    # board starts
    print('Begin the game:')
    print_general_actions(graphic, 'Begin Game!')
    print_general_actions(graphic, 'press enter to continue')
    begin_game_button(graphic)

    # begins turn loop 
    # for graphics, make it its own function so the button press works
    turn_counter = 1
    while not board.player_one.has_won or not board.player_two.has_won:
        print(return_player(current_player, board))
        print_board_graphics(graphic, current_player, other_player)
        input('press enter key to continue\n')
        if turn(current_player, other_player, turn_counter, graphic):
            break
        current_player, other_player = change_player(current_player, other_player)
        turn_counter += 1
    print('End of Game:')
    if board.player_one.has_won:
        print('Player 1 won!')
        print('thanks for playing!')
    if board.player_two.has_won:
        print('Player 2 won!')
        print('thanks for playing!')
    
def begin_game_button(graphic):
    '''
    might be how i do all the pass turn buttons
    '''
    graphic.text(850, 425, 'press to begin the game!')
    r = graphic.rectangle(850, 420, 100, 50)
    #graphic.canvas.tag_bind(r, "<Button-1>", lambda x: begin turn counter(curP, otherP, graphic))

def shuffle_deck(deck, graphic):
    '''
    deck should be a set but can be a list, 
    is shuffled using random.choice which is then is put into a Stack
    '''

    new_deck = Stack()
    if type(deck) == set:
        deck = list(deck)
    else:
        deck = deck.get_list()
    while len(deck) > 0:
        card = random.choice(deck)
        deck.remove(card)
        new_deck.push(card)
    return new_deck

def initialize_board(graphic):
    '''
    initializes board at the beginning of a game
    '''
    # shuffles the two decks
    deck_1 = shuffle_deck(DECK_1, graphic)
    deck_2 = shuffle_deck(DECK_2, graphic)
    # set the two decks on the board
    board = Board(deck_1, deck_2)
    return board

def start_game(board, player_1, player_2, graphic):
    '''
    sets starting 7 card hand
    '''
    player_1.set_color()
    player_2.set_color()
    player_1.set_t_and_a_zone()
    player_2.set_t_and_a_zone()
    for i in range(7):
        board.one_hand.append(board.one_deck.pop())
        board.two_hand.append(board.two_deck.pop())

def turn(current_player, other_player, turn_counter, graphic):
    '''
    conducts a player's turn, does not change turn counter
    '''
    print()
    text = 'turn: ' + str(turn_counter)
    print(text)
    print_general_actions(graphic, text)
    text = 'draw phase:\n' 
    print(text)
    print_general_actions(graphic, text)

    if turn_counter == 1:
        print('this is the first turn, you do not draw\n')
    elif turn_counter != 1:
        card = current_player.draw()
        print_draw_graphics(graphic, card)
    print_general_actions(graphic, 'press enter to continue')
    input('press enter key to continue to commercial planning phase\n')
    commercial_planning_phase(current_player, other_player, graphic)
    boh_phase(current_player, other_player, graphic)
    if opening_phase(current_player, other_player, graphic):
        if battle_phase(current_player, other_player, turn_counter, graphic):
            return True
        closing_phase(current_player, other_player, graphic)
    print('end of ' + current_player.name + "'s turn\n")
    return False

def commercial_planning_phase(current_player, other_player, graphic):
    '''
    Literally just untaps everything, also removes turn restrictions for play
    '''
    print_board_graphics(graphic, current_player, other_player)
    current_player.untap_all()
    current_player.remove_turn_restrictions()
    print_board_graphics(graphic, current_player, other_player)
    text = 'commercial planning phase:\n'
    print(text)
    print_general_actions(graphic, text)
    print_general_actions(graphic, 'press enter to continue')
    input('press enter key to continue to boh phase\n')

def boh_phase(current_player, other_player, graphic):
    '''
    conducts the boh phase of the turn, just adds a card of the players selection
    to the Board.
    '''
    print_board_graphics(graphic, current_player, other_player)
    text = 'boh phase:\n select card or type no'
    print(text)
    print_general_actions(graphic, text)
    show_cards(current_player.get_hand())
    print_hand_graphics(current_player, graphic)
    # asks what card to put in boh zone
    while True:

        card_name = input('which card do you want to put into your ' + 
                          'boh zone this turn?\n' + 
                          'type "no" to skip\n').strip()
        if card_name == 'no':
            break
        if card_in_hand(card_name, current_player):
            current_player.play_boh(card_name)
            print_board_graphics(graphic, current_player, other_player)
            break
        else: 
            text = 'that is not a valid card\n'
            print(text)
            print_general_actions(graphic, text)
    print('\nboh zone:')
    show_cards(current_player.boh_zone)
    print_board_graphics(graphic, current_player, other_player)
    print_tiny_card_list_corner_vertical(graphic, current_player.boh_zone, len(current_player.boh_zone))
    print_general_actions(graphic, 'press enter to continue', True)
    input('press enter key to continue to opening phase\n')

def opening_phase(current_player, other_player, graphic):
    '''
    conducts the opening play phase where a player can play as many cards as they want
    '''
    the_stack = Stack()
    text = 'opening phase:\n'
    print(text)
    print_general_actions(graphic, text)
    show_cards(current_player.get_hand())
    
    # player can play as many cards as they can
    show_hand = True
    while True:
        print_board_graphics(graphic, current_player, other_player)
        if show_hand:
            print_hand_graphics(current_player, graphic)
            text = 'opening phase:\n hand, close, play, show hand'
            print_general_actions(graphic, text)
        end = input('if you want to move to battle phase, type "battle"\n' +
                'if you want to skip the battle phase, type "close"\n' + 
                'if you want to play a card, type "play"\n' +
                '"show hand"\n' + 
                '"show board"\n' +
                '"show discard"\n' + 
                '"show card"\n').strip()
        if end == 'get card':
            get_card(current_player)
        elif end == 'close':
            return False
        # moves on to next phase
        elif end == 'battle':
            break
        elif end == 'show hand':
            if show_hand:
                show_hand = False
            else:
                show_hand = True
        elif end == 'show board':
            print_board(current_player, other_player)
        elif end == 'show discard':
            show_discard_pile(current_player)
        # if the player wants to know what a card does
        elif end == 'show card':
            show_card(current_player, other_player)
        # if the player cannot use any boh, moves to next phase
        elif current_player.tapped_boh == len(current_player.boh_zone):
            print('you have run out of boh, time to attack')
            break
        # plays card
        elif end == 'play':
            play_card(current_player, other_player, the_stack, graphic)
            print_board_graphics(graphic, current_player, other_player)
        else:
            text = 'enter valid command'
            print(text)
            print_general_actions(graphic, text, True)
        print()
        print('current hand')
        show_cards(current_player.get_hand())
    print_general_actions(graphic, 'press enter to continue', True)
    input('\npress enter key to continue to battle phase\n')
    return True


def play_card(current_player, other_player, the_stack, graphic):
    '''
    player, player, Stack
    '''
    card_name = input('enter the card name that' + 
                            ' you want to play\n').strip()
    # plays the card using the name based on type and provided methods in 
    # Player Class if valid Card name
    print()
    if card_in_hand(card_name, current_player):
        card = get_card_from_name(card_name, current_player.hand)
        successful_play = False
        if current_player.can_play(card):
            if card.get_type() in CHARACTER_TYPES:
                successful_play = current_player.play_character_card(card_name)
                print_board_graphics(graphic, current_player, other_player)
                # need to make function to activate character effects
            elif card.get_type() == 'SPELL':
                print_board_graphics(graphic, current_player, other_player)
                successful_play = current_player.play_spell_card(other_player, card_name)
                print_board_graphics(graphic, current_player, other_player)
                play_spell_card_graphics(graphic, card)
                # need to make a function to activate special bs spell effects
            elif card.get_type() == 'FASHIONITEM':
                # deals with different types of fashion items
                print_board_graphics(graphic, current_player, other_player)
                successful_play = current_player.play_fashion_card(other_player, card_name)
                print_board_graphics(graphic, current_player, other_player)
                play_fashion_item_graphics(graphic, card)
                # this should just work
            if successful_play:
                # oppponents response
                check_effects(card, current_player, other_player, graphic)
                current_player = respond(current_player, other_player, the_stack, graphic)
        else:
            text = "you can't play that"
            print_general_actions(graphic, text, True)
    else: 
        text = 'that is not a valid card\n'
        print_general_actions(graphic, text, True)

def battle_phase(current_player, other_player, turn_counter, graphic):
    '''
    conducts the player's battle phase
    '''
    # has to check if the player can attack
    # has to see how many characters they can attack with.
    # targets must be declared individually
    # t&A zone attacks, T&A target(s) must be declared
    # implements the t&a function which means using opponent player.
    # 
    if turn_counter == 1:
        text = 'you cannot conduct the battle phase this turn\n'
        print_general_actions(graphic, 'press enter to continue', True)
        return
    #the_stack = Stack()
    text = 'battle phase:\n'
    print_general_actions(graphic, text)
    while True:
        print_board_graphics(graphic, current_player, other_player)
        print_board(current_player, other_player)
        if list_is_empty(current_player.floor_zone):
            text = 'you cannot attack since your floor is empty\n'
            print_general_actions(graphic, text)
            break
        if not can_attack(current_player):
            text = 'you cannot attack since all characters are tapped\n'
            print_general_actions(graphic, text)
            break
        # if the player cannot use any boh, moves to next phase
        print_general_actions(graphic, 'attack yes/no?')
        command = input('would you like to attack? (yes/no)\n').strip()
        if command == 'no':
            break
        elif command == 'yes':
            has_won = begin_attack(current_player, other_player, graphic)
            if has_won:
                return True
        else:
            text = 'enter yes or no'
            print_general_actions(graphic, text)
    return False

def begin_attack(current_player, other_player, graphic):
    while True:
        attacker = input('which card do you want to attack with\n').strip()
        if card_on_floor(attacker, current_player):
            break
        else:
            print('select a card that exists')
            show_cards(current_player.floor_zone)
            print()
    attacker = get_card_from_name(attacker, current_player.floor_zone)
    if attacker.is_tapped():
        print('this character has already attacked\n')
    else:
        # conducts t&a attack
        if list_is_empty(other_player.floor_zone):
            if list_is_empty(other_player.t_and_a_zone):
                current_player.has_won = True
                return True
            conduct_direct_attack(attacker, current_player, other_player, graphic)
        # conducts character v character attack
        else:
            while True:
                defender = input('which card do you want to attack\n').strip()
                if card_on_floor(defender, other_player):
                    break
                else:
                    print('select a card that exists')
            conduct_character_attack(attacker, current_player, defender, other_player, graphic)
    return False

def closing_phase(current_player, other_player, graphic):
    # should just be second opening phase tbh with the hand limit checker at the end
    the_stack = Stack()
    print('closing phase:\n')
    # if the player cannot use any boh, moves to next phase
    if current_player.tapped_boh == len(current_player.boh_zone):
        print('you have run out of boh, time to close')
        check_hand_limit(current_player, graphic)
        return
    show_cards(current_player.get_hand())
    
    # player can play as many cards as they can
    while True:
        print_board_graphics(graphic, current_player, other_player)
        end = input('if you want to close, type "close"\n' + 
                'if you want to play a card, type "play"\n' +
                '"show board"\n' +
                '"show discard"\n' + 
                '"show card"\n').strip()
        # ends the turn
        if end == 'close':
            check_hand_limit(current_player, graphic)
            return 
        elif end == 'show board':
            print_board(current_player, other_player)
        elif end == 'show discard':
            show_discard_pile(current_player)
        # if the player wants to know what a card does
        elif end == 'show card':
            show_card(current_player, other_player)
        # plays card
        elif end == 'play':
            play_card(current_player, other_player, the_stack, graphic)
        else:
            print('enter valid command')
        print()
        print('current hand')
        show_cards(current_player.get_hand())

def respond(current_player, other_player, stack, graphic):
    '''
    responds to character summons, spell casts (maybe), and fashion items(maybe)
    a stack of size 1 
    #
    #probably make can_respond_function to shortcut things
    '''
    actual_player = current_player
    # alternates player responses until 'no' command is given
    while True:
        if other_player.tapped_boh == len(other_player.boh_zone):
                print("\nyour opponent has run out of boh, they cannot respond\n")
                return actual_player
        show_cards(other_player.get_hand())
        response = input('do you want to play a spell card in response ' + other_player.name + 
                         '? (yes/no)\n').strip()
        # asks what opponent wants to do
        if response == 'no':
            break
        elif response == 'yes':
            # shows hand and asks what card to play
            print()
            show_cards(other_player.get_hand())
            print_hand_graphics(other_player, graphic)
            card_name = input('what spell card would you like to play in response?' + 
            ' type "no" to exit\n').strip()
            if card_name == 'no':
                break
            if card_in_hand(card_name, other_player):
                card = get_card_from_name(card_name, other_player.hand)
                if card.get_type() == 'SPELL':
                    if current_player.can_play(card):
                        stack.push(card)
                        play_spell_card_graphics(graphic, card)
                        current_player, other_player = other_player, current_player
                    else:
                        print('you cannot play that\n')
                else:
                    print('you cannot play that\n')
        else: 
            print('yes or no')
    # resolves the stack
    resolve_stack(current_player, other_player, stack, graphic)
    return actual_player

def resolve_stack(current_player, other_player, stack, graphic):
    '''
    should replace code in respond()
    '''
    while not stack.is_empty():
        if stack.size() % 2 == 1:
            player = other_player
            other_player = current_player
        else:
            player = current_player
            other_player = other_player
        card = stack.pop()
        card_name = card.get_name()
        # maybe also be able to play equip cards
        player.play_spell_card(other_player, card_name)
    # need to make a function to activate special bs spell effects

def print_board(current_player, other_player):
    '''
    prints board
    '''
    curr_tapped_boh = current_player.tapped_boh
    other_tapped_boh = other_player.tapped_boh
    curr_total_boh = len(current_player.boh_zone)
    other_total_boh = len(other_player.boh_zone)
    print()
    print('opposing side:\n')
    print('total boh: ' + str(other_total_boh) + ' tapped boh: ' + str(other_tapped_boh))
    print()
    print('t&a zone:')
    print_t_and_a_zone(other_player)
    print('floor stats:')
    show_floor_stats(other_player.floor_zone)
    print('floor zone:')
    show_cards(other_player.floor_zone)
    print('your side:\n')
    print('floor zone:')
    show_cards(current_player.floor_zone)
    print('floor stats:')
    show_floor_stats(current_player.floor_zone)
    print('t&a zone:')
    print_t_and_a_zone(current_player)
    print('total boh: ' + str(curr_total_boh) + ' tapped boh: ' + str(curr_tapped_boh))
    print()

def print_t_and_a_zone(player):
    '''
    prints t&a zone
    '''
    t_and_a_representation = []
    for card in player.t_and_a_zone:
        if card is None:
            t_and_a_representation.append('Empty')
        else:
            t_and_a_representation.append('Card')
    print(t_and_a_representation)
    print()

def conduct_character_attack(attacker, current_player, defender, other_player, graphic):
    defender = get_card_from_name(defender, other_player.floor_zone)
    while True:
        chosen_stat = input('what stat do you want to attack with\n' +
                            '"loyalty", "truck", "garment care"\n').strip()
        if has_blocker(other_player, graphic):
            defender = change_attack_target(other_player, defender)
        if chosen_stat == 'loyalty':
            attacker_stat = attacker.get_loyalty_stat()
            defender_stat = defender.get_loyalty_stat()
            break
        elif chosen_stat == 'truck':
            attacker_stat = attacker.get_truck_stat()
            defender_stat = defender.get_truck_stat()
            break
        elif chosen_stat == 'garment care':
            attacker_stat = attacker.get_garment_care_stat()
            defender_stat = defender.get_garment_care_stat()
            break
        else:
            print('enter a valid stat')
    the_stack = Stack()
    if has_boh(other_player):
            respond(current_player, other_player, the_stack, graphic)
    attacker.tap()
    if attacker_stat > defender_stat:
        # attacker wins
        remove_from_floor(defender, other_player, current_player)
        print(defender.get_name() + ' was eliminated\n')
        show_cards(other_player.floor_zone)
    elif attacker_stat < defender_stat:
        # defender wins
        remove_from_floor(attacker, current_player, other_player)
        print(attacker.get_name() + ' was eliminated\n')
        show_cards(current_player.floor_zone)
    else:
        print('It was a tie, no one is eliminated\n')
        print()
    print_board_graphics(graphic, current_player, other_player)

def remove_from_floor(target_card, loser_player, winner_player):
    '''
    makes card die, will probably need affecting_spells varaible in character cards
    which will function like equipped_cards in order to remove spell buffs correctly
    cuz i cant access the spell cards bythemselves when something dies.
    if it dies, if the thing is multitarget then we have to deal with that then
    '''
    card_position = 0
    count = 0
    for card in loser_player.floor_zone: 
        if card == target_card:
            # resets data stored by Card Object
            target_card.set_position(None)
            equipped_cards = target_card.get_equipped_cards()
            # removes equip cards
            for equip_card in equipped_cards:
                equip_card.unapply_factors()
                equip_card.remove_effects()
                equip_card.set_target(None)
                owner = check_owner(loser_player, winner_player, equip_card)
                owner.discard_pile.add(equip_card)
            target_card.remove_equipped_cards(None)
            # removes Spell cards
            spells = target_card.get_spell_cards()
            for spell in spells:
                spell.unapply_factors()
                target_card.remove_effects(spell.get_effects())
                spell.get_targets().remove(target_card)
                if len(spell.get_targets()) == 0:
                    owner = check_owner(loser_player, winner_player, spell)
                    owner.discard_pile.add(spell)
            target_card.remove_spell_cards(None)
            # sends card to discard pile
            loser_player.discard_pile.add(target_card)
            card_position = count
        count += 1
    loser_player.current_num_on_floor -= 1
    loser_player.floor_zone[card_position] = None

def check_owner(current_player, other_player, card):
    if card.get_owner() == current_player.name:
        owner = current_player
    else:
        owner = other_player
    return owner

def conduct_direct_attack(attacker, current_player, other_player, graphic):
    '''
    conducts a direct attack, uses play form t&a zone
    '''
    target_num = 1
    if 'double t&a' in attacker.get_effects():
        target_num = 2
        if t_and_a_zone_cards_left(other_player) == 1:
            target_num = 1
    attacker.tap()
    for i in range(target_num):
        if not list_is_empty(other_player.floor_zone):
            return
        while True:
            target = input('enter the position of the t&a card you ' +  
                           'want to attack\n').strip()
            if target.isnumeric():
                target = int(target) - 1
                if other_player.t_and_a_zone[target] is None:
                    print('there is no t&a card there, select another')
                elif int(target) > 4 or int(target) < 0:
                    print('enter a number 1-5')
                else:
                    break
            else:
                print('enter a number 1-5')
        # might be useless
        print_board_graphics(graphic, current_player, other_player)
        print('they have recieved a t&a infraction, will they play it?\n')
        print_card_graphics(graphic, other_player.t_and_a_zone[target], 55, 330)
        other_player.play_from_t_and_a_zone(other_player, target)

def change_player(current_player, other_player):
    '''
    changes player
    '''
    return other_player, current_player

def return_player(current_player, board):
    '''
    returns current players name
    '''
    player_string = ''
    if current_player == board.player_one:
        player_string = 'player 1:'
    else:
        player_string = 'player 2:'
    return player_string
    
def show_cards(card_list):
    '''
    shows list of card objects' names
    '''
    card_name_list = []
    for card in card_list:
        if card is not None:
            card_name_list.append(card.get_name())
        else:
            card_name_list.append(None)
    print(card_name_list)

def show_t_and_a(card_list):
    'shows cards in t_and_a zone but probably wont use except for debugging'
    card_name_list = []
    for card in card_list:
        card_name_list.append(card)
    return card_name_list

def show_floor_stats(card_list):
    '''
    shows character stats on floor, not implemented yet but will be a command
    make one for hand that reads effects and stats 
    show_floor_effects
    show_hand_stats, 
    show_hand_effects,
    '''
    card_stat_list = []
    for card in card_list:
        if card is not None:
            card_stat_list.append(card.get_stats())
        else:
            card_stat_list.append(None)
    print(card_stat_list)
    print()


def get_card_from_name(card_name, card_list):
    '''
    super imporant, gets Card object from String, error checking not done in function
    must be done before calling, card_list is usually hand, or board
    '''
    for card in card_list:
        if card is not None:
            if card.get_name() == card_name:
                return card
    print('card was not present in that list')
    print(card_list)
    return card_name

def card_in_hand(card_name, current_player):
    '''
    returns if the Card object is in a hand using its name
    '''
    card_name_list = []
    for card in current_player.hand:
        card_name_list.append(card.get_name())
    if card_name not in card_name_list:
        return False
    else:
        return True

def card_on_floor(card_name, current_player):
    '''
    checks if the card is on the floor based off name and player
    '''
    card_name_list = []
    for card in current_player.floor_zone:
        if card is not None:
            card_name_list.append(card.get_name())
        else:
            card_name_list.append(None)
    if card_name not in card_name_list:
        return False
    else:
        return True
    
def can_attack(current_player):
    '''
    checks if player can attack
    '''
    for character in current_player.floor_zone:
        if character is not None:
            if not character.is_tapped():
                return True
    return False

def list_is_empty(card_list):
    '''
    checks if any list of cards is empty
    '''
    for card in card_list:
        if card is not None:
            return False
    return True

def t_and_a_zone_cards_left(player):
    '''
    returns the amount of T&A cards left in a player's zone
    '''
    count = 0
    for card in player.t_and_a_zone:
        if card is not None:
            count += 1
    return count

def show_discard_pile(player):
    '''
    shows the player's discard pile
    '''
    card_names = []
    for card in player.discard_pile:
        card_names.append(card.get_name())
    print(card_names)

def has_blocker(player, graphic):
    '''
    checks if there is a card with "blocker" on the Floor
    '''
    for card in player.floor_zone:
        if card is not None:
            for effect in card.get_effects():
                if effect == 'blocker':
                    show_to_opponent(graphic, card)
    
                    return True
    return False

def has_boh(player):
    '''
    checks if player has any untapped boh
    '''
    if player.tapped_boh == len(player.boh_zone):
        return False
    else:
        return True

def change_attack_target(other_player, defender):
    '''
    changes attack target specifcally if there is a character with "blocker" ability
    '''
    print()
    print(other_player.name + '\none or more of you cards has "blocker"')
    blockers = []
    blocker_names = []
    # prompts user if they want to switch attack targets based on abilit
    while True:
        confirm = input('would you like to change the target of the attack? (yes/no)\n').strip()
        if confirm == 'yes':
            for card in other_player.floor_zone:
                if card is not None:
                    if 'blocker' in card.get_effects():
                        blockers.append(card)
                        blocker_names.append(card.get_name())
            break
        elif confirm == 'no':
            return defender
        else:
            print('that is not a valid command')
    # gets card and returns the new target
    while True:
        print(blocker_names)
        card_name = input('which card would you like to switch to?\n').strip()
        if card_name in blocker_names:
            defender = get_card_from_name(card_name, blockers)
            return defender
        else:
            print('enter a valid card')

def check_hand_limit(current_player, graphic):
    if len(current_player.hand) > 10:
        while True:
            show_cards(current_player.hand)
            print_hand_graphics(current_player, graphic)
            card_name = input('please select card to discard\n').strip()
            if card_in_hand(card_name, current_player):
                print(card_name + ' was discarded\n')
                card = get_card_from_name(card_name, current_player.hand)
                current_player.discard(card)
                break
            else: 
                print('that is not a valid card\n')

def show_card(current_player, other_player):
    '''
    Shows a card on the floor or in a current_player's hand
    prints description
    '''
    while True:
        card_name = input('enter the card you wish to examine? (card name/no)\n').strip()
        if card_in_hand(card_name, current_player) or card_on_floor(card_name, current_player) \
            or card_on_floor(card_name, other_player):
            break
        elif card_name == 'no':
            return
        else:
            print('enter a valid card\n')
    # check for opponents card
    if card_on_floor(card_name, other_player):
        while True:
            command = input("would you like to examine your opponent's card?  (yes/no)\n").strip()
            if command == 'yes':
                card = get_card_from_name(card_name, other_player.floor_zone)
                break
            if command == 'no':
                break
    # check for card on controller's floor
    if card_on_floor(card_name, current_player):
        card = get_card_from_name(card_name, current_player.floor_zone)
    # check for card in controller's hand
    elif card_in_hand(card_name, current_player):
        card = get_card_from_name(card_name, current_player.hand)
    #print card info
    print()
    print('card name: ' + card.get_name())
    print('card type: '+ card.get_type())
    if card.get_type() in CHARACTER_TYPES:
        print('card stats: ')
        print('loyalty: ' + str(card.get_loyalty_stat()))
        print('truck: ' + str(card.get_truck_stat()))
        print('garment care: ' + str(card.get_garment_care_stat()))
        print('stress level: ' + str(card.get_stress_level()))
    print('effects: ')
    card.get_effect_descriptions()
    print()
    print(card.get_flavor_text())
    print()
    print('cost: ' + str(card.get_cost()))
    if card_on_floor(card_name, current_player):
        print()
        equipped_cards = []
        for equip_card in card.get_equipped_cards():
            equipped_cards.append(equip_card.get_name())
        print('equipped cards: ' + str(equipped_cards))
        print()
        spell_cards = []
        for spell_card in card.get_spell_cards():
            spell_cards.append(spell_card.get_name())
        print('spell cards: ' + str(spell_cards))

def check_in_list_from_name(card_name, card_list):
    card_name_list = []
    for card in card_list:
        if card is not None:
            card_name_list.append(card.get_name())
    if card_name in card_name_list:
        return True
    else:
        return False

def get_card(current_player):
    '''
    literally just so i can test, maybe used later

    DOES NOT HAVE bug:

    cannot get card if the card is within the t&a zone

    '''
    while True:
        card_name = input('what card do you want?\n').strip()
        if check_in_list_from_name(card_name, current_player.deck.get_list()):
            target = get_card_from_name(card_name, current_player.deck.get_list())
            current_player.deck.get_list().remove(target)
            current_player.hand.append(target)
            current_player.shuffle_deck()
            break
        else:
            print('enter valid card')

def print_board_objects(current_player, other_player):
    '''
    tester function
    '''
    print('begin check')
    print(current_player.floor_zone)
    print(other_player.floor_zone)
    print('end of check')

main()