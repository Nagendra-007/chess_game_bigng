import pygame
import math
from math import pi
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

def movable_squares(target_pawn_pos,list_of_locations,angle_list):
    movable_locations = []
    for location in list_of_locations:
        for angle in angle_list:
            dx = target_pawn_pos.centerx - location.centerx
            dy = target_pawn_pos.centery - location.centery
            test_angle = math.atan2(-dy, dx)
            if test_angle == angle:
                movable_locations.append(location)
    return movable_locations