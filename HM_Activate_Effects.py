from HM_Card_List import CHARACTER_TYPES
from HM_The_Hiring_Graphics import*
import random

def activate_effects(played_card, current_player, other_player, graphic):
    '''
    should be called in HM_THE HIRING GAME WHATEVER class 
    every turn unless its a turn effect, in which case it should
    be activate_floor_effects maybe
    '''
    print()

def activate_floor_effects(current_player, other_player, graphic):
    '''
    should be able to activate every beginning of turn in order to increase 
    stats if necessary
    '''
    print()


def check_effects(played_card, current_player, other_player, graphic):
    '''
    card is a Card Object, checks what effects it has
    and selects appropriate check functionc
    '''
    # activated each effect in card.get_effects()
    if played_card.get_type() == 'VISUAL':
        choose_one_effect(played_card, current_player, graphic)
    for effect in played_card.get_effects():
        action_text = 'ABILITY ACTIVATE: \n' 
        text = effect
        print(action_text + text + '\n')
        print_actions(graphic, action_text, text)
        # checks the type of card to select effect
        if played_card.get_type() in CHARACTER_TYPES:
            check_character_effects(played_card, current_player, other_player, effect, graphic)
        elif played_card.get_type() == 'SPELL':
            check_spell_effects(played_card, current_player, other_player, effect, graphic)
        elif played_card.get_type() == 'FASHIONITEM':
            check_fashion_item_effects(played_card, current_player, other_player, effect, graphic)
    
    # changes effect to activated
    played_card.effect_activated = True
    print_general_actions(graphic, 'press enter to continue', True)
    input('press enter to continue\n')

def check_character_effects(played_card, current_player, other_player, effect, graphic):
    '''
    checks all character effects against effect argument
    '''
    if effect == 'draw':
        draw_effect(played_card, current_player, graphic)
    elif effect == 'enrique': # works
        enrique_effect(played_card, graphic)
    elif effect == 'backstock': # works
        backstock_effect(played_card, current_player, graphic)
    elif effect == 'starbs':
        starbs_effect(played_card, current_player, graphic)
    elif effect == 'backup to cashpoint':
        backup_to_cashpoint_effect(played_card, current_player, graphic)
    elif effect == 'check the totes':
        check_the_totes_effect(played_card, current_player, graphic)
    elif effect == 'hate crime':
        hate_crime_effect(played_card, current_player, other_player, graphic)
    elif effect == 'put on hold':
        put_on_hold(played_card, current_player, graphic)
    elif effect == "gott'em":
        gottem_effect(played_card, current_player)
    elif effect == 'tech pants':
        tech_pants_effect(played_card, current_player, graphic)
    elif effect == 'sample pick i':
        sample_pick_i_effect(played_card, current_player, graphic)
    # do the stupid visual choose one function
    elif effect == 'refill':
        refill_effect(played_card, current_player, graphic)
    elif effect == 're-hang':
        rehang_effect(played_card, current_player, graphic)
    elif effect == 'sample pick ii':
        sample_pick_ii_effect(played_card, current_player, graphic)
    elif effect == 'refresh':
        refresh_effect(played_card, current_player, graphic)
    elif effect == 'scheduling':
        scheduling_effect(played_card, current_player, graphic)
        
def check_spell_effects(played_card, current_player, other_player, effect, graphic):
    # spell and fashion item effects are strings as opposed to Lists, may have to fix
    # card format
    if effect == 'starbucks!':
        starbucks_effect(played_card, current_player, other_player, graphic)
    elif effect == 'call hod!':
        call_hod_effect(played_card, current_player, graphic)
    elif effect == 'fill the fridge!':
        fill_the_fridge_effect(played_card, current_player, graphic)
    elif effect == 'use our app!':
        use_our_app(played_card, current_player, graphic)
    elif effect == 'dress coded!':
        dress_coded_effect(played_card, current_player, other_player, graphic)
    elif effect == 'hr call!':
        hr_call_effect(played_card, graphic)
    elif effect == 'bad wifi!':
        bad_wifi_effect(played_card, graphic)
    elif effect == 'b.o.r.e. stickering!':
        bore_stickering_effect(played_card, graphic)
    elif effect == 'callout!':
        print('callout print')
    elif effect == "you're fired!":
        youre_fired_effect(played_card, current_player, other_player, graphic)
    elif effect == 'commercial move!':
        commercial_move_effect(played_card, current_player, other_player, graphic)
    elif effect == 'district walk!':
        district_walk_effect(played_card, current_player, other_player, graphic)
    elif effect == '15-minute break!':
        fifteen_minute_break_effect(played_card, current_player, graphic)
    elif effect == 'i quit!':
        i_quit_effect(played_card, current_player, other_player, graphic)
def check_fashion_item_effects(played_card, current_player, other_player, effect, graphic):
    print('fashion item print')
    



'''
The Character Effect Functions

'''

def draw_effect(played_card, current_player, graphic):
    '''
        This function makes the current_player draw a Card.
        It then saves the drawn Card

        Arguments: card, Card Object
                   current_player, Player Object
                   graphic, graphics Object
        Return Values: n/a
        '''
    print('draw was activated')
    drawn_card = current_player.draw()
    print_draw_graphics(graphic, drawn_card)
    print_actions(graphic, None, None,'draw 1')

def enrique_effect(played_card, graphic):
    '''
        This function makes the Card Object passed
        Immune to Spells and Fashion Items by setting
        Card.immune = True 

        Arguments: card, Card Object
                   graphic, graphics Object
        Return Values: n/a
    '''
    played_card.immune = True
    print_actions(graphic, None, None, 'character is immune')

def backstock_effect(played_card, current_player, graphic):
    '''
        This function makes the current_player add a Card
        from their hand to their boh zone. It then taps()
        the Card so it cannot be used during the turn this ability
        is played.

        Arguments: card, Card Object
                   current_player, Player Object
                   graphic, graphics Object
        Return Values: n/a
    '''
    show_cards(current_player.get_hand())
    print_tiny_card_list_corner_vertical(graphic, current_player.hand, len(current_player.hand))
    # asks what card to put in boh zone
    print_actions(graphic, None, None, 'select 1')
    while True:
        card_name = input('which card do you want to put into your ' + 
                          'boh zone?\n').strip()
        if check_in_list_from_name(card_name, current_player.hand):
            current_player.play_boh(card_name)
            # taps the card that was put into boh zone
            for card in current_player.boh_zone:
                if card.get_name() == card_name:
                    card.tap()
            break
        else: 
            print('that is not a valid card\n')
    print('\nboh zone:')
    show_cards(current_player.boh_zone)
    #print_board_graphics(graphic, current_player, other_player)

def blocker_effect(played_card, current_player, graphic):
    '''
    blocker is handled within the HM_Game main function
    '''
    print('blocker print')

def starbs_effect(played_card, current_player, graphic):
    '''
    starbs is handled within the starbucks_effect spell function
    '''
    print('starbs print')

def backup_to_cashpoint_effect(played_card, current_player, graphic):
    '''
        This function makes the current_player select another
        Character Card they control. Said Card is then made immune
        which is visually represented by giving them the 'Enrique' 
        ability.

        Arguments: card, Card Object
                   current_player, Player Object
                   graphic, graphics Object
        Return Values: n/a
    '''
    # checks if there is a target
    print('backup to cashpoint activated, please select a target')
    print_actions(graphic, None, None, 'select other character')
    if is_targets(played_card, current_player.floor_zone):
        # finds target
        while True:
            target = ''
            card_name = input('enter the name of another character card you control\n').strip()
            for card in current_player.floor_zone:
                if card is not None:
                    if card.get_name() == played_card.get_name():
                        break
                    elif card.get_name() == card_name:
                        target = card
            if target not in current_player.floor_zone:
                print('please enter valid target for this effect')
            else:
                break
        # gives target enrique ability and makes immune
        target.immune = True
        target.add_effects('enrique')
    else:
        print_general_actions(graphic, 'no target')
        print('no valid targets for ability, it is ignored\n')

            
def check_the_totes_effect(played_card, current_player, graphic):
    '''
        This function reveals the top 3 Cards to the current_player.
        It then makes them select 1 Card to add to their hand.
        Of the remaining cards, the current_player is asked to select
        1 to add to their hand. The remaining card is placed on the 
        bottom of their deck.

        Arguments: card, Card Object
                   current_player, Player Object
                   graphic, graphics Object
        Return Values: n/a
    '''
    # gets the top 3 cards
    card_one = current_player.deck.pop()
    card_two = current_player.deck.pop()
    card_three = current_player.deck.pop()
    three_cards = [card_one, card_two, card_three]
    # asks which card to keep
    while True:
        print_card_list_corner(graphic, three_cards, 3)
        print_actions(graphic, None, None, 'select 1 to keep, and 1 to go on top')
        card_name = input('enter which card you would like to keep\n').strip()
        # adds card to hand
        if check_in_list_from_name(card_name, three_cards):
            target = get_card_from_name(card_name, three_cards)
            current_player.hand.append(target)
            three_cards.remove(target)
            break
        else:
            print('select valid card name\n')
    # asks with card to place on top of deck
    while True:
        print_card_list_corner_without_card(graphic, target, three_cards, 2, 1)
        card_name = input('enter which card you would like to put on the top\n').strip()
        if check_in_list_from_name(card_name, three_cards):
            # puts card on top
            target = get_card_from_name(card_name, three_cards)
            current_player.deck.push(target)
            three_cards.remove(target)
            # puts other card on bottom
            current_player.deck.put_on_bottom(three_cards[0])
            break
        else:
            print('select valid card name\n')
    
def hate_crime_effect(played_card, current_player, other_player, graphic):
    '''
        This function asks the current_player to target 1 of their opponent's
        Cards in their floor zone. It then taps() that Card until after 
        your next turn. 

        Arguments: card, Card Object
                   current_player, Player Object
                   other_palyer, Player Object
                   graphic, graphics Object
        Return Values: n/a
    '''
    # checks for target
    if is_targets(played_card, other_player.floor_zone):
        print_actions(graphic, None, None, 'select target character')
        # finds target
        while True:
            card_name = input('enter which card you like to target?\n').strip()
            if check_in_list_from_name(card_name, other_player.floor_zone):
                target = get_card_from_name(card_name, other_player.floor_zone)
                # taps for 1 turn counter
                tap_for_x_turns(target, 1)
                print(target.get_name() + ' cannot be untapped until after your next turn\n')
                break
    else:
        print_general_actions(graphic, 'no target')
        print('no valid targets for ability, it is ignored\n')


def put_on_hold(played_card, current_player, graphic):
    '''
        This function asks the current_player to select 1 of the
        Fashion Item Cards in their deck. They add the selected Card
        to their hand. The rest are put back in the deck and the deck is 
        shuffled(). The selected Card is not able to be played until
        their next turn.

        Arguments: card, Card Object
                   current_player, Player Object
                   other_palyer, Player Object
                   graphic, graphics Object
        Return Values: n/a
    '''
    # gets list of fashion items
    fashion_items_list = []
    for card in current_player.deck.get_list():
        if card.get_type() == 'FASHIONITEM':
            fashion_items_list.append(card)
    if len(current_player.boh_zone) == 0:
        print_general_actions(graphic, 'no target')
        print('no valid targets for ability, it is ignored\n')
        return
    # asks to pick 1
    print_actions(graphic, None, None, 'select 1')
    while True:
        show_cards(fashion_items_list)
        print_tiny_card_list_corner_vertical(graphic, fashion_items_list, len(fashion_items_list))
        card_name = input('enter the name of the fashion item you want\n').strip()
        if check_in_list_from_name(card_name, fashion_items_list):
            # adds target to hand, but cannot be played during turn when activated
            # deck is shuffled and shown to opponent
            target = get_card_from_name(card_name, fashion_items_list)
            target.can_play = False
            target.can_play_turns = 1
            current_player.deck.get_list().remove(target)
            current_player.hand.append(target)
            current_player.shuffle_deck()
            show_to_opponent(graphic, target)
            break
        else:
            print('enter valid target\n')

def gottem_effect(played_card, current_player):
    '''
    will have to be handled like blocker pro3bably
    '''
    print('gottem effect')

def tech_pants_effect(played_card, current_player, graphic):
    '''
        This function retrieves the Techwear Pants Card from the deck
        if it is present. It is shown to the opponent,
        then added to the current_player's hand. It costs 1 less.

        Arguments: card, Card Object
                   current_player, Player Object
                   graphic, graphics Object
        Return Values: n/a
    '''
    # checks if target is in deck
    if check_in_list_from_name('Techwear Pants', current_player.deck.get_list()):
        for card in current_player.deck.get_list():
            if card.get_name() == 'Techwear Pants':
                # adds card to hand and makes it cost 1 less
                # then shows to opponent
                current_player.hand.append(card)
                card.set_cost(card.get_cost() - 1)
                show_to_opponent(graphic, card)
    else:
        print_general_actions(graphic, 'card not in deck')
        print('card not in deck, it is ignored\n')

def sample_pick_i_effect(played_card, current_player, graphic):
    '''
    does work
    '''
    card = current_player.draw()
    print_draw_graphics(graphic, card)
    show_to_opponent(graphic, card)
    if card.get_type() == 'FASHIONITEM':
        print_general_actions(graphic, 'Card was Fashion Item, draw 1')
        print_general_actions(graphic, 'press enter to continue')
        input('press enter key to continue')
        card = current_player.draw()
        print_draw_graphics(graphic, card)

def refill_effect(played_card, current_player, graphic):
    '''
    does work
    '''
    if len(current_player.boh_zone) == 0:
        print_general_actions(graphic, 'no target')
        print('no valid targets for ability, it is ignored\n')
        return
    print_actions(graphic, None, None, 'select 1')
    # asks to pick 1
    boh_zone = current_player.boh_zone
    while True:
        show_cards(current_player.boh_zone)
        print_tiny_card_list_corner_vertical(graphic, boh_zone, len(boh_zone))
        card_name = input('enter the name of the card you want\n').strip()
        if check_in_list_from_name(card_name, boh_zone):
            # adds target to hand and shown to opponent
            target = get_card_from_name(card_name, boh_zone)
            current_player.boh_zone.remove(target)
            current_player.hand.append(target)
            show_to_opponent(graphic, target)
            break
        else:
            print('enter valid target\n')

def rehang_effect(played_card, current_player, graphic):
    '''
    Does work
    '''
    deck = current_player.deck.get_list()
    if len(deck) == 0:
        print_general_actions(graphic, 'no target')
        print('no valid targets for ability, it is ignored\n')
        return
    print_actions(graphic, None, None, 'select 1')
    # asks to pick 1
    while True:
        show_cards(deck)
        print_tiny_card_list_corner_vertical(graphic, deck, len(deck))
        card_name = input('enter the name of the card you want\n').strip()
        if check_in_list_from_name(card_name, deck):
            # adds target to hand and shown to opponent
            # deck is shuffled
            target = get_card_from_name(card_name, deck)
            deck.remove(target)
            current_player.shuffle_deck()
            current_player.hand.append(target)
            show_to_opponent(graphic, target)
            break
        else:
            print('enter valid target\n')

def sample_pick_ii_effect(played_card, current_player, graphic):
    '''
    so far works, kinda OP
    '''
    card = current_player.draw()
    print_draw_graphics(graphic, card)
    show_to_opponent(graphic, card)
    if card.get_type() == 'SPELL':
        print_general_actions(graphic, 'Card was Spell, draw 2')
        print_general_actions(graphic, 'press enter to continue')
        input('press enter key to continue')
        # draw 1
        card = current_player.draw()
        print_draw_graphics(graphic, card)
        print_general_actions(graphic, 'press enter to continue')
        input('press enter key to continue')
        # draw 2
        card = current_player.draw()
        print_draw_graphics(graphic, card)

def refresh_effect(played_card, current_player, graphic):
    # keeps track of hand size when played
    num_cards = len(current_player.hand)
    # puts card back in deck
    for card in current_player.get_hand():
        current_player.deck.push(card)
    # resets hand to 0
    current_player.hand = []
    # shuffles and draws size + 1 # of cards
    current_player.shuffle_deck()
    for i in range(0, num_cards + 1):
        card = current_player.draw()
        print_draw_graphics(graphic, card)
        print_general_actions(graphic, 'press enter to continue\n')
        input('press enter key to continue\n')

def fanny_pack_effect(played_card, current_player, graphic):
    '''
        This function retrieves the Fanny Pack Card from the deck
        if it is present. It is shown to the opponent,
        then added to the current_player's hand. It then costs 0

        Arguments: played_card, Card Object
                   current_player, Player Object
                   graphic, graphics Object
        Return Values: n/a
    '''
    # checks if target is in deck
    if check_in_list_from_name('Fanny Pack', current_player.deck.get_list()):
        for card in current_player.deck.get_list():
            if card.get_name() == 'Fanny Pack':
                # adds card to hand and makes it cost 0
                # then shows to opponent
                current_player.hand.append(card)
                card.set_cost(0)
                show_to_opponent(graphic, card)
    else:
        print_general_actions(graphic, 'card not in deck')
        print('card not in deck, it is ignored\n')

def scheduling_effect(played_card, current_player, graphic):
    if is_targets(played_card, current_player.floor_zone) \
        and check_type_in_list(CHARACTER_TYPES, current_player.hand):
        while True:
            print_general_actions(graphic, 'select target')
            card_name = input('select which target you want to re-schedule\n').strip()
            if card_name == played_card.get_name():
                print('not a valid target\n')
            elif check_in_list_from_name(card_name, current_player.floor_zone):
                floor_target = get_card_from_name(card_name, current_player.floor_zone)
                print_general_actions(graphic, 'select card in hand')
                show_cards(current_player.hand)
                print_hand_graphics(current_player, graphic)
                hand_card_name = input('select card in hand to swap shifts\n').strip()
                if check_in_list_from_name(hand_card_name, current_player.hand):
                    hand_target = get_card_from_name(hand_card_name, current_player.hand)
                    # i also need to check cost
                    if hand_target.get_type() not in CHARACTER_TYPES:
                        print('not valid target')
                    else:
                        switch_card_in_hand(floor_target, hand_target, current_player)
                        break
                else:
                    print('target is not in your hand\n')
            else:
                print('target is not on the floor\n')
    else:
        print_general_actions(graphic, 'no target')
        print('no valid targets for ability, it is ignored\n')













'''

Spell effects


spell effects already have a targeting system that works, so the first while loop in these fucntions that i made arent necessary
'''
def starbucks_effect(played_card, current_player, other_player, graphic):
    target_card = played_card.get_targets()[0]
    # checks for starbs ability
    has_starbs = False
    for card in current_player.floor_zone:
        if card is not None:
            if 'starbs' in card.get_effects():
                has_starbs = True
    # if player has starbs ability
    if has_starbs:
        while True:
            selection = input('do you want heads or tails?\n').strip()
            print_general_actions(graphic, 'type "heads" or "tails"')
            if selection == 'heads':
                target_card.change_base_stats([0, 15, 0])
                target_card.change_stress(-10)
                break
            elif selection == 'tails':
                target_card.change_base_stats([0, -15, 0])
                target_card.change_stress(10)
                break
            else:
                print('type "heads" or "tails"')
    # if played does not have starbs ability
    else:
        # flips coin using random, 
        rand = random.randint(1, 2)
        print_general_actions(graphic, 'to flip, press enter')
        input('to flip coin, press enter\n')
        # if heads, increases stats
        if rand == 1:
            print_general_actions(graphic, 'coin was heads')
            input('coin was heads')
            target_card.change_base_stats([0, 15, 0])
            target_card.change_stress(-10)
        # if tails, decreases stats
        if rand == 2:
            print_general_actions(graphic, 'coin was tails')
            input('coin was tails')
            target_card.change_base_stats([0, -15, 0])
            target_card.change_stress(10)

def call_hod_effect(played_card, current_player, graphic):
    if check_type_in_list('VISUAL', current_player.hand) or check_type_in_list('MANAGER', current_player.hand):
        target = played_card.get_targets()[0]
        target.tap()
        while True:
            show_cards(current_player.hand)
            print_hand_graphics(current_player, graphic)
            card_name = input('select which overhead you want to play\n').strip()
            if check_in_list_from_name(card_name, current_player.hand):
                hand_target = get_card_from_name(card_name, current_player.hand)
                if hand_target.get_type() == 'VISUAL' or hand_target.get_type() == 'MANAGER':
                    new_cost = hand_target.get_cost() - target.get_cost()
                    hand_target.set_cost(new_cost)
                    break
                else:
                    print('choose valid target')
            else:
                print('choose valid target')
    else:
        print('no valid hand target, ability ignored')

def fill_the_fridge_effect(played_card, current_player, graphic):
    # changes stress of all allies
    for card in played_card.get_targets():
            card.change_stress(-15)
    # draws two cards
    for i in range(2):
        card = current_player.draw()
        print_draw_graphics(graphic, card)
        print_general_actions(graphic, 'press enter to continue')
        input('press enter key to continue')
    # discards 2 cards
    for i in range(2):
        while True:
            show_cards(current_player.hand)
            print_hand_graphics(current_player, graphic)
            card_name = input('select card to discard\n').strip()
            if check_in_list_from_name(card_name, current_player.hand):
                target_card = get_card_from_name(card_name, current_player.hand)
                current_player.discard(target_card)
                print_general_actions(graphic, 'card discarded')
                break
            else:
                print('select valid card\n')
    
def use_our_app(played_card, current_player, graphic):
        # THIS ONE IS ONLY ALLIES, fix that later
    played_card.apply_factors()

def dress_coded_effect(played_card, current_player, other_player, graphic):
    # finds Card targets and removes equip cards from the targets
    for target in played_card.get_targets():
        owner = check_owner(target, current_player, other_player)
        for equip_card in target.get_equipped_cards():
            equip_card.unapply_factors()
            equip_card.remove_effects()
            equip_card.set_target(None)
            owner.discard_pile.add(equip_card)
        target.remove_equipped_cards(None)
    print_general_actions(graphic, 'fashion items removed')

def hr_call_effect(played_card, graphic):
    # gets target card and makes it not untap for a turn
    # increases stress by 30
    for target in played_card.get_targets():
        target.tap()
        target.do_not_untap = True
        target.do_not_untap_turns = 1
        target.change_stress(30)
    print_general_actions(graphic, 'im calling ashley')

def bad_wifi_effect(played_card, graphic):
    played_card.apply_factors()
    print_general_actions(graphic, 'wifi doesnt work')

def bore_stickering_effect(played_card, graphic):
    played_card.apply_factors()
    print_general_actions(graphic, 'pain')

def youre_fired_effect(played_card, current_player, other_player, graphic):
    target_card = played_card.get_targets()[0]
    remove_from_floor(target_card, current_player, other_player)
    print_general_actions(graphic, "you're fired!")

# this one down
def commercial_move_effect(played_card, current_player, other_player, graphic):
    print_general_actions(graphic, "we had a move")
    # increases enemy FTSA and PTSA stress by 20
    for card in other_player.floor_zone:
        if card is not None:
            if card.get_type() == 'PTSA' or card.get_type() == 'FTSA':
                card.change_stress(20)
    # decreases ally overhead stress by 10
    for card in current_player.floor_zone:
        if card is not None:
            if card.get_type() == 'VISUAL' or card.get_type() == 'MANAGER':
                card.change_stress(-10)

def district_walk_effect(played_card, current_player, other_player, graphic):
    # increases enemy stress levels by 40
    for card in played_card.get_targets():
            card.change_stress(40)
    # draws card for current_player
    card = current_player.draw()
    print_draw_graphics(graphic, card)

def fifteen_minute_break_effect(played_card, current_player, graphic):
    # gets card
    target_card = played_card.get_targets()[0]
    # sets stats to normal and makes it immune 
    target_card.return_to_OG_stats()
    target_card.immune = True
    # draws a card
    card = current_player.draw()
    print_draw_graphics(graphic, card)
    print_general_actions(graphic, 'press enter to continue')
    input('press enter key to continue')

def i_quit_effect(played_card, current_player, other_player, grpahic):
    target_card = played_card.get_targets()[0]
    if target_card in current_player.hand:
        current_player.discard(target_card)
    else:
        remove_from_floor(target_card, current_player, other_player)
    












'''

Helper functions

'''
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

def check_type_in_list(card_type, card_list):
    for card in card_list:
        if card is not None:
            if card.get_type() == card_type or card.get_type() in card_type:
                return True
    return False

def is_targets(card, card_list):
    '''
    Checks for other targets other than card
    '''
    for cardd in card_list:
        if cardd is not None and not cardd == card and cardd.immune == False:
            return True
    return False

def check_in_list_from_name(card_name, card_list):
    card_name_list = []
    for card in card_list:
        if card is not None:
            card_name_list.append(card.get_name())
    if card_name in card_name_list:
        return True
    else:
        return False

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

def choose_one_effect(card, current_player, graphic):
    index = len(card.get_effects())
    original_effect = card.get_effects()[0]
    effect_one = card.get_effects()[index - 1]
    effect_two = card.get_effects()[index - 2]
    while True:
        effect_name = input('choose ' + effect_one + ' or ' + effect_two + '\n').strip()
        if effect_name in card.get_effects():
            card.set_effects([original_effect, effect_name])
            break
        else:
            print('that is not a valid effect')

def switch_card_in_hand(floor_card, hand_card, player):
    # removes cards attached to floor_card
    equipped_cards = floor_card.get_equipped_cards()
    # removes equip cards
    for equip_card in equipped_cards:
        equip_card.unapply_factors()
        equip_card.remove_effects()
        equip_card.set_target(None)
        player.discard_pile.add(equip_card)
        floor_card.remove_equipped_cards(None)
    # removes Spell cards
    spells = floor_card.get_spell_cards()
    for spell in spells:
        spell.unapply_factors()
        floor_card.remove_effects(spell.get_effects())
        spell.set_target(None)
        # might not work, needs to discard when last one dies
        # spell.remove_target(card)
        # if len(spell.get_targets()) == 0:
        # player.discard_pile.add_spell
        player.discard_pile.add(spell)
        floor_card.remove_spell_cards(None)
    # switches cards
    position = floor_card.get_position()
    print(position)
    hand_card.set_position(position)
    player.floor_zone[position] = hand_card
    player.hand.append(floor_card)
    floor_card.set_position(None)
    player.hand.remove(hand_card)

def check_owner(target_card, current_player, other_player):
    if target_card.get_owner() == current_player.name:
        player = current_player
    else:
        player = other_player
    return player

def remove_from_floor(target_card, current_player, other_player):
    '''
    makes card die, will probably need affecting_spells varaible in character cards
    which will function like equipped_cards in order to remove spell buffs correctly
    cuz i cant access the spell cards bythemselves when something dies.
    if it dies, if the thing is multitarget then we have to deal with that then
    '''
    card_position = 0
    count = 0
    player = check_owner(target_card, current_player, other_player)
    for card in player.floor_zone: 
        if card == target_card:
            # resets data stored by Card Object
            target_card.set_position(None)
            equipped_cards = target_card.get_equipped_cards()
            # removes equip cards
            for equip_card in equipped_cards:
                equip_card.unapply_factors()
                equip_card.remove_effects()
                equip_card.set_target(None)
                owner = check_owner(equip_card, current_player, other_player)
                owner.discard_pile.add(equip_card)
            target_card.remove_equipped_cards(None)
            # removes Spell cards
            spells = target_card.get_spell_cards()
            for spell in spells:
                spell.unapply_factors()
                target_card.remove_effects(spell.get_effects())
                spell.get_targets().remove(target_card)
                if len(spell.get_targets()) == 0:
                    owner = check_owner(spell, current_player, other_player)
                    owner.discard_pile.add(spell)
            target_card.remove_spell_cards(None)
            # sends card to discard pile
            player.discard_pile.add(target_card)
            card_position = count
        count += 1
    player.floor_zone[card_position] = None

'''

do-er functions
'''
def tap_for_x_turns(card, x):
    '''
    taps a card for x amount of turns, used in combination with CharacterCard 
    '''
    card.do_not_untap = True
    card.do_not_untap_turns = x
    card.tap()

