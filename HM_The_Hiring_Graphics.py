from HM_Board import Board
from HM_Decks import DECK_1, DECK_2
from HM_Board import Stack
from HM_Card_List import CHARACTER_TYPES
from graphics_game import graphics
from PIL import ImageTk, Image

'''
THE GRAPHICS SECTION OF THE STUPID GAME

uses graphics from graphics_game.py



'''
    
def print_board_graphics(graphic, current_player, other_player, phase=None):
    '''
    I HATE GRAPHICS MATH
    will use game graphics to show board and cards with commands
    each graphics related action will most likely have its own function
    '''
    graphic.clear()
    for i in range(5):
        # prints grey zones
        print_card_graphics(graphic, 'nothing', 200 + 125 * i, 255)
        print_card_graphics(graphic, 'nothing', 200 + 125 * i, 405)

    print_opponents_side(graphic, other_player)
    next_button = graphic.rectangle(845, 500, 100, 50, 'orange')
    graphic.text(850, 500, 'next phase:')
    # implement the next phase button
    spell_zone = graphic.rectangle(55, 330, 100, 140, 'light grey')
    graphic.canvas.tag_bind(next_button, "<Button-1>", lambda x: move_phase())
    print_player_side(graphic, current_player)
    
def print_opponents_side(graphic, other_player):
    '''
    prints top side of the board
    '''
    # prints player
    graphic.text(60, 15, other_player.name, 'black', 25)
    graphic.text(850, 15, 'hand: ' + str(len(other_player.hand)), 'black', 25)
    # prints boh points
    for i in range(len(other_player.boh_zone)):
        if other_player.boh_zone[i].is_tapped():
            graphic.rectangle(210 + 62 * i, 10, 20, 20, 'red')
        else:
            graphic.rectangle(210 + 62 * i, 10, 20, 20, 'purple')

    # prints boh zone barrier
    graphic.rectangle(0, 50, 1100, 10, 'purple')
    # prints opponent T\t&a
    i = 0
    for card in other_player.t_and_a_zone:
        if card is not None:
            print_card_graphics(graphic, 'hidden', 200 + 125 * i, 75)
        else:
            print_card_graphics(graphic, 'broken', 200 + 125 * i, 75)
        i += 1
    # prints discard pile
    graphic.rectangle(50, 70, 110, 150, 'red')
    graphic.text(50, 70, 'discard: \n' + str(len(other_player.discard_pile)), 'black', 20)
    # prints deck
    graphic.rectangle(840, 70, 110, 150, 'purple')
    if len(other_player.deck.get_list()) != 0:
        print_card_graphics(graphic, 'hidden', 845, 75)
    graphic.text(850, 75, 'deck: \n' + str(other_player.deck.size()), 'black', 20)
    # prints floor zone barrier
    graphic.rectangle(0, 230, 1100, 10, 'red')
    # prints cards in opponents floor zone
    i = 0
    for card in other_player.floor_zone:
        if card is not None:
            print_card_graphics(graphic, card, 200 + 125 * i, 255)
        i += 1

def print_player_side(graphic, current_player):
    '''
    prints bottom side of the board


    each LIST_OF
    is going to be a list of Rectangle objects that will be bound to left clicks so that they
    can hopefully show the cards in the top left corner but we'll see
    '''
    # prints cards in controllers floor zone
    LIST_OF_FLOOR = []
    i = 0
    for card in current_player.floor_zone:
        if card is not None:
            floor = print_card_graphics(graphic, card, 200 + 125 * i, 405)
        else: 
            floor = None
        LIST_OF_FLOOR.append(floor)
        i += 1
    # prints floor zone barrier
    graphic.rectangle(0, 560, 1100, 10, 'red')

    # prints controller t&a
    LIST_OF_T_A = []
    i = 0
    for card in current_player.t_and_a_zone:
        if card is not None:
            t_a = print_card_graphics(graphic, 'hidden', 200 + 125 * i, 585)
        else: 
            t_a = print_card_graphics(graphic, 'broken', 200 + 125 * i, 585)
        LIST_OF_T_A.append(t_a)
        i += 1
    # prints discard pile
    graphic.rectangle(840, 580, 110, 150, 'red')
    graphic.text(840, 580, 'discard: \n' + str(len(current_player.discard_pile)), 'black', 20)
    # prints deck
    graphic.rectangle(50, 580, 110, 150, 'purple')
    if len(current_player.deck.get_list()) != 0:
        print_card_graphics(graphic, 'hidden', 55, 585)
    graphic.text(60, 585, 'deck: \n' + str(current_player.deck.size()), 'black', 20)
    # prints boh zone barrier
    graphic.rectangle(0, 740, 1100, 10, 'purple')

    # prints boh points
    LIST_OF_BOH = []
    for i in range(len(current_player.boh_zone)):
        if current_player.boh_zone[i].is_tapped():
           boh = graphic.rectangle(210 + 62 * i, 770, 20, 20, 'red') 
        else:
           boh = graphic.rectangle(210 + 62 * i, 770, 20, 20, 'purple')
        LIST_OF_BOH.append(boh)

    # prints player
    graphic.text(60, 760, current_player.name, 'black', 25)
    graphic.text(850, 760, 'hand: ' + str(len(current_player.hand)), 'black', 25)

def print_card_graphics(graphic, card, x, y):
    '''
    prints a card using graphics
    '''
    # card back image
    # card background image
    # card character image
    if card == 'hidden':
        card_graphic = graphic.rectangle(x, y, 100, 140, 'black')
        graphic.print_images(x + 5, y + 5, 'HMCard')
        graphic.rectangle(x + 5, y + 5, 2, 130, 'red')
        graphic.rectangle(x + 5, y + 5, 90, 2, 'red')
        graphic.rectangle(x + 5, y + 133, 90, 2, 'red')
        graphic.rectangle (x + 93, y  + 5, 2, 130, 'red')
        #graphic.line(x + 5, y + 5, x + 5, y + 135,  'red', 3)
        #graphic.line()
    elif card == 'nothing':
        #graphic.print_images(0, 0, name)
        card_graphic = graphic.rectangle(x, y, 100, 140, 'grey')
    elif card == 'broken':
        #graphic.print_images(0, 0, name)
        card_graphic = graphic.rectangle(x, y, 100, 140, 'orange')
    else:
        if card.is_tapped():
            color = 'red'
        # prints cards if they are equipped to a character
        if card.get_type() in CHARACTER_TYPES:
            print_equipped_fashion_item_graphics(graphic, card, x, y)
            print_targeting_spell_card_graphics(graphic, card, x, y)
        
        # changes card display if not playable, or tapped
        if card.is_tapped():
            color = 'red'
        elif card.can_play == False:
            color = 'blue'
        else:
            color = 'black'
        # prints card and border, needs to also print picture using graphic.print_images
        card_graphic = graphic.rectangle(x, y, 100, 140, color)
        # print card image
        get_card_image(graphic, x, y, card.get_name())
        #graphic.print_images(x + 5 , y + 5, 'JingMad')
        graphic.rectangle(x + 5, y + 60, 90, 70, 'green')
        # prints name
        if len(card.get_name()) > 9:
            name = card.get_name().split(' ')
            count = 0
            for words in name:
                graphic.text(x + 5, y + 5 + 14 * count, words, 'white', 14)
                count += 1
        else:
            graphic.text(x + 5, y + 5, card.get_name(), 'white', 14)
        # print the cost inside the circle
        graphic.ellipse(x + 89, y + 10, 20, 20, 'black')
        graphic.ellipse(x + 89, y + 10 , 18, 18, card.color)
        graphic.text(x + 85, y, str(card.get_cost()))
        if card.get_type() in CHARACTER_TYPES:
            print_character_card_graphics(graphic, card, x, y)
        elif card.get_type() == 'SPELL':
            # put in center of zone on the left
            print_spell_card_graphics(graphic, card, x, y)
        elif card.get_type() == 'FASHIONITEM':
            print_fashion_item_graphics(graphic, card, x, y)
    return card_graphic

def print_equipped_fashion_item_graphics(graphic, card, x, y):
    '''
    prints equipped fashion item card slightly down and to the left of the
    card that is passed
    '''
    length_equip_cards = len(card.get_equipped_cards())
    if y < 400:
        y -= (7 * (length_equip_cards + 1))
    if y > 400:
        y += (7 * (length_equip_cards + 1))
    x -= (7 * (length_equip_cards + 1))
    for i in range(length_equip_cards, 0, -1):
        if y < 400:
            y += 7
        if y > 400:
            y -= 7
        x += 7
        equip_card = card.get_equipped_cards()[i - 1]
        print_card_graphics(graphic, equip_card, x, y)

def print_targeting_spell_card_graphics(graphic, card, x, y):
    '''
    prints equipped fashion item card slightly down and to the left of the
    card that is passed
    '''
    length_spell_cards = len(card.get_spell_cards())
    if y < 400:
        y -= (7 * (length_spell_cards + 1))
    if y > 400:
        y += (7 * (length_spell_cards + 1))
    x += (7 * (length_spell_cards + 1))
    for i in range(length_spell_cards, 0, -1):
        if y < 400:
            y += 7
        if y > 400:
            y -= 7
        x -= 7
        spell_card = card.get_spell_cards()[i - 1]
        print_card_graphics(graphic, spell_card, x, y)
                     
    
def print_character_card_graphics(graphic, card, x, y):
    '''
    prints the character cards stats in graphic
    '''
    # prints card type
    graphic.rectangle(x + 5, y + 60, 90, 10, 'purple')
    # prints stress level meter
    stress = card.get_stress_level()
    if stress > 90:
        stress = 90
    graphic.rectangle(x + 5, y + 125, 90, 10, 'white')
    if stress > 5:
        graphic.rectangle(x + 5, y + 125, stress - 5, 10, 'light green')
    if stress > 75:
        graphic.rectangle(x + 5, y + 125, stress - 5, 10, 'yellow')
    elif stress == 90:
        graphic.rectangle(x + 5, y + 125, 90, 10, 'red')
    graphic.rectangle(x + 75, y + 125, 3, 10, 'black')


    # if-else handles stat change displays
    if card.get_OG_stats()[0] != card.get_loyalty_stat():
       graphic.text(x + 10, y + 58, str(card.get_loyalty_stat()), 'light blue', 12) 
    else:
        graphic.text(x + 10, y + 58, str(card.get_loyalty_stat()), 'black', 12)
    if card.get_OG_stats()[1] != card.get_truck_stat():
        graphic.text(x+ 42, y + 58, str(card.get_truck_stat()), 'light blue', 12)
    else:
        graphic.text(x + 42, y + 58, str(card.get_truck_stat()), 'black', 12)
    if card.get_OG_stats()[2] != card.get_garment_care_stat():
        graphic.text(x + 75, y + 58, str(card.get_garment_care_stat()), 'light blue', 12)
    else:
        graphic.text(x + 75, y + 58, str(card.get_garment_care_stat()), 'black', 12)
    # stress level
    if card.get_OG_stats()[3] != card.get_stress_level():
        graphic.text(x + 7, y + 125, 'stress: '+ str(card.get_stress_level()), 'blue', 10)
    else:
        graphic.text(x + 7, y + 125, 'stress: '+ str(card.get_stress_level()), 'black', 10)

    # prints effects
    if card.effect_activated == True:
        color = 'orange'
        if card.immune:
            graphic.rectangle(x + 5, y + 69, 90, 1, 'gold')
    else: 
        color = 'black'
    j = 0
    for i in range(len(card.get_effects())): 
        graphic.text(x + 6, y + 70 + (i * 9) + j, card.get_effects()[i], color, 7)
        if card.get_type() == 'VISUAL' and card.effect_activated == False:
            if i == 1:
                graphic.text(x + 5, y + 80 + (i * 9), 'or', 'black', 7)
                j = 9
    
    # prints flavor text
    graphic.text(x + 7, y + 105, card.get_flavor_text(), 'black', 7)

def print_spell_card_graphics(graphic, card, x, y):
    '''
    todo
    '''
    graphic.rectangle(x + 5, y + 60, 90, 10, 'orange')
    
    # prints factors
    normal, special = card.get_factors()
    graphic.text(x + 10, y + 58, str(normal[0]), 'black', 12)
    graphic.text(x + 42, y + 58, str(normal[1]), 'black', 12)
    graphic.text(x + 75, y + 58, str(normal[2]), 'black', 12)

    # prints effect
    if card.effect_activated == True:
        color = 'orange'
    else: 
        color = 'black'
    graphic.text(x + 6, y + 70, card.get_effects(), color, 7)

    # prints flavor text
    graphic.text(x + 7, y + 105, card.get_flavor_text(), 'black', 7)

    # stress factor
    if normal[3] < 0:
        color = 'light green'
    elif normal[3] == 0:
        color = 'white'
    else:
        color = 'red'
    graphic.rectangle(x + 5, y + 125, 90, 10, color)
    graphic.text(x + 7, y + 125, 'stress: '+ str(normal[3]), 'black', 10)

def print_fashion_item_graphics(graphic, card, x, y):
    graphic.rectangle(x + 5, y + 60, 90, 10, 'light blue')

   # prints factors
    normal = card.get_factors()
    graphic.text(x + 10, y + 58, str(normal[0]), 'black', 12)
    graphic.text(x + 42, y + 58, str(normal[1]), 'black', 12)
    graphic.text(x + 75, y + 58, str(normal[2]), 'black', 12)

    # prints effect
    if card.effect_activated == True:
        color = 'orange'
    else: 
        color = 'black'
    graphic.text(x + 6, y + 70, card.get_effects(), color, 9)

    # prints flavor text
    graphic.text(x + 7, y + 105, card.get_flavor_text(), 'black', 7)

    # stress factor
    if normal[3] < 0:
        color = 'light green'
    elif normal[3] == 0:
        color = 'white'
    else:
        color = 'red'
    graphic.rectangle(x + 5, y + 125, 90, 10, color)
    graphic.text(x + 7, y + 125, 'stress: '+ str(normal[3]), 'black', 10)

def play_spell_card_graphics(graphic, card):
    '''
    puts spell cards in spell zone, and shows opponent
    '''
    print_card_graphics(graphic, card, 55, 330)
    show_to_opponent(graphic, card)
   
def play_fashion_item_graphics(graphic, card):
    '''
    puts fashion cards in spell zone, and shows opponent
    '''
    print_card_graphics(graphic, card, 55, 330)
    show_to_opponent(graphic, card)

def print_hand_graphics(current_player, graphic):
    '''
    prints the current player's hand using graphics
    '''
    i = 0
    j = 0
    for card in current_player.hand:
        if i >= 9:
            print_card_graphics(graphic, card, 9 + 109 * j, 555)
            j += 1
        else:
            print_card_graphics(graphic, card, 9 + 109 * i, 410)
        i += 1

def print_tiny_card_graphics(graphic, card, x, y):
    r = graphic.rectangle(x, y, 100, 55, 'black')
    r2 = graphic.rectangle(x + 5, y + 5, 90, 45, 'green')

    # print the cost inside the circle
    graphic.ellipse(x + 89, y + 10, 20, 20, 'black')
    graphic.ellipse(x + 89, y + 10 , 18, 18, card.color)
    graphic.text(x + 85, y, str(card.get_cost()))
    # prints name
    if len(card.get_name()) > 9:
        name = card.get_name().split(' ')
        count = 0
        for words in name:
            graphic.text(x + 5, y + 5 + 14 * count, words, 'black', 14)
            count += 1
    else:
        graphic.text(x + 5, y + 5, card.get_name(), 'black', 14)

def print_tiny_card_list_corner_vertical(graphic, card_list, num_cards):
    move_down = 0
    move_right = 0
    for card in card_list:
        if move_down == 12:
            move_down = 0
            move_right += 1
        print_tiny_card_graphics(graphic, card, 10 + 110 * move_right, 10 + 65 * move_down)
        move_down += 1

def print_card_list_corner(graphic, card_list, num_cards):
    '''
    prints num_cards in top corner
    '''
    i = 0
    for card in card_list:
        print_card_graphics(graphic, card, 10 + 110 * i, 10)
        i += 1

def print_card_list_corner_without_card(graphic, target, card_list, num_cards, num_times):
    '''
    prints num_cards in top corner
    '''
    i = 0
    for card in card_list:
        if card.get_name() != target.get_name():
            print_card_graphics(graphic, card, 10 + 110 * i, 10 + 150 * num_times)
        i += 1


def print_draw_graphics(graphic, card):
    print_card_graphics(graphic, card, 55, 330)

def show_to_opponent(graphic, card):
    print_card_graphics(graphic, card, 850, 10)

def print_actions(graphic, action_text, text, extra_text=None):
    if text is not None:
        effect_info = graphic.rectangle(845, 250, 100, 50, 'light blue')
        graphic.text(850, 255, action_text, 'black', 10)
        graphic.text(850, 265 + 10, text, 'black', 10)
    if extra_text is not None:
        # centers text
        graphic.text(895 - ((len(extra_text) // 2) * 4), 300 , extra_text, 'black', 10)

def print_general_actions(graphic, text, need_box=False):
    i = 0
    if need_box:
        effect_info = graphic.rectangle(845, 350, 100, 50, 'green')
    if text == 'press enter to continue':
        i = 20
    else:
        effect_info = graphic.rectangle(845, 350, 100, 50, 'green')
    graphic.text(895 - (len(text) // 2) * 4, 350 + i , text, 'black', 10)

def get_card_image(graphic, x, y, name):
    name = name.strip()
    graphic.print_images(x + 5 , y + 5, name)

def move_phase():
    '''
    will be implemented and written once the game is complete and i need to switch to a 
    graphics based UI
    '''
    print()