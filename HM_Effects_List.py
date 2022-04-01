""" File: HM_Effects_List.py
    Author: Jackson Covey
    Purpose: This program is meant to act as a List of the
    card effects released in the 1st edition of in a H&M The Hiring TCG.

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

CHARACTER CARDS EFFECT NAMES AND DESCRIPTIONS STORED IN DICTIONARIES:

'''
# The Hiring Edition 1 PTSA and FTSA Card Effects.
PTSA_FTSA_CHARACTER_EFFECTS = dict([
    ("enrique", "While Character is on the Floor:" +
     " \nCharacter is immune to to all Spells."),

    ("draw", "When played: \nDraw a card."),

    ("backstock", "When played: \nAdd 1 additional BOH Card to the BOH Zone" +
     " from your hand. It comes into play, tapped."),

    ("blocker", "During an opponent’s attack, activate this effect:\n" +
     "Change their attack to this card using their originally declared stat."),

    ("starbs", "While Character is on the Floor: \nIf “Starbucks!” is cast," +
     " you can select the effect without flipping a coin."),

    ("backup to cashpoint", "When played: \nTarget 1 Character you control." +
     "\nIt is immune to Spells from both players."),

    ("check the totes", "When played: \nLook at the top 3 cards of your deck" +
     ". \nSelect 1 card to add to your hand. Select 1 card to put on the top"
     " \nof your deck. Put the remaining card on the bottom of your deck."),

    ("hate crime", "When played: \ntarget and tap one enemy Character." + 
    " \nThe targeted card does not untap until your opponent’s next turn."),

    ("put on hold", "When played: \nSearch your deck for 1 Fashion Item.\n" +
     "Reveal it to your opponent, and add it to your hand.\nIt cannot be " +
     "played this turn. Shuffle your deck."),

    ("gott'em", "When declared the target of an attack:\n" +
     "Opposing Character’s Base Stats are reduced by 10."),

    ("tech pants", 'When played: \nSearch your deck for 1 “Techwear Pants” ' +
     'Fashion Item, and add it to your hand. \nShuffle your deck. '+ 
     'It costs 1 less.'),

    ("moral i", "While Character is on the Floor: \nOther ally Characters’ " +
     "Base Stats are increased by 5."),

    ("destress i", "While Character is on the Floor: \nOther ally " +
     "Characters’ Stress Levels are decreased by 10. \nIncreases " +
     "this Character’s Stress Level by 5 for each other Character affected."),

    ("stress i", "While Character is on the Floor: \nOpponent’s " +
     "Stress Levels are increased by 10. \nDecrease this Character’s" +
     " Stress Level by 5 for each other Character affected.")])

# The Hiring Edition 1 Visual Card Effects.
VISUAL_CHARACTER_EFFECTS = dict([
    ("sample pick i", "When played: \nDraw 1 card. \nIf it is a Fashion" +
     " Item, draw another card."),

    ("finger-spacing", "While Character is on the Floor: \nAlly Characters’" +
     " Garment Care Stats are increased by 10, and Stress Levels are" +
     " increased by 5."),

    ("refill", "When played: \nSelect 1 card from your BOH Zone, add it to" +
     "your hand"),

    ("re-hang", "When played: \nSearch your deck for 1 card. \nReveal it" +
     " to your opponent. \nAdd it to your hand. Shuffle deck."),

    ("sample pick ii", "When played: \nDraw 1 card. \nIf it is a Spell, " +
     "draw another 2 cards."),

    ("refresh", "When played: \nShuffle your hand into your deck." +
     "\nDraw the same amount of cards you had +1.")])

# The Hiring Edition 1 Manager Card Effects.
MANAGER_CHARACTER_EFFECTS = dict([
    ("hod", "While Character is on the Floor: \nWhen an opponent declares " +
     "any attack, tap this card. \nThe declared attack stat can be" +
     " re-declared by the controller of this card."),

    ("moral ii", "While Character is on the Floor: \nAlly PTSA and FTSA" +
     " Character’s 3 Base Stats are increased by 10."),

    ("truck lead", "While Character is on the Floor: \nAlly PTSA and FTSA" +
     " Truck Stats and Garment Care Stats are increased by 15."),

    ("fanny pack", "When played: \nSearch your deck for 1 “Fanny Pack” " +
     'Fashion Item, and add it to your hand. \nShuffle your deck.' +
     "\nIt costs 0."),

    ("destress ii", "While Character is on the Floor: \nAlly PTSA, FTSA," +
     " and Visual Stress Levels are decreased by 10. \nDecrease this " +
     "Character’s Stress Level by 5 for each other Character affected."),

    ("double t&a", "When attacking directly: \nThis Character can remove 2 T" +
     "&A cards instead of 1. \nIf an opponent only has 1 T&A card left in " +
     "their T&A Zone, this card only removes 1."),

    ("scheduling", "When played: \nSelect 1 other Character on the Floor." +
     " \nSelect a Character in your hand of less or equal BOH cost. \nRemove" +
     " the Character on the Floor and place it in the Discard Pile. \nPlay" +
     " the one from your hand without tapping cards in your BOH Zone."),

    ("stress ii", "While Character is on the Floor: \nOpponent’s Stress" +
     " Levels are increased by 20. \nDecrease this Character’s Stress Level" +
     " by 5 for each other Character affected.")])

OVERHEAD_CHARACTER_EFFECTS = \
    {**VISUAL_CHARACTER_EFFECTS, **MANAGER_CHARACTER_EFFECTS, }

CHARACTER_EFFECTS = \
    {**PTSA_FTSA_CHARACTER_EFFECTS, **OVERHEAD_CHARACTER_EFFECTS}
CHARACTER_EFFECT_NAMES = CHARACTER_EFFECTS.keys()

'''
SPELL CARDS EFFECT NAMES AND DESCRIPTIONS STORED IN DICIONARIES:
'''

SPELL_BUFF_EFFECTS = dict([
    ("the values!", "Target any 1 Character. \nIncrease all" +
     " target’s Base Stats by 5 this turn. \nIf the Character" +
     " is a Visual or Manager: \nIncrease the target’s Base" +
     " Stats by 10 instead, and decrease the target’s Stress Level by 10."),

    ("5bd!", "Target any 1 Character. \nIncrease all target’s Base Stats" +
     " by 5 this turn. \nIf Character is a FTSA, increase by 15 instead."),

    ("starbucks!", "Target any 1 Character. Flip a Coin." +
     " \nIf heads: Increase target’s Truck Stat by 15, decrease target’s" +
     " Stress Level by 10 this turn.\n" +
     " \nIf tails: Decrease target’s Truck Stat by 15, increase target’s" +
     " Stress Level by 10 this turn."),

    ("call hod!", "Ally PTSA or FTSA must be on the Floor to activate." +
     " Target 1 ally PTSA or FTSA on the Floor. Tap it. " +
     " \nYou can play 1 Manager or Visual from your hand for x less BOH" +
     " points, where x is the BOH cost of the target tapped card."),

    ("fill the fridge!", "Manager must be on the Floor to activate." +
     " \nAll ally Character’s Stress Levels decrease by 15 this turn." +
     " \nDraw 2 cards, discard 2 cards."),

    ("use our app!", "Target up to 2 ally Characters. Increase targets’" +
     " Loyalty Stats by 10 this turn.")])

SPELL_DEBUFF_EFFECTS = dict([
    ("dress coded!", "Ally Manager or Visual must be on the Floor to" +
     " activate.\nWhen played, target any 1 Character." +
     " \nIf any Fashion Items are equipped, remove them and send them" +
     " to your opponent’s Discard Pile."),

    ("hr call!", "Target any 1 Character. \nTap target Character." +
     " \nTarget Character cannot be untapped until your opponent’s next" +
     " turn.\nTarget Character’s Stress Level is increased by 30."),

    ("bad wifi!", "Target any 1 Character. \nIts Loyalty Stat is" +
     " reduced by 20. \nTarget Character’s Stress Level is" +
     " increased by 20."),

    ("b.o.r.e. stickering!", "Target any 1 Character. \nTarget" +
     " Character’s Loyalty Stat and Garment Care Stat are reduced by" +
     " 15 this turn. \nTarget Character’s Stress Level is increased" +
     " by 20."),

    ("callout!", "Target any 1 Character. \nRemove it from the" +
     " Floor. \nFor the remainder of the turn, all opponent’s" +
     " Characters’ Stress Levels are increased by 30. \nDuring the" +
     " Closing Phase, return the target card to the Floor tapped."),

    ("you're fired!", "Ally Manager must be on the Floor to activate." +
     " \nTarget any 1 Character. \nIt is removed from the Floor and" +
     " placed in its owner's Discard Pile."),

    ("commercial move!", "All opponents’ PTSA and FTSA Characters’" +
     " Stress Levels are increased by 20 this turn. \n All ally Visual" +
     " and Manager Characters’ Stress Levels are decreased by 10" +
     " this turn."),

    ("district walk!", "Opponent’s Characters’ Stress Levels are" +
     " increased by 40 this turn. \nDraw a card. ")])

SPELL_NEGATION_EFFECTS = dict([
    ("15-minute break!", "Target any 1 Character. \nIts Base Stats" +
     " and Stress Level are returned to normal and cannot be changed" +
     " this turn. \nDraw a card."),

    ("i quit!", "Target 1 ally Character on the Floor or in your" +
     " hand. \nPlace target Character in your Discard Pile."),

    ("lunch!", "Target any 1 Character. \nTarget Character is removed" +
     " from the Floor until the Closing Phase of this turn." +
     " \nDuring the Closing Phase, return it to the Floor.")])

SPELL_DISCARD_EFFECTS = dict([
    ("re-hire!", "During your turn, target 1 Character in" +
     " your Discard Pile. \nPlace Target Character onto the" +
     " Floor without paying its BOH cost. \nYou cannot" +
     " conduct your Floor Phase this turn.")])

SPELL_STAT_CHANGE_EFFECTS = \
    {**SPELL_BUFF_EFFECTS, **SPELL_DEBUFF_EFFECTS}
SPELL_EFFECTS = \
    {**SPELL_STAT_CHANGE_EFFECTS, **SPELL_NEGATION_EFFECTS,
     **SPELL_DISCARD_EFFECTS}
SPELL_EFFECT_NAMES = SPELL_EFFECTS.keys()

'''

FASHION ITEM EFFECT NAMES AND DESCRIPTIONS STORED IN DICIONARIES:

'''
FASHION_ITEM_TARGET_ALLY_EFFECTS = dict([
    ("fanny pack", "Equipped Character's Garment Care Stat is" +
     " increased by 10.\nIf the Character is a Manager:" +
     " \nIncrease all Base Stats by 15, but negate the Character's" +
     " other abilities."),

    ("pilgrim collar", "Equipped Character's Garment Care Stat and" +
     " Loyalty Stat are increased by 10."),

    ("sunday club shirt", "While equipped, this Character gains the" +
     " ability:\nMoral I"),

    ("pleated skirt", "Equipped Character's Loyalty Stat is" +
     " increased by 10, and its Stress Level is decreased by 10"),

    ("techwear pants", "While equipped, this Character gains the" +
     " ability:\nGott'em" + "\nEquipped Character's Base Stats" +
     " are increased by 10."),

    ("fedora", "When equipped, look at the top card of your deck." +
     " \nThen, place it on the top or bottom of your deck." +
     " \nEquipped Character's Base Stats and Stress Level" +
     " are increased by 10."),

    ("the breakdown", "While equipped, this Character's type is set" +
     " to Manager, and it gains the ability:\n HOD" +
     " \nEquipped Character's Base Stats " +
     " are increased by 5, and Stress Level is increased by 10."),

    ("cobra's", "Equipped Character's Base Stats are" +
     " increased by 10, and its Stress Level is decreased by 20"),

    ("pimp jacket", "While equipped, this Character gains the" +
     " ability:\nDouble T&A")
    ])

FASHION_ITEM_TARGET_ALL_EFFECTS = dict([
    ("blazer", "Targets any Character" + "\nEquipped Character's" +
     " Base Stats are decreased by 10, and its Stress Level" +
     " is increased by 20"),

    ("2 weeks notice", "Targets any Character" + "\nWhen equipped, this" +
     " Character is tapped. \nIt remains tapped for a total of 2 turns." +
     " \nAfter 2 turns, it is removed from the FLoor, and put into the" +
     " Discard Pile."),
     ])

FASHION_ITEM_EFFECTS = {**FASHION_ITEM_TARGET_ALLY_EFFECTS, **FASHION_ITEM_TARGET_ALL_EFFECTS}


ALL_EFFECTS = \
    {**SPELL_EFFECTS, **CHARACTER_EFFECTS, **FASHION_ITEM_EFFECTS}
