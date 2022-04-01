from HM_Effects_List import ALL_EFFECTS
""" File: HM_Card.py
    Author: Jackson Covey
    Purpose: This program is meant to emulate a basic Card
    Object in H&M The Hiring TCG. Each Card inherits the basic
    methods that are necessary to emulate card mechanics.
"""


class Card:
    """ This class represents a generic Playing Card in a Trading
        Card Game. It can be played, contains basic information,
        and will most likely need to have added methods like discard,
        a playable boolean value,

        The constructor builds the object with 7 private fields.
            _name, the name of the card, String
            _type, the type of card, String
            _effects, the card's effects, List of Strings
            _flavor_text, the card's fun quote, String
            _cost, the card's BOH cost, int
            effect_activated, a boolean value that checks if effect was activated
            _tapped, whether the card is tapped or not, Boolean
            _owner, who the card belongs to, String

        The class defines several helpful methods and fields:
            play(): - prints a fun message, will most likely do other stuff.
            get_name(): - getter method for the card's name
            get_type(): - getter method for the card's type
            get_effects(): - getter method for the card's effects List
            get_effect_descriptions(): - getter method for the card effects'
                descriptions from HM_Effects_List
            get_flavor_text(): - getter method for the card's quote
            get_cost(): - getter method for the card's cost
            set_cost(int): - setter method for the card's cost
            tap(): - changes _tapped to True if possible
            untap(): - changes _tapped to False if possible
            set_owner(String): - sets the owner of the card
            get_owner(): - gets the owner of the card
            is_tapped(): - returns whether the card is tapped or not
            __str__(self): - prints the card

        USAGE:
        Create a Card object by declaring as such:
        x = Card(String, String, String List, String, int)

        Use Card methods by typing:
        x.play()
        play = x.get_name()
        etc...
    """

    def __init__(self, name, type, effects, flavor_text, cost):
        '''
        This constructor defines the Card Class's private variables.
        Classes that inherit from this class will have the same
        private variabes, as well as unique ones defined in their
        own Class.

        Arguments: name, String
                   type, String
                   effects, String List except sometimes
                   flavor_text, String
                   cost, int
        
        '''
        self._name = name
        self._type = type
        self._effects = effects
        self._flavor_text = flavor_text
        self._cost = cost
        self.effect_activated = False
        self._tapped = False
        self._owner = 'player 1'
        self.immune = False
        self.can_play = True
        self.can_play_turns = 0
        self.do_not_untap = False
        self.do_not_untap_turns = 0
        self.color = None

    def play(self):
        '''
        This function displays that a Card has been played.

        Arguments: n/a
        Return Values: String
        '''
        return "I play " + self._name

    def get_name(self):
        '''
        This function is a getter method for the Card's name.

        Arguments: n/a
        Return Values: String
        '''
        return self._name

    def get_type(self):
        return self._type

    def set_effects(self, effects):
        '''
        This function is a Setter method for the Card's effects list.

        Arguments: effects, List of Strings
        Return Values: List of Strings
        '''
        self._effects = effects

    def get_effects(self):
        '''
        This function is a getter method for the Card's effects list.

        Arguments: n/a
        Return Values: List of Strings
        '''
        return self._effects

    def get_effect_descriptions(self):
        '''
        This function is a getter method for the Card's effect's descriptions.
        It uses the HM_Effects_List Class, and for each effect in
        self._effects, it prints out the respective descriptions.

        Arguments: n/a
        Return Values: Prints Strings
        '''
        if type(self._effects) != type([]):
            return ALL_EFFECTS[self._effects]
        else:
            effect_descriptions = []
            for effect in self._effects: 
                effect_descriptions.append(ALL_EFFECTS[effect])
                print(effect_descriptions)
            return effect_descriptions


    def get_flavor_text(self):
        '''
        This function is a getter method for the Card's flavor text.

        Arguments: n/a
        Return Values: n/a
        '''
        return self._flavor_text

    def get_cost(self):
        '''
        This function is a getter method for the Card's cost.

        Arguments: n/a
        Return Values: int
        '''
        return self._cost

    def set_cost(self, new_cost):
        '''
        This function is a setter method for a Card's cost.
        It is used for when Cards have to cost more/less than
        they did originally.

        Arguments: new_cost, int
        Return Values: n/a
        '''
        if new_cost < 0:
            self._cost = 0
        self._cost = new_cost

    def tap(self):
        '''
        This function is a setter method for a Card's tapped status.
        Used for when Cards have to be used. When self._tapped is
        True, it means it has been used. When self._tapped is False,
        it means it has not been used, and it can be used.

        This function marks the Card as used.

        Arguments: n/a
        Return Values: n/a
        '''
        if self._tapped is True:
            print(self._name + " is already tapped.")
        else:
            self._tapped = True
            print(self._name + " was tapped.")

    def untap(self):
        '''
        This function is a setter method for a Card's tapped status.
        Used for when Cards have to be used. When self._tapped is
        True, it means it has been used. When self._tapped is False,
        it means it has not been used, and it can be used.

        This function marks the Card as unused. It can then be used.

        Arguments: n/a
        Return Values: n/a
        '''
        if self._tapped is False:
            print(self._name + " is already untapped.")
        else: 
            self._tapped = False
            print(self._name + " was untapped.")

    def set_owner(self, player):
        '''
        This function is a setter method for the owner of the Card.
        This us used so that a person cannot use certain Cards that do
        not belong to them.

        Arguments: player, a String
        Return Values: n/a
        '''
        self._owner = player

    def get_owner(self):
        '''
        This function is a getter method for the owner of the Card.
        This us used so that a person cannot use certain Cards that do
        not belong to them.

        Arguments: n/a
        Return Values: a String
        '''
        return self._owner
    
    def is_tapped(self):
        '''
        This function is a getter method for the Card's tapped status.

        Arguments: n/a
        Return Values: boolean
        '''
        return self._tapped

    def __str__(self):
        return "The " + self._name + " card."