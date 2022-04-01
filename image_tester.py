
from tkinter import *
from PIL import ImageTk, Image
from HM_Card_List import sean, kevin, daniel
from graphics_game import graphics
from HM_Import_Images import import_images

def main():
    '''
    works with space in image name
    '''
    graphic = graphics(1000, 800, 'HM The Hiring')
    import_images(graphic)
    #graphic.appendImages('Audrey.png')
    list_ = [sean, kevin, daniel]
    print(kevin.get_name())
    count = 0
    for card in list_:
        graphic.print_images(10 + 110 * count, 10, card.get_name())
        count += 1

    #graphic.print_images(120, 10, 'Audrey.png')
    input()


main()