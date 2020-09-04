import pygame
import math
from math import pi
from pygame.locals import QUIT, Rect

# initialising pygame and creating  window
pygame.init()
game_window = pygame.display.set_mode((640,640))
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
            if test_angle == angle and location!=target_pawn_pos:
                movable_locations.append((location,angle))

                #movable_locations.remove((target_pawn_pos,0))
    return movable_locations


def isfarther(start, pos1, pos2):
    # Returns T/F whether pos2 is farther away than pos1

    if type(pos2) == int:  # for pawns
        return pos1 > distance_formula(start.center, pos2)
    else:
        return distance_formula(start.center, pos1) > distance_formula(start.center, pos2)

def nearest_piece(position, listof):
    nearest = None
    posCounter = 50000  # a very high number/ could use board dimension^2
    for piece in listof:
        if distance_formula(piece.rect.center, position) < posCounter:
            nearest = piece
            posCounter = distance_formula(piece.rect.center, position)
    return nearest

def is_under_check(TargetPiece, pieces):
    for piece in pieces:
        if piece.team != TargetPiece.team and newspot in piece.elgible_moves():
            return True
        else:
            return False

def nearest_pos(position, listofPos):
    nearest = None
    posCounter = 50000  # a very high number/ could use board dimension^2
    for pos in listofPos:
        if distance_formula(pos.center, position) < posCounter:
            nearest = pos
            posCounter = distance_formula(pos.center, position)
    return nearest


def getangles_of_removes(Input):
    output = []
    for x,y in Input:
        if y not in output:
            output.append(y)

    return output

def near(Y,Input):
    output = {}
    List = []
    for x,y in Input:
        if y in output:
            output[y].append(x)
        else:
            output[y] = [x]

    for i in Y:
        List.append((i,output[i]))
    return List

















