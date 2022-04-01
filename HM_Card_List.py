from HM_Card_Types import CharacterCard, SpellCard, FashionItem
from HM_Effects_List import SPELL_EFFECTS, FASHION_ITEM_EFFECTS, \
    CHARACTER_EFFECTS
""" File: HM_Card_List.py
    Author: Jackson Covey
    Purpose: This program is meant to act as a Card List of the
    cards released in the 1st edition of in a H&M The Hiring TCG.
    It will contain a set of created Card Objects that are hard-coded

    USAGE:
    Creates an ArrayStack that functions as a Stack ADT, while using a java
    Array to store data. It implements the StackInterface and its abstract
    methods.
    arr is the Array where data is actually stored. actualSize is the true
    size of arr as arr needs to be expanded for large data sets. length is
    the amount of data that the ArrayQueue is storing that the user can access.

    Like a normal Stack, ArraySTack is a LIFO which stores data in an array.
    .push() is used to add data after the last accessible element in the
    array.
    .pop() is used to return and remove last accessible data point in arr.
    .peek() returns the data stored at the front, but does not remove it.
    .isEmpty() returns true if the ArrayStack has no data the user can access.
    .size() returns the number of indexes in arr the user can access.
    .clear() resets arr to default settings at time of construction.

    ArrayStack objects can be instantiated with no arguments, or can be copied
    through the copy constructor.
"""


'''
How to make a CharacterCard:
Character_name = CharacterCard(owner, "name", "type", [L,T,GC,S], [effects],
                                flavor text, cost, equipped_card=None)
'''
CHARACTER_TYPES = ['PTSA', 'FTSA', 'VISUAL', 'MANAGER']
# PTSA
estevan = \
    CharacterCard('player 1', "Estevan", "PTSA", [35, 35, 35, 35], ["draw"],
                  '"i gotchu"', 1)

enrique = \
    CharacterCard('player 1', "Enrique", "PTSA", [35, 25, 35, 20],
                  ["enrique", "backstock"], '"baby fight club"', 1, True)

kevin = \
    CharacterCard('player 1', "Kevin", "PTSA", [35, 35, 40, 40], ["blocker"],
                  '''"i'll take an ice water"''', 1)

chadz = \
    CharacterCard('player 1', "Chadz", "PTSA", [6, 9, 42, 0], ["enrique"],
                  '"this is my boyfriend \napplication"', 2, True)

rihanna = \
    CharacterCard('player 1', "Rihanna", "PTSA", [45, 35, 40, 40], ["backup to cashpoint"],
                  '"something in arabic"', 2)

hailee = \
    CharacterCard('player 1', "Hailee", "PTSA", [45, 40, 35, 40], ["check the totes"],
                  '''"i'm calling my lawyer"''', 2)

jonesy = \
    CharacterCard('player 1', "Jonesy", "PTSA", [40, 40, 40, 30], ["starbs"],
                  '"oh sweetie"', 2)

tiana = \
    CharacterCard('player 1', "Tiana", "PTSA", [40, 40, 40, 45], ["hate crime"],
                  '"for the vibes"', 3)

lindsay = \
    CharacterCard('player 1', "Lindsay", "PTSA", [45, 45, 40, 60], ["put on hold"],
                  '"arson"', 3)

sean = \
    CharacterCard('player 1', "Sean", "PTSA", [50, 35, 35, 45], ["gott'em"],
                  '''"you've activated up my \nupdog card"''', 3)

amor = \
    CharacterCard('player 1', "Amor", "PTSA", [50, 50, 40, 50], ["tech pants"],
                  '"something"', 4)

arieanna = \
    CharacterCard('player 1', "Arieanna", "PTSA", [50, 45, 40, 50], ["moral i"],
                  '''"they're all plastics, honey"''', 4)

jackson = \
    CharacterCard('player 1', "Jackson", "PTSA", [40, 50, 40, 50], ["destress i"],
                  '''"we'll get to that when \nwe get to that"''', 4)

mason = \
    CharacterCard('player 1', "Mason", "PTSA", [50, 60, 45, 00], ["stress i"],
                  '"caaaahhhhhpppppyyyyy"', 4)
megan = \
    CharacterCard('player 1', "Megan", "FTSA", [55, 50, 55, 60], ["blocker", "draw"],
                  '''"i'm short"''', 4)

ily = \
    CharacterCard('player 1', "Ily", "FTSA", [50, 55, 55, 60], ["blocker", "backstock"],
                  '''"i'm clocking out"''', 4)

haley = \
    CharacterCard('player 1', "Haley", "FTSA", [45, 55, 70, 65],
                  ["blocker", "sample pick i"], '"something"', 5)

# Visuals

dani = \
    CharacterCard('player 1', "Dani", "VISUAL", [55, 45, 85, 65],
                  ["finger-spacing", "refill", "re-hang"], '"i gotchaaaaa"', 5)

anthony = \
    CharacterCard('player 1', "Anthony", "VISUAL", [60, 40, 90, 70],
                  ["finger-spacing", "sample pick ii", "refresh"],
                  '"hola señor"', 6)

# Managers
cody = \
    CharacterCard('player 1', "Cody", "MANAGER", [70, 55, 75, 65], ["hod", "moral ii"],
                  '"flavor"', 6)

noah = \
    CharacterCard('player 1', "Noah", "MANAGER", [55, 75, 75, 70], ["hod", "truck lead"],
                  '"ya hate to see it"', 7)

charlotte = \
    CharacterCard('player 1', "Charlotte", "MANAGER", [75, 50, 85, 70],
                  ["hod", "destress ii"],  '"ya know what..."', 7)

daniel = \
    CharacterCard('player 1', "Daniel", "MANAGER", [71, 71, 80, 75],
                  ["hod", "double t&a", "scheduling", "stress ii"],
                  '"i need a shirt for tonight"', 8)

'''
All of the Characters in a list
'''
CHARACTER_LIST = \
    [estevan, enrique, kevin, chadz, rihanna, hailee, jonesy,
     tiana, lindsay, sean, amor, arieanna, jackson, mason, megan, ily,
     haley, dani, anthony, cody, noah, charlotte, daniel]

'''
How to make a SpellCard:
SpellCardName = SpellCard(owner, name, type, effects, flavor_text, cost, factors,
                 special=None, special_factors=None, target_num=1, target_type):
'''

# starbucks coin flip multiplies the buffs by -1
starbucks = \
    SpellCard('player 1', "Starbucks!", "SPELL", ["starbucks!"],
              '"anyone want an ice \nwater?"', 3, [0, 15, 0, -10], ['choose'])

# has to call get_special_factors to check if ptsa or ftsa is on the floor
# will probably have to be specially coded
call_hod = \
    SpellCard('player 1', "Call HOD!", "SPELL", ["call hod!"],
              '"HOD pickup!"', 4, [0, 0, 0, 0], ["PTSA", "FTSA"], )

fill_the_fridge = \
    SpellCard('player 1', "Fill the Fridge!", "SPELL", ["fill the fridge!"],
              '"post this on convo!"', 4, [0, 0, 0, -15], ["MANAGER"],
              [0, 0, 0, 0], 5, 'all_allies')

# basic buff that has 2 targets
use_our_app = \
    SpellCard('player 1', "Use our App!", "SPELL", ["use our app!"],
              '"we do have free wifi"', 4, [10, 0, 0, 0],
              [], [0, 0, 0, 0], 2, 'ally')

# has to interact with fashion items, probably specifically coded
dress_coded = \
    SpellCard('player 1', "Dress Coded!", "SPELL", ["dress coded!"],
              '''"you're out of dress code"''', 1, [0, 0, 0, 0],
              ["MANAGER", "VISUAL"])

# has to tap a card, and interact with turns so its an ongoing affect
# will probably be specifically coded
hr_call = \
    SpellCard('player 1', "HR Call!", "SPELL", ["hr call!"],
              '''"i'm calling ashley"''', 3, [0, 0, 0, 30])

# simple debuff
bad_wifi = \
    SpellCard('player 1', "Bad Wifi!", "SPELL", ["bad wifi!"],
              '''"it's okay, the wifi isn't \nworking"''',
              3, [-20, 0, 0, 20])

bore_stickering = \
    SpellCard('player 1', "B.O.R.E. Stickering!", "SPELL",
              ["b.o.r.e. stickering!"],
              '"today you are stickering \nb.o.r.e."', 4, [-15, 0, -15, 20])

# has to interact with board, do buff, then undo buff.
# has to be individually coded
callout = \
    SpellCard('player 1', "Callout!", "SPELL", ["callout!"],
              '"someone called out"', 5, [0, 0, 0, 30])

# has to interact with the board.
youre_fired = \
    SpellCard('player 1', "You're Fired!", "SPELL", ["you're fired!"],
              '"someone called out"', 5, [0, 0, 0, 0], ["MANAGER"])

# simple debuff with special condition debuffs
commercial_move = \
    SpellCard('player 1', "Commercial Move!", "SPELL", ["commercial move!"],
              '"uh oh"', 6, [0, 0, 0, 20], ["MANAGER", "VISUAL"],
              [0, 0, 0, -10], 10, "AOE")

# simple debuff
district_walk = \
    SpellCard('player 1', "District Walk!", "SPELL", ["district walk!"],
              '"big rip"', 7, [0, 0, 0, 40], [], [], 5, "all_opponents")

# has to somehow call the opoosing spells' undo_buffs() functions
# prob modify this factors by using get_factors from
fifteen_minute_break = \
    SpellCard('player 1', "15-minute Break!", "SPELL", ["15-minute break!"],
              '"when is my 15"', 2, [0, 0, 0, 0], [], [0, 0, 0, 0])

# has to interact with floor
i_quit = \
    SpellCard('player 1', "I Quit!", "SPELL", ["i quit!"],
              '"bye"', 1, [0, 0, 0, 0], [], [], 1, 'ally\\hand')

# has to interact with floor
lunch = \
    SpellCard('player 1', "Lunch!", "SPELL", ["lunch!"],
              '"when is my lunch"', 2, [0, 0, 0, 0])

re_hire = \
    SpellCard('player 1', "Re-Hire!", "SPELL", ["re-hire!"],
              '"welcome back"', 5, [0, 0, 0, 0])

'''
All of the Spells in a list
'''
SPELL_LIST = [starbucks, call_hod, fill_the_fridge, use_our_app,
              dress_coded, hr_call, bad_wifi, bore_stickering, callout,
              youre_fired, commercial_move, district_walk,
              fifteen_minute_break, i_quit, lunch, re_hire]

'''
How to make a FashionItem:
FashionItemName = FashionItem(owner, name, type, effects, text, cost, factors,
                              target=None, added_effects=None):
'''
# maybe make a special variable, and create a list of special effects/cards
# that can check and be like if special_var is not None: check what it is?
# most likely that will be the most effective strategy

# come back to fanny pack this and code the special conditions
fanny_pack = \
    FashionItem('player 1', 'Fanny Pack', 'FASHIONITEM', ['fanny pack'],
                '"i want the h&m fanny \npack"', 2, [0, 0, 10, 0])

pilgrim_collar = \
    FashionItem('player 1', 'Pilgrim Collar', 'FASHIONITEM', ['pilgrim collar'], '"ew"',
                1, [10, 0, 10, 0])

sunday_club_shirt = \
    FashionItem('player 1', 'Sunday Club Shirt', 'FASHIONITEM', ['sunday club shirt'],
                '"we should all buy this"', 2, [0, 0, 0, 0], None, 'moral i')

pleated_skirt = \
    FashionItem('player 1', 'Pleated Skirt', 'FASHIONITEM', ['pleated skirt'],
                '"kilt day"', 3, [10, 0, 0, -10])

techwear_pants = \
    FashionItem('player 1', 'Techwear Pants', 'FASHIONITEM', ['techwear pants'],
                '''"they're only $120"''', 3, [5, 5, 5, 5], None, "gott'em")

# come back to fedora to do the card draw thing
fedora = \
    FashionItem('player 1', 'Fedora', 'FASHIONITEM', ['fedora'],
                '"daniel on a night out"', 4, [10, 10, 10, 10])

# come back to this one to do special abilities
the_breakdown = \
    FashionItem('player 1', 'The Breakdown', 'FASHIONITEM', ['the breakdown'],
                '"where did I put my breakdown?"', 4, [5, 5, 5, 10], None, "hod")

cobras = \
    FashionItem('player 1', "Cobra's", 'FASHIONITEM', ["cobra's"],
                '"the daniel pants', 5, [10, 10, 10, -20])

pimp_jacket = \
    FashionItem('player 1', 'Pimp Jacket', 'FASHIONITEM', ['pimp jacket'],
                '"i look like a pimp now"', 6,
                [0, 0, 0, 0], None, 'double t&a')
# blazer has an issue maybe, need to be able to play on opponents cards
blazer = \
    FashionItem('player 1', 'Blazer', 'FASHIONITEM', ['blazer'],
                '"fancy day"', 2, [-10, -10, -10, 20])

two_weeks_notice = \
    FashionItem('player 1', '2 Weeks Notice', 'FASHIONITEM', ['2 weeks notice'],
                '''"i'm putting in my two weeks"''', 3, [0, 0, 0, 0])

FASHION_ITEM_LIST = [fanny_pack, pilgrim_collar, sunday_club_shirt,
                     pleated_skirt, techwear_pants, fedora, the_breakdown,
                     cobras, pimp_jacket, blazer, two_weeks_notice]


CARD_LIST = CHARACTER_LIST + SPELL_LIST + FASHION_ITEM_LIST
CARD_SET = set(CARD_LIST)

for card in CARD_SET:
    card.set_cost(0)

def test_stats_boost():
    '''
    # add 1 fashionitem
    daniel.add_equipped_cards(fanny_pack)
    print(daniel.get_stats())
    fanny_pack.set_target(daniel)
    fanny_pack.apply_factors()
    print(daniel.get_OG_stats())
    print(daniel.get_stats())
    print(daniel.get_equipped_cards())
    print()
    # add another fashion item
    daniel.add_equipped_cards(pilgrim_collar)
    print(daniel.get_stats())
    pilgrim_collar.set_target(daniel)
    pilgrim_collar.apply_factors()
    print(daniel.get_OG_stats())
    print(daniel.get_stats())
    print(daniel.get_equipped_cards())
    print()
    # attempt to remove a fashion item
    daniel.remove_equipped_cards()
    pilgrim_collar.unapply_factors()
    fanny_pack.unapply_factors()
    fanny_pack.set_target(None)
    pilgrim_collar.set_target(None)
    print(daniel.get_stats())
    print(daniel.get_equipped_cards())
    print()
    daniel.add_equipped_cards(fanny_pack)
    print(daniel.get_stats())
    fanny_pack.set_target(daniel)
    fanny_pack.apply_factors()
    print(daniel.get_OG_stats())
    print(daniel.get_stats())
    print(daniel.get_equipped_cards())
    print()
    '''
    # add another fashion item
    daniel.add_equipped_cards(pilgrim_collar)
    print(daniel.get_stats())
    pilgrim_collar.set_target(daniel)
    pilgrim_collar.apply_factors()
    print(daniel.get_OG_stats())
    print(daniel.get_stats())
    print(daniel.get_equipped_cards())
    daniel.remove_equipped_cards()
    print(daniel.get_equipped_cards())

def card_test(card):
    # 100% works from what I've tested
    card.play()
    print(card.get_name())
    print(card.get_type())
    print(card.get_effects())
    print(card.get_effect_descriptions())
    print(card.get_flavor_text())
    print(card.get_cost())
    card.set_cost(5)
    print(card.get_cost())
    print(card.tap())
    print(card.untap())
    card.set_owner('me')
    print(card.get_owner())

def fashion_item_test():
    # 100% works from what I've tested
    for card in FASHION_ITEM_LIST:
        card.set_target(daniel)
        # print(daniel.get_stats())
        card.apply_factors()
        # print(daniel.get_stats())
        card.unapply_factors()
        card.get_added_effects()
        card.give_effects()
        # print(daniel.get_effects())
        card.remove_effects()
        # print(daniel.get_effects())

# fashion_item_test()

def spell_test():
    # works as far as i know
    for card in SPELL_LIST:
        card = starbucks
        # card_test(card)
        # getter method test
        print(card.get_factors())
        print(card.get_special())
        print(card.get_targets())
        print(card.get_target_num())
        print('daniels stats')
        print(daniel.get_stats())
        print()
        # setter method test
        card.set_targets([daniel])
        card.set_target_num(1)
        card.apply_factors()
        print('the new stats')
        print(daniel.get_stats())
        card.unapply_factors()
        [print('the undone stats?')]
        print(daniel.get_stats())
        print('done')
        # functionality test

# spell_test()

def character_test():
    print('\n equip card testing')
    # revisit these functions after coding FashionItems
    print(dani.get_equipped_cards())
    daniel.add_equipped_cards('a')

    print(daniel.get_equipped_cards())
    '''
    daniel.remove_equipped_cards()
    print(daniel.get_equipped_cards())

    print('next test')
    print('\n equip card testing')
    # revisit these functions after coding FashionItems
    print('dani')
    print(jackson.get_equipped_cards())
    print(dani.get_equipped_cards())
    '''
    '''
    for name in CHARACTER_LIST:
        card_test(name)

        print(name.get_name())
        print(name.get_stats())
        print(name.get_loyalty_stat())
        print(name.get_truck_stat())
        print(name.get_garment_care_stat())
        print(name.get_effects())
        print(name.get_effect_descriptions())
        print(name.get_flavor_text())
        print(name.set_cost(0))
        print(name.get_cost())
        print(name.tap())
        print(name.untap())
        print(name.untap())
        print(name.tap())
        print(name.get_stats())
        print(name.get_OG_stats())
        print(name.get_loyalty_stat())
        print(name.get_truck_stat())
        print(name.get_garment_care_stat())
        print(name.get_stress_level())
        print(name.get_total_stats())
        name.change_stress(50)
        print(name.get_stats())
        name.change_stress(-50)
        print(name.get_stats())
        name.change_base_stats([0, 0, 5, 10])
        print(name.get_stats())
        name.change_base_stats([5, 0, 0, 10])
        print(name.get_stats())
        name.change_base_stats([0, 5, 0, 10])
        print(name.get_stats())
        name.change_base_stats([-4, 20, -50, 10])
        print(name.get_stats())

        print(name.get_effects())
        name.add_effects(['tech pants', "gott'em"])
        print(name.get_effects())
        name.remove_effects(['tech pants', "gott'em"])
        print(name.get_effects())

        print('\n equip card testing')
        # revisit these functions after coding FashionItems
        print(name.get_equipped_cards())

        name.add_equipped_cards(techwear_pants)
        print(name.get_equipped_cards())
        #name.remove_equipped_cards(techwear_pants)
        #print(name.get_equipped_cards())
    '''
# character_test()
