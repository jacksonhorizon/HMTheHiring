from HM_Card_Types import CharacterCard, SpellCard, FashionItem
from HM_Effects_List import SPELL_EFFECTS, FASHION_ITEM_EFFECTS, \
    CHARACTER_EFFECTS
""" File: HM_Card_List.py
    Author: Jackson Covey
    Purpose: This program is meant to act as a Card List of the
    cards released in the 1st edition of in a H&M The Hiring TCG.
    It will contain a set of created Card Objects that are hard-coded

    It then changes their owners to player 2. This allows for 2 sets of Objects
    that can be used to make 2 unique decks.
"""


'''
How to make a CharacterCard:
Character_name = CharacterCard(owner, "name", "type", [L,T,GC,S], [effects],
                                flavor text, cost, equipped_card=None)
'''
# PTSA
estevan_2 = \
    CharacterCard('player 2', "Estevan", "PTSA", [35, 35, 35, 35], ["draw"],
                  '"i gotchu"', 1)

enrique_2 = \
    CharacterCard('player 2', "Enrique", "PTSA", [35, 25, 35, 20],
                  ["enrique", "backstock"], '"baby fight club"', 1, True)

kevin_2 = \
    CharacterCard('player 2', "Kevin", "PTSA", [35, 35, 40, 40], ["blocker"],
                  '''"i'll take an ice water"''', 1)

chadz_2 = \
    CharacterCard('player 2', "Chadz", "PTSA", [6, 9, 42, 0], ["enrique"],
                  '"this is my boyfriend \napplication"', 2, True)

rihanna_2 = \
    CharacterCard('player 2', "Rihanna", "PTSA", [45, 35, 40, 40], ["backup to cashpoint"],
                  '"something in arabic"', 2)

hailee_2 = \
    CharacterCard('player 2', "Hailee", "PTSA", [45, 40, 35, 40], ["check the totes"],
                  '''"i'm calling my lawyer"''', 2)

jonesy_2 = \
    CharacterCard('player 2', "Jonesy", "PTSA", [40, 40, 40, 30], ["starbs"],
                  '"oh sweetie"', 2)

tiana_2 = \
    CharacterCard('player 2', "Tiana", "PTSA", [40, 40, 40, 45], ["hate crime"],
                  '"for the vibes"', 3)

lindsay_2 = \
    CharacterCard('player 2', "Lindsay", "PTSA", [45, 45, 40, 60], ["put on hold"],
                  '"arson"', 3)

sean_2 = \
    CharacterCard('player 2', "Sean", "PTSA", [50, 35, 35, 45], ["gott'em"],
                  '''"you've activated up \nmy updog card"''', 3)

amor_2 = \
    CharacterCard('player 2', "Amor", "PTSA", [50, 50, 40, 50], ["tech pants"],
                  '"something"', 4)

arieanna_2 = \
    CharacterCard('player 2', "Arieanna", "PTSA", [50, 45, 40, 50], ["moral i"],
                  '''"they're all plastics, honey"''', 4)

jackson_2 = \
    CharacterCard('player 2', "Jackson", "PTSA", [40, 50, 40, 50], ["destress i"],
                  '''"we'll get to that when \nwe get to that"''', 4)

mason_2 = \
    CharacterCard('player 2', "Mason", "PTSA", [50, 60, 45, 00], ["stress i"],
                  '"caaaahhhhhpppppyyyyy"', 4)
megan_2 = \
    CharacterCard('player 2', "Megan", "FTSA", [55, 50, 55, 60], ["blocker", "draw"],
                  '''"i'm short"''', 4)

ily_2 = \
    CharacterCard('player 2', "Ily", "FTSA", [50, 55, 55, 60], ["blocker", "backstock"],
                  '''"i'm clocking out"''', 4)

haley_2 = \
    CharacterCard('player 2', "Haley", "FTSA", [45, 55, 70, 65],
                  ["blocker", "sample pick i"], '"something"', 5)

# Visuals

dani_2 = \
    CharacterCard('player 2', "Dani", "VISUAL", [55, 45, 85, 65],
                  ["finger-spacing", "refill", "re-hang"], '"i gotchaaaaa"', 5)

anthony_2 = \
    CharacterCard('player 2', "Anthony", "VISUAL", [60, 40, 90, 70],
                  ["finger-spacing", "sample pick ii", "refresh"],
                  '"hola señor"', 6)

# Managers
cody_2 = \
    CharacterCard('player 2', "Cody", "MANAGER", [70, 55, 75, 65], ["hod", "moral ii"],
                  '"flavor"', 6)

noah_2 = \
    CharacterCard('player 2', "Noah", "MANAGER", [55, 75, 75, 70], ["hod", "truck lead"],
                  '"ya hate to see it"', 7)

charlotte_2 = \
    CharacterCard('player 2', "Charlotte", "MANAGER", [75, 50, 85, 70],
                  ["hod", "destress ii"],  '"ya know what..."', 7)

daniel_2 = \
    CharacterCard('player 2', "Daniel", "MANAGER", [71, 71, 80, 75],
                  ["hod", "double t&a", "scheduling", "stress ii"],
                  '"i need a shirt for tonight"', 8)

'''
All of the Characters in a list
'''
CHARACTER_LIST = \
    [estevan_2, enrique_2, kevin_2, chadz_2, rihanna_2, hailee_2, jonesy_2,
     tiana_2, lindsay_2, sean_2, amor_2, arieanna_2, jackson_2, mason_2, megan_2,
     ily_2, haley_2, dani_2, anthony_2, cody_2, noah_2, charlotte_2, daniel_2]

'''
How to make a SpellCard:
SpellCardName = SpellCard(owner, name, type, effects, flavor_text, cost, factors,
                 special=None, special_factors=None, target_num=1):
'''

# starbucks coin flip multiplies the buffs by -1
starbucks_2 = \
    SpellCard('player 2', "Starbucks!", "SPELL", ["starbucks!"],
              '"anyone want an ice \nwater?"', 3, [0, 15, 0, -10], ['choose'])

# has to call get_special_factors to check if ptsa or ftsa is on the floor
# will probably have to be specially coded
call_hod_2 = \
    SpellCard('player 2', "Call HOD!", "SPELL", ["call hod!"],
              '"HOD pickup!"', 4, [0, 0, 0, 0], ["PTSA", "FTSA"])

fill_the_fridge_2 = \
    SpellCard('player 2', "Fill the Fridge!", "SPELL", ["fill the fridge!"],
              '"post this on convo!"', 4, [0, 0, 0, 0], ["MANAGER"],
              [0, 0, 0, -15], 5, 'all_allies')

# basic buff that has 2 targets
use_our_app_2 = \
    SpellCard('player 2', "Use our App!", "SPELL", ["use our app!"],
              '"we do have free wifi"', 4, [10, 0, 0, 0],
              [], [0, 0, 0, 0], 2, 'ally')

# has to interact with fashion items, probably specifically coded
dress_coded_2 = \
    SpellCard('player 2', "Dress Coded!", "SPELL", ["dress coded!"],
              '''"you're out of dress code"''', 1, [0, 0, 0, 0],
              ["MANAGER", "VISUAL"])

# has to tap a card, and interact with turns so its an ongoing affect
# will probably be specifically coded
hr_call_2 = \
    SpellCard('player 2', "HR Call!", "SPELL", ["hr call!"],
              '''"i'm calling ashley"''', 3, [0, 0, 0, 30])

# simple debuff
bad_wifi_2 = \
    SpellCard('player 2', "Bad Wifi!", "SPELL", ["bad wifi!"],
              '''"it's okay, the wifi isn't \nworking"''',
              3, [-20, 0, 0, 20])

bore_stickering_2 = \
    SpellCard('player 2', "B.O.R.E. Stickering!", "SPELL",
              ["b.o.r.e. stickering!"],
              '"today you are stickering \nb.o.r.e."', 4, [-15, 0, -15, 20])

# has to interact with board, do buff, then undo buff.
# has to be individually coded
callout_2 = \
    SpellCard('player 2', "Callout!", "SPELL", ["callout!"],
              '"someone called out"', 5, [0, 0, 0, 30])

# has to interact with the board.
youre_fired_2 = \
    SpellCard('player 2', "You're Fired!", "SPELL", ["you're fired!"],
              '"someone called out"', 5, [0, 0, 0, 0], ["MANAGER"])

# simple debuff with special condition debuffs
commercial_move_2 = \
    SpellCard('player 2', "Commercial Move!", "SPELL", ["commercial move!"],
              '"uh oh"', 6, [0, 0, 0, 20], ["MANAGER", "VISUAL"],
              [0, 0, 0, -10], 10, "AOE")

# simple debuff
district_walk_2 = \
    SpellCard('player 1', "District Walk!", "SPELL", ["district walk!"],
              '"big rip"', 7, [0, 0, 0, 40], [], [], 5, "all_opponents")

# has to somehow call the opoosing spells' undo_buffs() functions
# prob modify this factors by using get_factors from
fifteen_minute_break_2 = \
    SpellCard('player 2', "15-minute Break!", "SPELL", ["15-minute break!"],
              '"when is my 15"', 2, [0, 0, 0, 0], [], [0, 0, 0, 0])

# has to interact with floor
i_quit_2 = \
    SpellCard('player 1', "I Quit!", "SPELL", ["i quit!"],
              '"bye"', 1, [0, 0, 0, 0], [], [], 1, 'ally\\hand')

# has to interact with floor
lunch_2 = \
    SpellCard('player 2', "Lunch!", "SPELL", ["lunch!"],
              '"when is my lunch"', 2, [0, 0, 0, 0])

re_hire_2 = \
    SpellCard('player 2', "Re-Hire!", "SPELL", ["re-hire!"],
              '"welcome back"', 5, [0, 0, 0, 0])

'''
All of the Spells in a list
'''
SPELL_LIST = [starbucks_2, call_hod_2, fill_the_fridge_2, use_our_app_2,
              dress_coded_2, hr_call_2, bad_wifi_2, bore_stickering_2, callout_2,
              youre_fired_2, commercial_move_2, district_walk_2,
              fifteen_minute_break_2, i_quit_2, lunch_2, re_hire_2]

'''
How to make a FashionItem:
FashionItemName = FashionItem(owner, name, type, effects, text, cost, factors,
                              target=None, added_effects=None):
'''
# maybe make a special variable, and create a list of special effects/cards
# that can check and be like if special_var is not None: check what it is?
# most likely that will be the most effective strategy

# come back to fanny pack this and code the special conditions
fanny_pack_2 = \
    FashionItem('player 2', 'Fanny Pack', 'FASHIONITEM', ['fanny pack'],
                '"i want the h&m fanny \npack"', 2, [0, 0, 10, 0])

pilgrim_collar_2 = \
    FashionItem('player 2', 'Pilgrim Collar', 'FASHIONITEM', ['pilgrim collar'], '"ew"',
                1, [10, 0, 10, 0])

sunday_club_shirt_2 = \
    FashionItem('player 2', 'Sunday Club Shirt', 'FASHIONITEM', ['sunday club shirt'],
                '"we should all buy this"', 2, [0, 0, 0, 0], None, 'moral i')

pleated_skirt_2 = \
    FashionItem('player 2', 'Pleated Skirt', 'FASHIONITEM', ['pleated skirt'],
                '"kilt day"', 3, [10, 0, 0, -10])

techwear_pants_2 = \
    FashionItem('player 2', 'Techwear Pants', 'FASHIONITEM', ['techwear pants'],
                '''"they're only $120"''', 3, [5, 5, 5, 5], None, "gott'em")

# come back to fedora to do the card draw thing
fedora_2 = \
    FashionItem('player 2', 'Fedora', 'FASHIONITEM', ['fedora'],
                '"daniel on a night out"', 4, [10, 10, 10, 10])

# come back to this one to do special abilities
the_breakdown_2 = \
    FashionItem('player 2', 'The Breakdown', 'FASHIONITEM', ['the breakdown'],
                '"where did I put my breakdown?"', 4, [5, 5, 5, 10])

cobras_2 = \
    FashionItem('player 2', "Cobra's", 'FASHIONITEM', ["cobra's"],
                '"the daniel pants', 5, [10, 10, 10, -20])

pimp_jacket_2 = \
    FashionItem('player 2', 'Pimp Jacket', 'FASHIONITEM', ['pimp jacket'],
                '"i look like a pimp now"', 6,
                [0, 0, 0, 0], None, 'double t&a')

blazer_2 = \
    FashionItem('player 2', 'Blazer', 'FASHIONITEM', ['blazer'],
                '"fancy day"', 2, [-10, -10, -10, 20])

two_weeks_notice_2 = \
    FashionItem('player 2', '2 Weeks Notice', 'FASHIONITEM', ['2 weeks notice'],
                '''"i'm putting in my two weeks"''', 3, [0, 0, 0, 0])

FASHION_ITEM_LIST = [fanny_pack_2, pilgrim_collar_2, sunday_club_shirt_2,
                     pleated_skirt_2, techwear_pants_2, fedora_2, the_breakdown_2,
                     cobras_2, pimp_jacket_2, blazer_2, two_weeks_notice_2]


CARD_LIST_2 = CHARACTER_LIST + SPELL_LIST + FASHION_ITEM_LIST

CARD_SET_2 = set(CARD_LIST_2)

for card in CARD_SET_2:
    card.set_cost(0)