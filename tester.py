from HM_Board import Board
from HM_Decks import DECK_1, DECK_2
from HM_Board import Stack
from HM_Card_List import CHARACTER_TYPES
from HM_Card_List import district_walk
import random
from PIL import Image, ImageTk




from graphics_game import graphics
def main():
    #graphic = graphics(1000, 800, 'HM The Hiring')
    #simple_left_click(graphic, print_rectangle)
    #graphic.set_left_click_action(show_card_graphics)
    #graphic.set_right_click_action(unshow_card_graphics)
    #print_board_graphics(graphic, 1, 2)
    #board = print_board(graphic)
    #print_card(graphic, sean, board)
    rand = random.randint(1, 2)
    print(district_walk.can_target)
    input()


def print_board(graphic):
    r = graphic.rectangle(0, 0, 150, 200, 'white')
    return r

def print_card(graphic, card, background):
    r = graphic.rectangle(5, 5, 100, 140)
    graphic.canvas.tag_bind(r, "<Button-1>", lambda x: print_card_smaller(graphic, card))
    graphic.canvas.tag_bind(background, "<Button-1>", lambda x: print_board(graphic))

def print_card_smaller(graphic, card):
    r = graphic.rectangle(0, 0, 50, 70, 'red')




def print_board_graphics(graphic, current_player, other_player):
    '''
    I HATE GRAPHICS MATH
    will use game graphics to show board and cards with commands
    each graphics related action will most likely have its own function
    '''
    # prints boh points
    for i in range(10):
        graphic.rectangle(210 + 62 * i, 10, 20, 20, 'purple')
    # prints boh zone barrier
    graphic.rectangle(0, 50, 1100, 10, 'purple')
    # prints opponent T\t&a
    for i in range(0, 5):
        print_card_graphics(graphic, 'hi', 200 + 125 * i, 75)
    # prints discard pile
    graphic.rectangle(50, 70, 110, 150, 'red')
    # prints deck
    graphic.rectangle(840, 70, 110, 150, 'blue')
    # prints battle zone barrier
    graphic.rectangle(0, 230, 1100, 10, 'red')

    # prints battle zone barrier
    graphic.rectangle(0, 560, 1100, 10, 'red')
    # prints controller t&a
    for i in range(0, 5):
        print_card_graphics(graphic, 'hi', 200 + 125 * i, 585)
    # prints discard pile
    graphic.rectangle(840, 580, 110, 150, 'red')
    # prints deck
    graphic.rectangle(50, 580, 110, 150, 'blue')
    # prints boh zone barrier
    graphic.rectangle(0, 740, 1100, 10, 'purple')
    # prints boh points
    for i in range(10):
        graphic.rectangle(210 + 62 * i, 770, 20, 20, 'purple')

def print_card_graphics(graphic, card, x, y):
    graphic.rectangle(x, y, 100, 140, 'black' )


def show_card_graphics(graphic, mouse_x, mouse_y, current_player, other_player):
    '''
    if mouse_x in bound for card object and mouse_y in bounds for card object:

    '''
    r = graphic.rectangle(0,0,200, 280)

def unshow_card_graphics(graphic, mouse_x, mouse_y):
    graphic.clear()

def simple_left_click(graphic, callee):
    ''' Call the callee function whenever the left click happens.
    callee should take two parameters, the mouse x and mouse y coordinates.
    '''
    def left_click_action(event):
        callee(graphic, event.x, event.y)
    ''' <Button-1> is the left-most mouse button '''
    graphic.canvas.bind('<Button-1>', left_click_action)

def print_rectangle(graphic, x, y):
    r = graphic.rectangle(x,y,200, 280)
    input()
    simple_left_click()
    graphic.delete_object(r)


def set_left_click_action(self, callee, current_player, other_player):
    ''' Call the callee function whenever the left click happens.
    callee should take two parameters, the mouse x and mouse y coordinates.
    '''
    def left_click_action(event):
        callee(self, event.x, event.y, current_player, other_player)
    ''' <Button-1> is the left-most mouse button '''
    self.canvas.bind('<Button-1>', left_click_action)
main()