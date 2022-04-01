

from tkinter import *
from PIL import ImageTk, Image
from graphics_game import graphics
import os

def import_images(graphic):
    path = "/Users/jacksoncovey/Desktop/HMTheHiring/HM_Images/"
    for filename in os.listdir(path):
        if not str(filename) == '.DS_Store':
            graphic.appendImages(path, str(filename))

def print_image_graphics(graphic, x, y, name):
    graphic.print_images(x, y, name)

def test():
    graphic = graphics(500, 200, 'test')
    import_images(graphic)
    print_image_graphics(graphic, 0, 0,'JingMad')
    input()