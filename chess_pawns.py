from Requried_functions import *


class chess_piece(pygame.sprite.Sprite):


    def __init__(self, image, position, team):
        pygame.sprite.Sprite.__init__(self)
        self.team = team
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(70,70))
        self.position = position
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = position.topleft
        self.rect.center = position.center

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

    def drag(self, cursor):
        self.rect.center = cursor

    def update(self, position):
        self.position = position
        self.rect.center = position.center


class king(chess_piece):
    def __init__(self,image, position, team):
        chess_piece.__init__(self,image,position,team)

    def elgible_moves(self):
        moves_if_no_blocls = movable_squares(self.position,square_boxes,[0,pi,pi/2,-pi/2,pi/4,-pi/4,3*pi/4,-3*pi/4])
        move_list = []
        dis = distance_formula(square_boxes[1], square_boxes[8])
        for pos in moves_if_no_blocls:
            if distance_formula(self.position, pos)<= dis:
                move_list.append(pos)
        return move_list

drawboard()
# This function is called to initialise the following chess pieces with in the square boxes defined in the function

piece = king("Media\wking.jpeg", square_boxes[60], 'White')

