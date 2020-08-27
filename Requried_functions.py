import pygame
import math
from pygame.locals import QUIT, Rect

# initialising pygame and creating  window
pygame.init()
game_window = pygame.display.set_mode((640,720))
pygame.display.set_caption("Hello Nagendra")

square_boxes = []
    # To draw board----------------------------------
def drawboard():
    white =(251, 196, 117)
    black = (139, 69, 0)
    colors = [white,black]
    index = 0
    increment = 80
    for row in range(8):
        for column in range(8):
            square_box = Rect(column*increment,row*increment,80,80)
            if square_box not in square_boxes:
                square_boxes.append(square_box)
            pygame.draw.rect(game_window,colors[index],square_box)
            index = (index-1)*-1
        index = (index - 1) * -1

    # End-----------------------------------------------


def square(x):
    return x * x

def distance_formula(pos1, pos2):
    # pos1 and pos2 are tuples of 2 numbers
     return math.sqrt(square(pos2[0] - pos1[0]) + square(pos2[1] - pos1[1]))

