from HM_Card import Card
from HM_Effects_List import ALL_EFFECTS
""" File: HM_Card_Types.py
    Author: Jackson Covey
    Purpose: This program is meant to emulate the Card Types in
    H&M The Hiring TCG. These Card Types include CharacterCard,
    SpellCard, FashionItem, and SummonCard. Each card has
    unqie characteristics, methods, and implementations that
    can be used elsewhere.
"""

class CharacterCard(Card):
    """ This class represents a Character Card in a Trading
        Card Game. It can be played, contains basic information and
        stats, and can be modified.

        The constructor builds the object with 11 private fields.
            _owner, the owner of the card, String
            _name, the name of the card, String
            _type, the type of card, String
            _OG_stats, the original stats of a card, List of 4 ints
            _stats, stats of a card that can be changed.
            _effects, the card's effects, List of Strings
            _flavor_text, the card's fun quote, String
            _cost, the card's BOH cost, int
            _tapped, whether the card is tapped or not, Boolean
            _owner, who the card belongs to, String
            _equipped_cards, what FashionItem(s) are equipped, FashionItem List

        The class defines several helpful methods and fields:
            get_stats(): - returns the current stats ex. [35, 25, 40, 30]
            get_OG_stats(): - returns the original stats
            get_loyalty_stat(): - returns the loyalty stat
            get_truck_stat(): - returns the truck stat
            get_garment_care_stat(): - returns the garment care stat
            get_total_stats(): - returns the total of the 3 base stats
            get_stress_level(): - returns the stress level
            change_stress(int): - changes the stress level and applies/undoes
                debuffs
            change_base_stats(int): - changes the 3 base stats
            add_effects(String): - adds an effect(s) to the Card's effects list
            get_equipped_cards(): - returns the FashionItem(s) equipped
            add_equipped_cards(): - sets the FashionItem(s) equipped
            remove_equipped_cards(): - removes the FashionItem(s) equipped
            get_spell_cards(): - returns the Spell cards that target the Character
            add_spell_cards(): - adds a Spell card that targets the Character
            remove_spell_cards(): - Removes Spell(s) that target the Character

        USAGE:
        Create a Card object by declaring as such:
        x = \
        CharacterCard(name, type, stats, effects, flavor_text, cost)

        Use Card methods by typing:
        x.play()
        play = x.get_name()
        x.change_stress(50)

        etc...
    """
    def __init__(self, owner, name, card_type, stats, effects,
                 flavor_text, cost, immune=False):
        '''
        This constructor defines the CharacterCard Class's private
        variables.

        Arguments: owner, String
                   name, String
                   card_type, String
                   stats, List of 4 ints
                   effects, String List
                   flavor_text, String
                   cost, int
                   equipped_cards, FashionItem List
                   spell_cards, Spell List
        '''
        self._owner = owner
        self._name = name
        self._type = card_type
        self._OG_stats = stats[:]
        self._stats = stats
        self._effects = effects
        self._flavor_text = flavor_text
        self._cost = cost
        self._tapped = False
        self._equipped_cards = []
        self._spell_cards = []
        self._active_effects = []
        self._position = None
        self.effect_activated = False
        self.immune = immune
        self.can_play = True
        self.can_play_turns = 0
        self.do_not_untap = False
        self.do_not_untap_turns = 0
        self.color = None

    def get_stats(self):
        '''
        This function is a getter method for the Card's stats.

        Arguments: n/a
        Return Values: List of 4 ints
        '''
        return self._stats

    def get_OG_stats(self):
        '''
        This function is a getter method for the Card's original stats.

        Arguments: n/a
        Return Values: List of 4 ints
        '''
        return self._OG_stats

    def get_loyalty_stat(self):
        '''
        This function is a getter method for the CharacterCard's loyalty stat.

        Arguments: n/a
        Return Values: int
        '''
        return self._stats[0]

    def get_truck_stat(self):
        '''
        This function is a getter method for the CharacterCard's truck stat.

        Arguments: n/a
        Return Values: int
        '''
        return self._stats[1]

    def get_garment_care_stat(self):
        '''
        This function is a getter method for the CharacterCard's garment care
        stat.

        Arguments: n/a
        Return Values: int
        '''
        return self._stats[2]

    def get_stress_level(self):
        '''
        This function is a getter method for the CharacterCard's stress level

        Arguments: n/a
        Return Values: int
        '''
        return self._stats[3]

    def get_total_stats(self):
        '''
        This function is a getter method for the Card's 3 base stat total.

        Arguments: n/a
        Return Values: int
        '''
        return self._stats[0] + self._stats[1] + self._stats[2]
    def return_to_OG_stats(self):
        '''
        This function is a setter method that changes the 3 base stats back to
        their original state.

        Arguments: n/a
        Return Values: n/a
        '''
        self._stats = self._OG_stats
        
    def change_stress(self, factor):
        '''
        This function changes the Character's Stress Level.
        It then applies debuffs accordingly past a Stress Level of 75. If it is already 75,
        it then undoes the debuff effect.

        Arguments: factor, int
        Return Values: n/a
        '''
        # checks if factor is positive
        if factor > 0:
            self._stats[3] += factor  # changes stat first
            if self._stats[3] > 75:
                # calcs # of debuff
                debuff_multiplier = int((self._stats[3] - 75) / 5)
                for i in range(0, debuff_multiplier):  # does debuff
                    self.change_base_stats([-5, -5, -5])
        elif factor < 0:
            if self._stats[3] > 75:
                # calcs # of debuffs to undo
                debuff_multiplier = int((self._stats[3] - 75) / 5)
                for i in range(debuff_multiplier):  # undoes debuff
                    self.change_base_stats([5, 5, 5])
            self._stats[3] += factor  # changes to new stat

    def change_base_stats(self, factors):
        '''
        This function changes the Character's 3 base stats.
        Of Note: When using, change stres must also be used separately.

        Arguments: factors, int List
        Return Values: n/a
        '''
        for i in range(0,3):
            self._stats[i] += factors[i]

    def add_effects(self, effects):
        '''
        This function adds an effect to the cards effects list.

        Arguments: effects, String or String List
        Return Values: n/a
        '''

        if type(effects) != type([]):
            effects = [effects]
        self._effects += effects

    def remove_effects(self, effects):
        '''
        This function removes an effect(s) from the cards effects list.

        Arguments: effects, String or String List
        Return Values: n/a
        '''
        if type(effects) != type([]):
            effects = [effects]
        for effect in effects:
            if effect in self._effects:
                self._effects.remove(effect)

    def get_equipped_cards(self):
        '''
        This function is a getter method for the Card's equipped cards

        Arguments: n/a
        Return Values: List of FashionItem
        '''
        return self._equipped_cards

    def add_equipped_cards(self, equip_cards):
        '''
        This function is a setter method for the Card's equipped cards

        Arguments: equip_cards, a List of FashionItems
        Return Values: n/a
        '''
        if type(equip_cards) != type([]):
            equip_cards = [equip_cards]
        self._equipped_cards += equip_cards

    def remove_equipped_cards(self, target=None):
        '''
        This function is a getter method for the Card's equiped cards.
        It uses a default argument to enable a remove all function.

        Arguments: target, FashionItem, default None
        Return Values: n/a
        '''
        if target is None:
            self._equipped_cards = []
            return
        self._equipped_cards.remove(target)

    def get_spell_cards(self):
        '''
        This function is a getter method for the Spell Cards 
        that are affect the Character

        Arguments: n/a
        Return Values: List of Spells
        '''
        return self._spell_cards

    def add_spell_cards(self, spell_cards):
        '''
        This function is a setter method for the Spell Cards
        that affect the Character

        Arguments: spell_cards, a List of Spells
        Return Values: n/a
        '''
        if type(spell_cards) != type([]):
            spell_cards = [spell_cards]
        self._spell_cards += spell_cards

    def remove_spell_cards(self, target=None):
        '''
        This function is a getter method for the Spells
        that affect the Character.
        It uses a default argument to enable a remove all function.

        Arguments: target, Spell, default None
        Return Values: n/a
        '''
        if target is None:
            self._spell_cards = []
            return
        self._spell_cards.remove(target)
    
    def get_position(self):
        '''
        This function is a getter method for the cards position on a board once set

        Arguments: n/a
        Return Values: int
        '''
        return self._position

    def set_position(self, new_position):
        self._position = new_position

class SpellCard(Card):
    """ This class represents a Spell Card in a Trading
        Card Game. It can be played, contains basic information and
        stats, and can be used to modify Characters or do something on
        the Board(eventually)

        The constructor builds the object with 10 private fields.
            _owner, the owner of the card, String
            _name, the name of the card, String
            card_type, the type of card, String
            _effects, the card's effects, List of Strings
            _flavor_text, the card's fun quote, String
            _cost, the card's BOH cost, int
            _factors, 4 numbers to change Character stats, List of ints
            _special, the card's special conditions, List of strings
            _special_factors, 4 numbers to change Character stats, List of ints
            _target_num, number of Character Cards that can be affected, int

        The class defines several helpful methods and fields:
            get_factors() - returns the factors by which Character stats
                are modified.
            get_special(): - returns list of special conditions
            get_targets(): - returns list of CharacterCards targeted
            get_target_num(): - returns number of targets
            set_targets([CharacterCard]): - sets the targets
            set_target_num(int): - sets the number of targets
            set_factors(List, List): - sets normal and special factors
                by which Character stats are modified.
            apply_factors(CharacterCard): - applies stat changes to a
                CharacterCard
            unapply_factors(CharacterCard): - unapplies stat changes to a
                CharacterCard

        USAGE:
        Create a Card object by declaring as such:
        y = \
        SpellCard(name, type, effects, flavor_text, cost, factors,
                      special, special_factors, target_num)

        Use Card methods by typing:
        y.set_factors([0, 10, 10, 10], [0, 15, 15, 15]
        y.apply_factors(CharacterCard)


        etc...
    """
    def __init__(self, owner, name, card_type, effects, flavor_text, cost,
                 factors=[0, 0, 0, 0], special=[],
                 special_factors=[0, 0, 0, 0], target_num=1, can_target='all'):

        '''
        This constructor defines the SpellCard Class's private
        variables.

        Arguments: owner, String
                   name, String
                   type, String
                   effects, String List
                   flavor_text, String
                   cost, int
                   tapped, boolean
                   factors, int List
                   special, String List
                   special_factOrs, int List
                   target_num, int
        Return Values: n/a
        '''
        self._owner = owner
        self._name = name
        self._type = card_type
        self._effects = effects
        self._flavor_text = flavor_text
        self._cost = cost
        self._tapped = False
        self._targets = None
        self._factors = factors  # [0,10,0,0]
        self._special = special
        self._special_factors = special_factors  # [0,0,0,0]
        self._target_num = target_num
        self.can_play_this_turn = True
        self.effect_activated = False
        self.can_play = True
        self.can_play_turns = 0
        self.do_not_untap = False
        self.do_not_untap_turns = 0
        self.can_target = can_target
        self.color = None

    def get_factors(self):
        '''
        This function is a getter method for the SpellCard's factors

        Arguments: n/a
        Return Values: int List, int List
        '''
        return self._factors, self._special_factors

    def get_special(self):
        '''
        This function is a getter method for the Card's special conditions

        Arguments: n/a
        Return Values: _special, String
        '''
        return self._special

    def get_targets(self):
        '''
        This function is a getter method for the Card's targets

        Arguments: n/a
        Return Values: _targets, CharacterCard List
        '''
        return self._targets

    def get_target_num(self):
        '''
        This function is a getter method for the Card's # of targets

        Arguments: n/a
        Return Values: _targets_num, int
        '''
        return self._target_num

    def set_factors(self, new_factors, new_special_factors):
        '''
        This function is a setter method for the Card's factors

        Arguments: new_factors, int List
            new_special_factors, int List
        Return Values: n/a
        '''
        self._factors = new_factors
        self._new_special_factors = new_special_factors

    def set_targets(self, new_targets):
        '''
        This function is a setter method for the Card's targets

        Arguments: new_targets, CharacterCard List
        Return Values: n/a
        '''
        self._targets = new_targets

    def set_target_num(self, new_target_num):
        '''
        This function is a setter method for the Card's # of targets

        Arguments: new_target_num, int
        Return Values: n/a
        '''
        # For AOE, reset target num to amount of targets on the board,
        # then set_targets([ ]), then apply buffs.
        self._target_num = new_target_num

    def apply_factors(self):
        '''
        This function is a applies the cards factors to (a) CharacterCard(s)

        Arguments: n/a
        Return Values: n/a
        '''
        if self._target_num != len(self._targets):
            print("Number of targets invalid")
            return
        for target in self._targets:  # applies buff to special targets
            if target.get_type() in self._special:
                target.change_base_stats(self._special_factors)
                target.change_stress(self._special_factors[3])
            else:  # applies buff normally
                target.change_base_stats(self._factors)
                target.change_stress(self._factors[3])

    def unapply_factors(self):
        '''
        This function is a undoes the cards factors to (a) CharacterCard(s)

        Arguments: n/a
        Return Values: n/a
        '''
        if len(self._special_factors) != 4:
            return
             
        if self._target_num != len(self._targets):
            print("Number of targets invalid")
            return
        new_special_factors = [0, 0, 0, 0]
        new_factors = [0, 0, 0, 0]
        for i in range(4):
            new_special_factors[i] = -1 * self._special_factors[i]
            new_factors[i] = -1 * self._factors[i]
        for target in self._targets:  # undoes buff to special targets
            if target.get_type() in self._special:
                target.change_base_stats(new_special_factors)
                target.change_stress(new_special_factors[3])
            else:  # undoes buff normally
                target.change_base_stats(new_factors)
                target.change_stress(new_factors[3])
    

class FashionItem(Card):
    """ This class represents a FashionItem Card in a Trading
        Card Game. It can be played, contains basic information and
        stats, and can be used to modify Characters or do something on
        the Board(eventually). Specifically, it can be equipped to a singular
        card, modify its stats, and give effects.

        The constructor builds the object with 9 private fields.
            _owner, the owner of the card, String
            _name, the name of the card, String
            card_type, the type of card, String
            _effects, the card's effects, List of Strings
            _flavor_text, the card's fun quote, String
            _cost, the card's BOH cost, int
            _factors, 4 numbers to change Character stats, List of ints
            _target, a Character Card target, Character
            _added_effects, effects to be added to the targets self._effects,
                String

        The class defines several helpful methods and fields:
            get_target_type(): - gets target type, used to determine all vs ally 
                                targets
            set_target(CharacterCard): - sets the targets
            get_factors(): - get the factors
            apply_factors(): - applies stat changes to target
                CharacterCard
            unapply_factors() - unapplies stat changes to target
                CharacterCard
            get_added_effects(): - returns the effects the card can give
            give_effects(): - gives the target Card the added_effects
            remove_effects(): - removes the target Card's added_effects

        USAGE:
        Create a Card object by declaring as such:
        y = \
        SpellCard(name, type, effects, flavor_text, cost, factors,
                      special, special_factors, target_num)

        Use Card methods by typing:
        y.set_factors([0, 10, 10, 10], [0, 15, 15, 15]
        y.apply_factors(CharacterCard)


        etc...
    """
    def __init__(self, owner, name, card_type, effects, flavor_text, cost, factors,
                 target=None, added_effects=None, can_target='all'):
        '''
        This constructor defines the FashionItem Class's private
        variables.

        Arguments: owner, String
                   name, String
                   type, String
                   effects, String List
                   flavor_text, String
                   cost, int
                   tapped, boolean
                   factors, int List
                   target, CharacterCard,
                   added_effects, String List
        '''
        self._owner = owner
        self._name = name
        self._type = card_type
        self._effects = effects
        self._flavor_text = flavor_text
        self._cost = cost
        self._tapped = False
        self._factors = factors
        self._target = target
        self._added_effects = added_effects
        self.effect_activated = False
        self.can_play = True
        self.can_play_turns = 0
        self.do_not_untap = False
        self.do_not_untap_turns = 0
        self.color = None
        self.can_target = can_target

    def set_target(self, new_target):
        '''
        This function sets the target of the FashiomItem

        Arguments: targets, CharacterCard
        Return Values: n/a
        '''
        self._target = new_target

    def get_factors(self):
        '''
        This function is a getter method for the Fashion cards's factors

        Arguments: n/a
        Return Values: int List
        '''
        return self._factors

    def apply_factors(self):
        '''
        This functions gives buff, then reverse the buff before un-equipping the card.

        Arguments: n/a
        Return Values: n/a
        '''
        self._target.change_base_stats(self._factors)
        self._target.change_stress(self._factors[3])

    def unapply_factors(self):
        '''
        Undoes the buff. This function must be called before the
        removing the unequipping the card.

        Arguments: n/a
        Return Values: n/a
        '''
        negative_factors = []
        for i in range(len(self._factors)):
            negative_factors.append(self._factors[i]  * -1)
        self._target.change_base_stats(negative_factors)
        self._target.change_stress(negative_factors[3])

    def get_added_effects(self):
        return self._added_effects

    def give_effects(self):
        '''
        This function gives the target CharacterCard, an effect in its
        self._effects list

        Arguments: target, CharacterCard
        Return Values: n/a
        '''
        if len(self._target.get_effects()) == 0:
            return
        elif self._added_effects is None:
            return
        self._target.add_effects(self._added_effects)

    def remove_effects(self):
        '''
        This function revmoves an effect(s) from target CharacterCard's
        self._effects list.

        Arguments: target, CharacterCard
        Return Values: n/a
        '''
        if self._added_effects is None:
            return
        self._target.remove_effects(self._added_effects)

class SummonCard(Card):
    def __init__(self, name, type, effects, text, cost):
        self._name = name
        self._type = type
        self._effects = effects
        self._text = text
        self._cost = cost


